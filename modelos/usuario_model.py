from config import conexion
from werkzeug.security import generate_password_hash, check_password_hash

def registrar_usuario(nombre, correo, contrasena):
    """ Permite registrar un nuevo usuario en la base de datos.
    La contraseña se almacena encriptada usando hashing. """

    conn = conexion()
    cursor = conn.cursor()
    contrasena_hash = generate_password_hash(contrasena)
    cursor.execute(
        "INSERT INTO usuarios (nombre, correo, contrasena_hash) VALUES (%s, %s, %s)",
        (nombre, correo, contrasena_hash)
    )
    conn.commit()
    cursor.close()
    conn.close()

def obtener_usuario_por_correo(correo):
    """ Devuelve un usuario por su correo """
    conn = conexion()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM usuarios WHERE correo = %s", (correo,))
    usuario = cursor.fetchone()
    cursor.close()
    conn.close()
    return usuario

def verificar_usuario(correo, contrasena):
    """ Constata si las credenciales son correctas.
    Devuelve el usuario si la contraseña coincide  """

    usuario = obtener_usuario_por_correo(correo)
    if usuario and check_password_hash(usuario['contrasena_hash'], contrasena):
        return usuario
    return None