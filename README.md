# Frutería Los Papus
Este proyecto es una aplicación web desarrollada en Python utilizando el micro-framework Flask, Ngrok como puente a internet y MongoDB como base de datos. El objetivo principal es la gestión y el control de existencias de productos para una frutería.

Proyecto desarrollado para la clase del profe Treviño.

### Características Principales
Autenticación Completa: Sistema de registro de usuarios e inicio de sesión seguro.

Recuperación de Contraseña: Mecanismo de seguridad mediante la generación de un código temporal de 6 dígitos con expiración de 10 minutos.

Control de Existencias: Visualización dinámica de los productos del inventario, incluyendo precios por kilogramo y stock .

### Librerias
Gestor de Entorno/Paquetes: uv 
Python
Flask
flask-mail
Base de Datos: MongoDB Atlas (NoSQL)
requirements.txt
pyproject.toml

### Instrucciones
La primera forma seria usando uv sync para sincronizar de forma Correcta el entorno virtual
luego correremos el codigo con uv run app.py

una segunda forma para correr de forma correcta el codigo crearemos un entorno virtual y lo activaremos

una vez activo descargaremos el contenido de requirements.txt en la terminal con este comando pip install -r requirements.txt
y tambien actualizaremos el pip con este comando  python.exe -m pip install --upgrade pip

###Para usar el codigo en linea usando Ngrok

buscaremos ngrok en la microsoft store y lo descargaremos (es la forma mas segura de descargar porque desde el navegador lo detecta como virus)
<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/6006b892-00e4-4ef0-b91b-a74d47d4975f" />

mientras se descarga o despues de descargar Ngrok iniciaremos sesion en ngrok o creara una cuenta en la pagina web
<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/db5c8c8e-0528-46d3-b220-efc491232ed2" />

una ves iniciado sesion se van al apartado ala izquierda de Your Authtoken
<img width="262" height="214" alt="image" src="https://github.com/user-attachments/assets/baf1c05f-86f5-4f4b-ab0e-57768c56765d" />

una ves en el apartado de Your Authtoken tendra que copiar el codigo de abajo que sera este, ngrok config add-authtoken despues de este codigo sera el authtoken personal que estara censurado por si lo quiere mostrar o ocultar, quedaria algo asi 
ngrok config add-authtoken 3EDdVEtvhCoDrkpbIKodzzVC3zx_6imcdJ9kFviN44LQCRht6
<img width="1005" height="631" alt="image" src="https://github.com/user-attachments/assets/a6c5a6f4-dd63-474a-b32c-231f658004d9" />

despues de sacar este codigo tendremos que ejecutar ngrok como administrador
<img width="799" height="507" alt="image" src="https://github.com/user-attachments/assets/4d723634-b618-4b24-b7fa-8e0b4c0201a2" />

al ejecutarlo como administrador meteremos el codigo que copiamos anterior mente y le daremos enter
<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/bc6b854d-5ac6-4d76-aaf8-d9c45e662187" />

una vez dado enter tendremos que ir a nuestro codigo y correrlo pero en ves de ir directa mente ala url copiaremos la ip y abriremos otra terminal ahi pondremos este codigo ngrok http y al final pegaremos la ip y le damos enter, asi quedaria 
ngrok http http://127.0.0.1:5000
<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/cd501d7d-db49-42bb-974d-a5de05ee72c6" />

<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/7383deed-702e-4402-ab01-5c29750c6d26" />

una ves hecho esto la pagina ya esta en internet en la foto la ip correspondiente seria la 
Forwarding                    https://chess-aspirin-fragile.ngrok-free.dev
hecho esto servira la parte de recuperacion de contraseña enviando un codigo de 6 digitos desde una cuenta secundaria creada solo para este codigo y todo se guardara en mongo atlas
para que funcione correctamente tiene que estar ngrok y la pagina ejecutandose

## Corral Lopez Damian 
## Carcamo Limon Miguel Angel

<img width="899" height="1599" alt="WhatsApp Image 2026-05-25 at 12 00 26 PM" src="https://github.com/user-attachments/assets/a61e99dd-e308-47a8-894e-c2b2e6f156e7" />
<img width="1200" height="1600" alt="WhatsApp Image 2026-05-25 at 12 02 03 PM" src="https://github.com/user-attachments/assets/1480ff30-1222-413f-925f-6ce14b2614e5" />
