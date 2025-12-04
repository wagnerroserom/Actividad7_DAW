from flask import render_template, request, redirect, session, flash
from app import app
from modelos.usuario_model import registrar_usuario, verificar_usuario

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    """ Muestra el formulario de registro o procesa el envío. """
    if request.method == 'POST':
        nombre = request.form['nombre']
        correo = request.form['correo']
        contrasena = request.form['contrasena']
        registrar_usuario(nombre, correo, contrasena)
        flash('Usuario registrado correctamente.', 'success')
        return redirect('/login')
    return render_template('registro.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """ Muestra el formulario de login o valida credenciales. """
    if request.method == 'POST':
        correo = request.form['correo']
        contrasena = request.form['contrasena']
        usuario = verificar_usuario(correo, contrasena)
        if usuario:
            session['usuario_id'] = usuario['id']
            session['nombre'] = usuario['nombre']
            return redirect('/contactos')
        flash('Credenciales incorrectas.', 'danger')
    return render_template('login.html')

@app.route('/salir')
def salir():
    """Cierra la sesión del usuario."""
    session.clear()
    return redirect('/login')