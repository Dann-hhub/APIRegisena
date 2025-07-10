from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
from flask_cors import CORS 
from config import config

app = Flask(__name__)

CORS(app)
conexion = MySQL(app)

#LISTAR
@app.route('/tipoequipo', methods=['GET'])
def listar_tipoequipo():
    try:
        cursor = conexion.connection.cursor()
        sql = 'SELECT * FROM tipoequipos'
        cursor.execute(sql)
        datos = cursor.fetchall()
        tipoequipos = []
        for fila in datos:
            tipoequipo={'id':fila[0], 'nombre':fila[1], 'estado':fila[2]}
            tipoequipos.append(tipoequipo)
        return jsonify({'tipoequipos': tipoequipos, 'mensaje': 'Tipo Equipos Listados.'})
    except Exception as ex:
        return jsonify({'mensaje': 'Error!'})

#BUSCAR
@app.route('/tipoequipo/<id>', methods=['GET'])
def leer_tipoequipo(id):
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT * FROM tipoequipos WHERE id = '{0}'".format(id)
        cursor.execute(sql)
        datos = cursor.fetchone()
        if datos != None:
            tipoequipo={'id':datos[0], 'nombre':datos[1], 'estado':datos[2]}
            return jsonify({'tipoequipo': tipoequipo, 'mensaje': 'Tipo Equipo Encontrado.'})
        else:
            return jsonify({'mensaje': 'Tipo Equipo no encontrado'})
    except Exception as ex:
        return jsonify({'mensaje': 'Error!'})

#CREAR
@app.route('/tipoequipo', methods=['POST'])
def crear_tipoequipo():
    try:
        cursor = conexion.connection.cursor()
        sql = "INSERT INTO tipoequipos (id, nombre, estado) VALUES ('{0}', '{1}', {2})""".format(request.json['id'], request.json['nombre'], request.json['estado'])
        cursor.execute(sql)
        conexion.connection.commit() #confirma la accion de creación
        return jsonify({'mensaje': 'Tipo Equipo creado.'})
    except Exception as ex:
        return jsonify({'mensaje': 'Error!'})
    
#ELIMINAR
@app.route('/tipoequipo/<id>', methods=['DELETE'])
def eliminar_tipoequipo(id):
    try:
        cursor = conexion.connection.cursor()
        sql = "DELETE FROM tipoequipos WHERE id = '{0}'".format(id)
        cursor.execute(sql)
        conexion.connection.commit() #confirma la accion de creación
        return jsonify({'mensaje': 'Tipo Equipo eliminado.'})
    except Exception as ex:
        return jsonify({'mensaje': 'Error!'})

#ACTUALIZAR
@app.route('/tipoequipo/<id>', methods=['PUT'])
def editar_tipoequipo(id):
    try:
        cursor = conexion.connection.cursor()
        sql = "UPDATE tipoequipos SET nombre = '{0}', estado = {1} WHERE id = '{2}'""".format(request.json['nombre'], request.json['estado'], id)
        cursor.execute(sql)
        conexion.connection.commit() #confirma la accion de creación
        return jsonify({'mensaje': 'Tipo Equipo actualizado.'})
    except Exception as ex:
        return jsonify({'mensaje': 'Error!'})
    
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------

#LISTAR
@app.route('/tipopersona', methods=['GET'])
def listar_tipopersona():
    try:
        cursor = conexion.connection.cursor()
        sql = 'SELECT * FROM tipopersonas'
        cursor.execute(sql)
        datos = cursor.fetchall()
        tipopersonas = []
        for fila in datos:
            tipopersona={'id':fila[0], 'nombre':fila[1], 'estado':fila[2]}
            tipopersonas.append(tipopersona)
        return jsonify({'tipopersonas': tipopersonas, 'mensaje': 'Tipo Personas Listados.'})
    except Exception as ex:
        return jsonify({'mensaje': 'Error!'})

