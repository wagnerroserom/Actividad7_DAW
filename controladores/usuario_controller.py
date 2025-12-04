# controladores/usuario_controller.py
from flask import render_template, request, redirect, session, flash
from modelos.usuario_model import registrar_usuario, verificar_usuario

def init_usuario_controller(app):
    """Registra las rutas de autenticación en la app Flask."""

    @app.route('/registro', methods=['GET', 'POST'])
    def registro():
        if request.method == 'POST':
            nombre = request.form['nombre'].strip()
            correo = request.form['correo'].strip()
            contrasena = request.form['contrasena']
            if len(contrasena) < 8:
                flash('La contraseña debe tener al menos 8 caracteres.', 'danger')
                return render_template('registro.html')
            if verificar_usuario_existente(correo):
                flash('El correo ya está registrado.', 'danger')
                return render_template('registro.html')
            registrar_usuario(nombre, correo, contrasena)
            flash('Usuario registrado correctamente. Ahora puede iniciar sesión.', 'success')
            return redirect('/login')
        return render_template('registro.html')

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            correo = request.form['correo']
            contrasena = request.form['contrasena']
            usuario = verificar_usuario(correo, contrasena)
            if usuario:
                session['usuario_id'] = usuario['id']
                session['nombre'] = usuario['nombre']
                return redirect('/contactos')
            flash('Correo o contraseña incorrectos.', 'danger')
        return render_template('login.html')

    @app.route('/salir')
    def salir():
        session.clear()
        flash('Ha cerrado sesión correctamente.', 'info')
        return redirect('/login')

# Función auxiliar para verificar si el correo ya existe
def verificar_usuario_existente(correo):
    from modelos.usuario_model import obtener_usuario_por_correo
    return obtener_usuario_por_correo(correo) is not None