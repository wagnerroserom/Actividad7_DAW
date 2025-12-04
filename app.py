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
from controladores.usuario_controller import init_usuario_controller
from controladores.contactos_controller import init_contactos_controller

init_usuario_controller(app)
init_contactos_controller(app)

# Ruta raíz obligatoria
@app.route('/')
def index():
    return redirect('/login')

# Se ejecuta la app solo si este archivo es el principal
if __name__ == "__main__":
    app.run(debug=True, port=5000)
