from flask import Flask
from flask_session import Session

# Se crea la aplicación Flask
app = Flask(__name__)

# Se configura la clave secreta
app.secret_key = 'admin123'

# Se configura el tipo de sesión
app.config['SESSION_TYPE'] = 'filesystem'

# Inicializa la extensión de sesiones
Session(app)

# Se importan los controladores
from controladores import usuario_controller, contactos_controller

# Se ejecuta la app solo si este archivo es el principal
if __name__ == "__main__":
    app.run(debug=True, port=5000)
