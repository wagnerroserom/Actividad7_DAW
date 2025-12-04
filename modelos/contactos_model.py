from config import conexion

def listar_contactos(usuario_id):
    """ Se prevee devolver todos los contactos de un usuario. """
    conn = conexion()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM contactos WHERE usuario_id = %s", (usuario_id,))
    contactos = cursor.fetchall()
    cursor.close()
    conn.close()
    return contactos

def agregar_contacto(usuario_id, nombre, correo, telefono, detalle):
    """ Se le permite agregar un nuevo contacto. """
    conn = conexion()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO contactos (usuario_id, nombre, correo, telefono, detalle) VALUES (%s, %s, %s, %s, %s)",
        (usuario_id, nombre, correo, telefono, detalle)
    )
    conn.commit()
    cursor.close()
    conn.close()

def obtener_contacto_por_id(id, usuario_id):
    """ Se obtiene un contacto específico si pertenece al usuario. """
    conn = conexion()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM contactos WHERE id = %s AND usuario_id = %s", (id, usuario_id))
    contacto = cursor.fetchone()
    cursor.close()
    conn.close()
    return contacto   

def actualizar_contacto(id, usuario_id, nombre, correo, telefono, detalle):
    """ Se permite actualizar un contacto si pertenece al usuario. """
    conn = conexion()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE contactos SET nombre=%s, correo=%s, telefono=%s, detalle=%s WHERE id=%s AND usuario_id=%s",
        (nombre, correo, telefono, detalle, id, usuario_id)
    )
    conn.commit()
    cursor.close()
    conn.close()

def eliminar_contacto(id, usuario_id):
    """ Se permite eliminar un contacto si pertenece al usuario. """
    conn = conexion()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM contactos WHERE id=%s AND usuario_id=%s", (id, usuario_id))
    conn.commit()
    cursor.close()
    conn.close()