#BUSCAR
@app.route('/tipopersona/<id>', methods=['GET'])
def leer_tipopersona(id):
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT * FROM tipopersonas WHERE id = '{0}'".format(id)
        cursor.execute(sql)
        datos = cursor.fetchone()
        if datos != None:
            tipopersona={'id':datos[0], 'nombre':datos[1], 'estado':datos[2]}
            return jsonify({'tipopersona': tipopersona, 'mensaje': 'Tipo Persona Encontrado.'})
        else:
            return jsonify({'mensaje': 'Tipo Persona no encontrado'})
    except Exception as ex:
        return jsonify({'mensaje': 'Error!'})

#CREAR
@app.route('/tipopersona', methods=['POST'])
def crear_tipopersona():
    try:
        cursor = conexion.connection.cursor()
        sql = "INSERT INTO tipopersonas (id, nombre, estado) VALUES ('{0}', '{1}', {2})""".format(request.json['id'], request.json['nombre'], request.json['estado'])
        cursor.execute(sql)
        conexion.connection.commit() #confirma la accion de creación
        return jsonify({'mensaje': 'Tipo Persona creado.'})
    except Exception as ex:
        return jsonify({'mensaje': 'Error!'})
    
#ELIMINAR
@app.route('/tipopersona/<id>', methods=['DELETE'])
def eliminar_tipopersona(id):
    try:
        cursor = conexion.connection.cursor()
        sql = "DELETE FROM tipopersonas WHERE id = '{0}'".format(id)
        cursor.execute(sql)
        conexion.connection.commit() #confirma la accion de creación
        return jsonify({'mensaje': 'Tipo Persona eliminado.'})
    except Exception as ex:
        return jsonify({'mensaje': 'Error!'})

#ACTUALIZAR
@app.route('/tipopersona/<id>', methods=['PUT'])
def editar_tipopersona(id):
    try:
        cursor = conexion.connection.cursor()
        sql = "UPDATE tipopersonas SET nombre = '{0}', estado = {1} WHERE id = '{2}'""".format(request.json['nombre'], request.json['estado'], id)
        cursor.execute(sql)
        conexion.connection.commit() #confirma la accion de creación
        return jsonify({'mensaje': 'Tipo Persona actualizado.'})
    except Exception as ex:
        return jsonify({'mensaje': 'Error!'})
    
#----------------------------------------------------------------------------------------------------------------------------------------------------------------

#LISTAR
@app.route('/rol', methods=['GET'])
def listar_roles():
    try:
        cursor = conexion.connection.cursor()
        sql = 'SELECT * FROM rol'
        cursor.execute(sql)
        datos = cursor.fetchall()
        roles = []
        for fila in datos:
            rol={'id':fila[0], 'nombre':fila[1], 'estado':fila[2], 'fechaCreacion':fila[3]}
            roles.append(rol)
        return jsonify({'roles': roles, 'mensaje': 'Roles Listados.'})
    except Exception as ex:
        return jsonify({'mensaje': 'Error!'})

#BUSCAR
@app.route('/rol/<id>', methods=['GET'])
def leer_rol(id):
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT * FROM rol WHERE id = '{0}'".format(id)
        cursor.execute(sql)
        datos = cursor.fetchone()
        if datos != None:
            rol={'id':datos[0], 'nombre':datos[1], 'estado':datos[2], 'FechaCreacion':datos[3]}
            return jsonify({'rol': rol, 'mensaje': 'Rol Encontrado.'})
        else:
            return jsonify({'mensaje': 'Rol no encontrado'})
    except Exception as ex:
        return jsonify({'mensaje': 'Error!'})

#CREAR
@app.route('/rol', methods=['POST'])
def crear_rol():
    try:
        cursor = conexion.connection.cursor()
        sql = "INSERT INTO rol (id, nombre, estado, fechaCreacion) VALUES ('{0}', '{1}', {2}, '{3}')""".format(request.json['id'], request.json['nombre'], request.json['estado'], request.json['fechaCreacion'])
        cursor.execute(sql)
        conexion.connection.commit() #confirma la accion de creación
        return jsonify({'mensaje': 'Rol creado.'})
    except Exception as ex:
        return jsonify({'mensaje': 'Error!'})
    
#ELIMINAR
@app.route('/rol/<id>', methods=['DELETE'])
def eliminar_rol(id):
    try:
        cursor = conexion.connection.cursor()
        sql = "DELETE FROM rol WHERE id = '{0}'".format(id)
        cursor.execute(sql)
        conexion.connection.commit() #confirma la accion de creación
        return jsonify({'mensaje': 'Rol eliminado.'})
    except Exception as ex:
        return jsonify({'mensaje': 'Error!'})

