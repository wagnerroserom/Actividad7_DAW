# Conexión con MySQL usando XAMPP
import mysql.connector

def conexion():
    """ Establece y devuelve la conexión con la base de datos 'agenda_db' """

    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="agenda_db"
    )