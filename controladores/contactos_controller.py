# controladores/contactos_controller.py
from flask import render_template, request, redirect, session, flash
from modelos.contactos_model import (
    listar_contactos,
    agregar_contacto,
    obtener_contacto_por_id,
    actualizar_contacto,
    eliminar_contacto
)

def init_contactos_controller(app):
    """Registra las rutas de gestión de contactos en la app Flask."""

    @app.route('/contactos')
    def contactos():
        if 'usuario_id' not in session:
            return redirect('/login')
        contactos_lista = listar_contactos(session['usuario_id'])
        return render_template('contactos.html', contactos=contactos_lista)

    @app.route('/contactos/agregar', methods=['GET', 'POST'])
    def agregar():
        if 'usuario_id' not in session:
            return redirect('/login')
        if request.method == 'POST':
            nombre = request.form.get('nombre', '').strip()
            if not nombre:
                flash('El nombre es obligatorio.', 'danger')
                return render_template('formulario_contacto.html', accion='Agregar')
            correo = request.form.get('correo', '').strip()
            telefono = request.form.get('telefono', '').strip()
            notas = request.form.get('notas', '').strip()
            agregar_contacto(session['usuario_id'], nombre, correo, telefono, notas)
            flash('Contacto agregado correctamente.', 'success')
            return redirect('/contactos')
        return render_template('formulario_contacto.html', accion='Agregar')

    @app.route('/contactos/editar/<int:id>', methods=['GET', 'POST'])
    def editar(id):
        if 'usuario_id' not in session:
            return redirect('/login')
        contacto = obtener_contacto_por_id(id, session['usuario_id'])
        if not contacto:
            flash('Contacto no encontrado.', 'danger')
            return redirect('/contactos')
        if request.method == 'POST':
            nombre = request.form.get('nombre', '').strip()
            if not nombre:
                flash('El nombre es obligatorio.', 'danger')
                return render_template('formulario_contacto.html', accion='Editar', contact=contacto)
            correo = request.form.get('correo', '').strip()
            telefono = request.form.get('telefono', '').strip()
            notas = request.form.get('notas', '').strip()
            actualizar_contacto(id, session['usuario_id'], nombre, correo, telefono, notas)
            flash('Contacto actualizado correctamente.', 'success')
            return redirect('/contactos')
        return render_template('formulario_contacto.html', accion='Editar', contact=contacto)

    @app.route('/contactos/eliminar/<int:id>', methods=['POST'])
    def eliminar(id):
        if 'usuario_id' not in session:
            return redirect('/login')
        eliminar_contacto(id, session['usuario_id'])
        flash('Contacto eliminado correctamente.', 'success')
        return redirect('/contactos')