#ACTUALIZAR
@app.route('/rol/<id>', methods=['PUT'])
def editar_rol(id):
    try:
        cursor = conexion.connection.cursor()
        sql = "UPDATE rol SET nombre = '{0}', estado = {1}, fechaCreacion = '{2}' WHERE id = '{3}'""".format(request.json['nombre'], request.json['estado'], request.json['fechaCreacion'], id)
        cursor.execute(sql)
        conexion.connection.commit() #confirma la accion de creación
        return jsonify({'mensaje': 'Rol actualizado.'})
    except Exception as ex:
        return jsonify({'mensaje': 'Error!'})
    
#----------------------------------------------------------------------------------------------------------------------------------------------------------------

#LISTAR
@app.route('/permiso', methods=['GET'])
def listar_permisos():
    try:
        cursor = conexion.connection.cursor()
        sql = 'SELECT * FROM permiso'
        cursor.execute(sql)
        datos = cursor.fetchall()
        permisos = []
        for fila in datos:
            permiso={'id':fila[0], 'nombre':fila[1]}
            permisos.append(permiso)
        return jsonify({'permisos': permisos, 'mensaje': 'permisos Listados.'})
    except Exception as ex:
        return jsonify({'mensaje': 'Error!'})

#BUSCAR
@app.route('/permiso/<id>', methods=['GET'])
def leer_permiso(id):
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT * FROM permiso WHERE id = '{0}'".format(id)
        cursor.execute(sql)
        datos = cursor.fetchone()
        if datos != None:
            permiso={'id':datos[0], 'nombre':datos[1]}
            return jsonify({'permiso': permiso, 'mensaje': 'Permiso Encontrado.'})
        else:
            return jsonify({'mensaje': 'Permiso no encontrado'})
    except Exception as ex:
        return jsonify({'mensaje': 'Error!'})

#CREAR
@app.route('/permiso', methods=['POST'])
def crear_permiso():
    try:
        cursor = conexion.connection.cursor()
        sql = "INSERT INTO permiso (id, nombre) VALUES ('{0}', '{1}')""".format(request.json['id'], request.json['nombre'])
        cursor.execute(sql)
        conexion.connection.commit() #confirma la accion de creación
        return jsonify({'mensaje': 'Permiso creado.'})
    except Exception as ex:
        return jsonify({'mensaje': 'Error!'})
    
#ELIMINAR
@app.route('/permiso/<id>', methods=['DELETE'])
def eliminar_permiso(id):
    try:
        cursor = conexion.connection.cursor()
        sql = "DELETE FROM permiso WHERE id = '{0}'".format(id)
        cursor.execute(sql)
        conexion.connection.commit() #confirma la accion de creación
        return jsonify({'mensaje': 'Permiso eliminado.'})
    except Exception as ex:
        return jsonify({'mensaje': 'Error!'})

#ACTUALIZAR
@app.route('/permiso/<id>', methods=['PUT'])
def editar_permiso(id):
    try:
        cursor = conexion.connection.cursor()
        sql = "UPDATE permiso SET nombre = '{0}' WHERE id = '{1}'""".format(request.json['nombre'], id)
        cursor.execute(sql)
        conexion.connection.commit() #confirma la accion de creación
        return jsonify({'mensaje': 'Permiso actualizado.'})
    except Exception as ex:
        return jsonify({'mensaje': 'Error!'})
    
#----------------------------------------------------------------------------------------------------------------------------------------------------------------

#LISTAR
@app.route('/equipo', methods=['GET'])
def listar_equipos():
    try:
        cursor = conexion.connection.cursor()
        sql = 'SELECT * FROM equipos'
        cursor.execute(sql)
        datos = cursor.fetchall()
        equipos = []
        for fila in datos:
            equipo={'serial':fila[0], 'marca':fila[1], 'accesorios':fila[2], 'color':fila[3], 'fechaRegistro':fila[4], 'tipoEquipoId':fila[5], 'estado':fila[6]}
            equipos.append(equipo)
        return jsonify({'equipos': equipos, 'mensaje': 'Equipos Listados.'})
    except Exception as ex:
        return jsonify({'mensaje': 'Error!'})

