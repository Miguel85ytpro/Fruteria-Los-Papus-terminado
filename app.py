from flask import Flask, render_template, request, redirect, url_for, session
from pymongo import MongoClient
import random
from datetime import datetime, timedelta, timezone
from flask_mail import Mail, Message
from bson.objectid import ObjectId

app = Flask(__name__)
app.secret_key = 'clave_secreta_papus'

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'fruterialospapus@gmail.com'
app.config['MAIL_PASSWORD'] = 'vdsb uadx wkzu rukg'
app.config['MAIL_DEFAULT_SENDER'] = 'fruterialospapus@gmail.com'

mail = Mail(app)

MONGO_URI = "mongodb+srv://miguel85yt1_db_user:Carcam010@fruteria.3a76l9l.mongodb.net/?appName=Fruteria"
client = MongoClient(MONGO_URI)
db = client['fruteria_db']
usuarios_col = db['usuarios']
tokens_col = db['tokens_recuperacion']
productos_col = db['productos']

@app.route("/")
def index():
    productos = []
    if 'user' in session:
        productos = list(productos_col.find())
    return render_template("index.html", productos=productos)

@app.route("/login", methods=['GET', 'POST'])
def login():
    error = request.args.get('error')
    exito = request.args.get('exito')
    if request.method == 'POST':
        u = request.form.get('usuario')
        p = request.form.get('password')
        user = usuarios_col.find_one({"usuario": u, "password": p})
        if user:
            session['user'] = u
            return redirect(url_for('index'))
        error = "Usuario o contraseña incorrectos."
    return render_template("login.html", error=error, exito=exito)

@app.route("/registro", methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        u = request.form.get('usuario')
        c = request.form.get('correo')
        p = request.form.get('password')
        if u and c and p:
            if usuarios_col.find_one({"usuario": u}):
                return render_template("registro.html", error="El nombre de usuario ya existe.")
            if usuarios_col.find_one({"correo": c}):
                return render_template("registro.html", error="El correo ya está registrado.")
            usuarios_col.insert_one({"usuario": u, "correo": c, "password": p})
            return redirect(url_for('login', exito="Cuenta creada con éxito. Ahora puedes iniciar sesión."))
    return render_template("registro.html")

@app.route("/logout")
def logout():
    session.pop('user', None)
    return redirect(url_for('index'))

@app.route("/inventario")
def inventario():
    if 'user' not in session:
        return redirect(url_for('login'))
    productos = list(productos_col.find())
    return render_template("inventario.html", productos=productos)

@app.route("/inventario/agregar", methods=['POST'])
def agregar_producto():
    nombre = request.form.get('nombre')
    precio = request.form.get('precio')
    stock = request.form.get('stock')
    estado = request.form.get('estado')
    productos_col.insert_one({
        "nombre": nombre,
        "precio_kg": float(precio),
        "stock": float(stock),
        "estado": estado
    })
    return redirect(url_for('inventario'))

@app.route("/inventario/editar/<id_prod>", methods=['POST'])
def editar_producto(id_prod):
    nuevo_estado = request.form.get('estado')
    nuevo_stock = request.form.get('stock')
    nuevo_precio = request.form.get('precio')
    productos_col.update_one(
        {"_id": ObjectId(id_prod)},
        {"$set": {
            "estado": nuevo_estado, 
            "stock": float(nuevo_stock),
            "precio_kg": float(nuevo_precio)
        }}
    )
    return redirect(url_for('inventario'))

@app.route("/inventario/eliminar/<id_prod>")
def eliminar_producto(id_prod):
    productos_col.delete_one({"_id": ObjectId(id_prod)})
    return redirect(url_for('inventario'))

@app.route("/recuperar", methods=['GET', 'POST'])
def recuperar():
    if request.method == 'POST':
        correo = request.form.get('correo')
        user = usuarios_col.find_one({"correo": correo})
        if not user:
            return render_template("recuperar_contraseña.html", error="El correo no está registrado.")
        tokens_col.delete_many({"correo": correo})
        codigo_otp = str(random.randint(100000, 999999))
        expiracion = datetime.now(timezone.utc) + timedelta(minutes=10)
        tokens_col.insert_one({"correo": correo, "token": codigo_otp, "expiracion": expiracion})
        try:
            msg = Message("Código de Recuperación - Frutería Papus", recipients=[correo])
            msg.body = f"Hola {user['usuario']}, tu código de seguridad es: {codigo_otp}. Expira en 10 minutos."
            mail.send(msg)
            return render_template("recuperar_contraseña.html", otp_generado=True, correo_otp=correo, info="Código enviado al correo.")
        except Exception as e:
            return render_template("recuperar_contraseña.html", error="Error al enviar el correo.")
    return render_template("recuperar_contraseña.html")

@app.route("/verificar-otp", methods=['POST'])
def verificar_otp():
    correo = request.form.get('correo')
    codigo_ingresado = request.form.get('codigo_otp')
    doc = tokens_col.find_one({"correo": correo, "token": codigo_ingresado})
    if not doc:
        return render_template("recuperar_contraseña.html", error="Código incorrecto.")
    if datetime.now(timezone.utc) > doc['expiracion'].replace(tzinfo=timezone.utc):
        tokens_col.delete_one({"_id": doc["_id"]})
        return render_template("recuperar_contraseña.html", error="El código ha expirado.")
    return render_template("restablecer.html", correo=correo, token=codigo_ingresado)

@app.route("/restablecer-proceso", methods=['POST'])
def restablecer_proceso():
    correo = request.form.get('correo')
    codigo = request.form.get('token')
    nueva_password = request.form.get('password')
    doc = tokens_col.find_one({"correo": correo, "token": codigo})
    if not doc:
        return "Acción no autorizada.", 403
    usuarios_col.update_one({"correo": correo}, {"$set": {"password": nueva_password}})
    tokens_col.delete_many({"correo": correo})
    return redirect(url_for('login', exito="Contraseña actualizada correctamente."))

if __name__ == "__main__":
    app.run(debug=True, port=5000)