#BUSCAR
@app.route('/equipo/<serial>', methods=['GET'])
def leer_equipo(serial):
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT * FROM equipos WHERE serial = '{0}'".format(serial)
        cursor.execute(sql)
        datos = cursor.fetchone()
        if datos != None:
            equipo={'serial':datos[0], 'marca':datos[1], 'accesorios':datos[2], 'color':datos[3], 'fechaRegistro':datos[4], 'tipoEquipoId':datos[5], 'estado':datos[6]}
            return jsonify({'equipo': equipo, 'mensaje': 'Equipo Encontrado.'})
        else:
            return jsonify({'mensaje': 'Equipo no encontrado'})
    except Exception as ex:
        return jsonify({'mensaje': 'Error!'})

#CREAR
@app.route('/equipo', methods=['POST'])
def crear_equipo():
    try:
        cursor = conexion.connection.cursor()
        sql = "INSERT INTO equipos (serial, marca, accesorios, color, fechaRegistro, tipoEquipoId, estado) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', {6})""".format(request.json['serial'], request.json['marca'], request.json['accesorios'], request.json['color'], request.json['fechaRegistro'], request.json['tipoEquipoId'], request.json['estado'])
        cursor.execute(sql)
        conexion.connection.commit() #confirma la accion de creación
        return jsonify({'mensaje': 'Equipo creado.'})
    except Exception as ex:
        return jsonify({'mensaje': 'Error!'})
    
#ELIMINAR
@app.route('/equipo/<serial>', methods=['DELETE'])
def eliminar_equipo(serial):
    try:
        cursor = conexion.connection.cursor()
        sql = "DELETE FROM equipos WHERE serial = '{0}'".format(serial)
        cursor.execute(sql)
        conexion.connection.commit() #confirma la accion de creación
        return jsonify({'mensaje': 'Equipo eliminado.'})
    except Exception as ex:
        return jsonify({'mensaje': 'Error!'})

#ACTUALIZAR
@app.route('/equipo/<serial>', methods=['PUT'])
def editar_equipo(serial):
    try:
        cursor = conexion.connection.cursor()
        sql = """UPDATE equipos SET marca = '{0}', accesorios = '{1}', color = '{2}', fechaRegistro = '{3}', tipoEquipoId = '{4}', estado = {5} WHERE serial = '{6}'""".format(request.json['marca'], request.json['accesorios'], request.json['color'], request.json['fechaRegistro'], request.json['tipoEquipoId'], request.json['estado'], serial)
        cursor.execute(sql)
        conexion.connection.commit()
        return jsonify({'mensaje': 'Equipo actualizado correctamente.'})
    except Exception as ex:
        return jsonify({'mensaje': 'Error al actualizar equipo', 'error': str(ex)}), 500
    
#----------------------------------------------------------------------------------------------------------------------------------------------------------------

#LISTAR
@app.route('/usuario', methods=['GET'])
def listar_usuarios():
    try:
        cursor = conexion.connection.cursor()
        sql = 'SELECT * FROM usuario'
        cursor.execute(sql)
        datos = cursor.fetchall()
        usuarios = []
        for fila in datos:
            usuario={'documento':fila[0], 'tipoDocumento':fila[1], 'nombre':fila[2], 'apellido':fila[3], 'rol':fila[4], 'correo':fila[5], 'contrasena':fila[6], 'estado':fila[7]}
            usuarios.append(usuario)
        return jsonify({'usuarios': usuarios, 'mensaje': 'Usuarios Listados.'})
    except Exception as ex:
        return jsonify({'mensaje': 'Error!'})

#BUSCAR
@app.route('/usuario/<documento>', methods=['GET'])
def leer_usuario(documento):
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT * FROM usuario WHERE documento = '{0}'".format(documento)
        cursor.execute(sql)
        datos = cursor.fetchone()
        if datos != None:
            usuario={'documento':datos[0], 'tipoDocumento':datos[1], 'nombre':datos[2], 'apellido':datos[3], 'rol':datos[4], 'correo':datos[5], 'contrasena':datos[6], 'estado':datos[7]}
            return jsonify({'usuario': usuario, 'mensaje': 'Usuario Encontrado.'})
        else:
            return jsonify({'mensaje': 'Usuario no encontrado'})
    except Exception as ex:
        return jsonify({'mensaje': 'Error!'})

#CREAR
@app.route('/usuario', methods=['POST'])
def crear_usuario():
    try:
        cursor = conexion.connection.cursor()
        sql = "INSERT INTO usuario (documento, tipoDocumento, nombre, apellido, rol, correo, contrasena, estado) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', {7})""".format(request.json['documento'], request.json['tipoDocumento'], request.json['nombre'], request.json['apellido'], request.json['rol'], request.json['correo'], request.json['contrasena'], request.json['estado'])
        cursor.execute(sql)
        conexion.connection.commit() #confirma la accion de creación
        return jsonify({'mensaje': 'Usuario creado.'})
    except Exception as ex:
        return jsonify({'mensaje': 'Error!'})
    
#ELIMINAR
@app.route('/usuario/<documento>', methods=['DELETE'])
def eliminar_usuario(documento):
    try:
        cursor = conexion.connection.cursor()
        sql = "DELETE FROM usuario WHERE documento = '{0}'".format(documento)
        cursor.execute(sql)
        conexion.connection.commit() #confirma la accion de creación
        return jsonify({'mensaje': 'Usuario eliminado.'})
    except Exception as ex:
        return jsonify({'mensaje': 'Error!'})

#ACTUALIZAR
@app.route('/usuario/<documento>', methods=['PUT'])
def editar_usuario(documento):
    try:
        cursor = conexion.connection.cursor()
        sql = """UPDATE usuario SET tipoDocumento = '{0}', nombre = '{1}', apellido = '{2}', rol = '{3}', correo = '{4}', contrasena = '{5}',  estado = {6} WHERE documento = '{7}'""".format(request.json['tipoDocumento'], request.json['nombre'], request.json['apellido'], request.json['rol'], request.json['correo'], request.json['contrasena'], request.json['estado'], documento)
        cursor.execute(sql)
        conexion.connection.commit()
        return jsonify({'mensaje': 'Usuario actualizado correctamente.'})
    except Exception as ex:
        return jsonify({'mensaje': 'Error al actualizar usuario'}), 500
    
#----------------------------------------------------------------------------------------------------------------------------------------------------------------

#LISTAR
@app.route('/persona', methods=['GET'])
def listar_personas():
    try:
        cursor = conexion.connection.cursor()
        sql = 'SELECT * FROM personas'
        cursor.execute(sql)
        datos = cursor.fetchall()
        personas = []
        for fila in datos:
            persona={'documento':fila[0], 'tipoDocumento':fila[1], 'nombre':fila[2], 'apellido':fila[3], 'tipoPersonaId':fila[4], 'equipo':fila[5], 'fechaRegistro':fila[6], 'estado':fila[7]}
            personas.append(persona)
        return jsonify({'personas': personas, 'mensaje': 'Personas Listadas.'})
    except Exception as ex:
        return jsonify({'mensaje': 'Error!'})

#BUSCAR
@app.route('/persona/<documento>', methods=['GET'])
def leer_persona(documento):
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT * FROM personas WHERE documento = '{0}'".format(documento)
        cursor.execute(sql)
        datos = cursor.fetchone()
        if datos != None:
            persona={'documento':datos[0], 'tipoDocumento':datos[1], 'nombre':datos[2], 'apellido':datos[3], 'tipoPersonaId':datos[4], 'equipo':datos[5], 'fechaRegistro':datos[6], 'estado':datos[7]}
            return jsonify({'persona': persona, 'mensaje': 'Persona Encontrada.'})
        else:
            return jsonify({'mensaje': 'Persona no encontrada'})
    except Exception as ex:
        return jsonify({'mensaje': 'Error!'})

#CREAR
@app.route('/persona', methods=['POST'])
def crear_persona():
    try:
        cursor = conexion.connection.cursor()
        sql = "INSERT INTO personas (documento, tipoDocumento, nombre, apellido, tipoPersonaId, equipo, fechaRegistro, estado) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', {7})""".format(request.json['documento'], request.json['tipoDocumento'], request.json['nombre'], request.json['apellido'], request.json['tipoPersonaId'], request.json['equipo'], request.json['fechaRegistro'], request.json['estado'])
        cursor.execute(sql)
        conexion.connection.commit() #confirma la accion de creación
        return jsonify({'mensaje': 'Persona creada.'})
    except Exception as ex:
        return jsonify({'mensaje': 'Error!'})
    
#ELIMINAR
@app.route('/persona/<documento>', methods=['DELETE'])
def eliminar_persona(documento):
    try:
        cursor = conexion.connection.cursor()
        sql = "DELETE FROM personas WHERE documento = '{0}'".format(documento)
        cursor.execute(sql)
        conexion.connection.commit() #confirma la accion de creación
        return jsonify({'mensaje': 'Persona eliminada.'})
    except Exception as ex:
        return jsonify({'mensaje': 'Error!'})

#ACTUALIZAR
@app.route('/persona/<documento>', methods=['PUT'])
def editar_persona(documento):
    try:
        cursor = conexion.connection.cursor()
        sql = """UPDATE personas SET tipoDocumento = '{0}', nombre = '{1}', apellido = '{2}', tipoPersonaId = '{3}', equipo = '{4}', fechaRegistro = '{5}',  estado = {6} WHERE documento = '{7}'""".format(request.json['tipoDocumento'], request.json['nombre'], request.json['apellido'], request.json['tipoPersonaId'], request.json['equipo'], request.json['fechaRegistro'], request.json['estado'], documento)
        cursor.execute(sql)
        conexion.connection.commit()
        return jsonify({'mensaje': 'Persona actualizada correctamente.'})
    except Exception as ex:
        return jsonify({'mensaje': 'Error al actualizar persona'}), 500
    
#----------------------------------------------------------------------------------------------------------------------------------------------------------------

#LISTAR
@app.route('/movimiento', methods=['GET'])
def listar_movimientos():
    try:
        cursor = conexion.connection.cursor()
        sql = 'SELECT * FROM movimiento'
        cursor.execute(sql)
        datos = cursor.fetchall()
        movimientos = []
        for fila in datos:
            movimiento={'id':fila[0], 'documentoPersona':fila[1], 'serialEquipo':fila[2], 'centroFormacion':fila[3], 'documentoVigilante':fila[4], 'observaciones':fila[5], 'tipoIngreso':fila[6], 'fechaIngreso':fila[7], 'tipoSalida':fila[8], 'fechaSalida':fila[9]}
            movimientos.append(movimiento)
        return jsonify({'movimientos': movimientos, 'mensaje': 'Movimientos Listados.'})
    except Exception as ex:
        return jsonify({'mensaje': 'Error!'})

#BUSCAR
@app.route('/movimiento/<id>', methods=['GET'])
def leer_movimiento(id):
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT * FROM movimiento WHERE id = '{0}'".format(id)
        cursor.execute(sql)
        datos = cursor.fetchone()
        if datos != None:
            movimiento={'id':datos[0], 'documentoPersona':datos[1], 'serialEquipo':datos[2], 'centroFormacion':datos[3], 'documentoVigilante':datos[4], 'observaciones':datos[5], 'tipoIngreso':datos[6], 'fechaIngreso':datos[7], 'tipoSalida':datos[8], 'fechaSalida':datos[9]}
            return jsonify({'movimiento': movimiento, 'mensaje': 'Movimiento Encontrado.'})
        else:
            return jsonify({'mensaje': 'Movimiento no encontrado'})
    except Exception as ex:
        return jsonify({'mensaje': 'Error!'})

#CREAR
@app.route('/movimiento', methods=['POST'])
def crear_movimiento():
    try:
        cursor = conexion.connection.cursor()
        sql = "INSERT INTO movimiento (id, documentoPersona, serialEquipo, centroFormacion, documentoVigilante, observaciones, tipoIngreso, fechaIngreso, tipoSalida, fechaSalida) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}', '{8}', '{9}')""".format(request.json['id'], request.json['documentoPersona'], request.json['serialEquipo'], request.json['centroFormacion'], request.json['documentoVigilante'], request.json['observaciones'], request.json['tipoIngreso'], request.json['fechaIngreso'], request.json['tipoSalida'], request.json['fechaSalida'])
        cursor.execute(sql)
        conexion.connection.commit() #confirma la accion de creación
        return jsonify({'mensaje': 'Movimiento creado.'})
    except Exception as ex:
        return jsonify({'mensaje': 'Error!'})
    
#ELIMINAR
@app.route('/movimiento/<id>', methods=['DELETE'])
def eliminar_movimiento(id):
    try:
        cursor = conexion.connection.cursor()
        sql = "DELETE FROM movimiento WHERE id = '{0}'".format(id)
        cursor.execute(sql)
        conexion.connection.commit() #confirma la accion de creación
        return jsonify({'mensaje': 'Movimiento eliminado.'})
    except Exception as ex:
        return jsonify({'mensaje': 'Error!'})

#ACTUALIZAR
@app.route('/movimiento/<id>', methods=['PUT'])
def editar_movimiento(id):
    try:
        cursor = conexion.connection.cursor()
        sql = """UPDATE movimiento SET documentoPersona = '{0}', serialEquipo = '{1}', centroFormacion = '{2}', documentoVigilante = '{3}', observaciones = '{4}', tipoIngreso = '{5}',  fechaIngreso = '{6}', tipoSalida = '{7}', fechaSalida = '{8}' WHERE id = '{9}'""".format(request.json['documentoPersona'], request.json['serialEquipo'], request.json['centroFormacion'], request.json['documentoVigilante'], request.json['observaciones'], request.json['tipoIngreso'], request.json['fechaIngreso'], request.json['tipoSalida'], request.json['fechaSalida'], id)
        cursor.execute(sql)
        conexion.connection.commit()
        return jsonify({'mensaje': 'Movimiento actualizado correctamente.'})
    except Exception as ex:
        return jsonify({'mensaje': 'Error al actualizar movimiento'}), 500
    
#----------------------------------------------------------------------------------------------------------------------------------------------------------------
# LOGIN
@app.route('/login', methods=['POST'])
def login():
    try:
        # Obtener credenciales del request
        correo = request.json.get('correo')
        contrasena = request.json.get('contrasena')

        if not correo or not contrasena:
            return jsonify({'success': False, 'message': 'Correo y contraseña son requeridos'}), 400

        cursor = conexion.connection.cursor()
        sql = "SELECT documento, nombre, apellido, rol, estado FROM usuario WHERE correo = %s AND contrasena = %s"
        cursor.execute(sql, (correo, contrasena))
        usuario = cursor.fetchone()

        if usuario:
            # Verificar si el usuario está activo
            if usuario[4] == 0:  # Asumiendo que estado 0 es inactivo
                return jsonify({'success': False, 'message': 'Usuario inactivo'}), 403
            
            # Construir respuesta
            usuario_data = {
                'documento': usuario[0],
                'nombre': usuario[1],
                'apellido': usuario[2],
                'rol': usuario[3],
                'correo': correo
            }
            return jsonify({'success': True, 'usuario': usuario_data, 'message': 'Login exitoso'})
        else:
            return jsonify({'success': False, 'message': 'Credenciales incorrectas'}), 401

    except Exception as ex:
        return jsonify({'success': False, 'message': 'Error en el servidor'}), 500
    
#----------------------------------------------------------------------------------------------------------------------------------------------------------------

@app.route('/update-password', methods=['POST'])
def update_password():
    try:
        data = request.get_json()
        correo = data['correo']
        nueva_contrasena = data['nuevaContrasena']

        cursor = conexion.connection.cursor()
        sql = "UPDATE usuario SET contrasena = %s WHERE correo = %s"
        cursor.execute(sql, (nueva_contrasena, correo))
        conexion.connection.commit()

        return jsonify({'success': True, 'message': 'Contraseña actualizada correctamente'})
    except Exception as ex:
        return jsonify({'success': False, 'message': 'Error al actualizar contraseña'}), 500
    
def pagina_no_encontrada(error):
    return "<h1>La pagina que intentas buscar no existe</h1>", 404

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(404, pagina_no_encontrada)
    app.run()