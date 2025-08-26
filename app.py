from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
from flask_cors import CORS 
from config import config
import random
import string
from datetime import datetime, timedelta

app = Flask(__name__)

# Diccionario temporal para almacenar códigos de verificación
verification_codes = {}

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
        sql = """INSERT INTO movimiento 
                 (documentoPersona, serialEquipo, centroFormacion, tipoIngreso, fechaIngreso, tipoSalida, fechaSalida) 
                 VALUES (%s, %s, %s, %s, %s, %s, %s)"""
        valores = (
            request.json['documentoPersona'],
            request.json['serialEquipo'],
            request.json['centroFormacion'],
            request.json['tipoIngreso'],
            request.json['fechaIngreso'],
            request.json.get('tipoSalida', ''),
            request.json.get('fechaSalida', '')
        )
        cursor.execute(sql, valores)
        conexion.connection.commit()
        return jsonify({'mensaje': 'Movimiento creado.'})
    except Exception as ex:
        return jsonify({'mensaje': f'Error: {str(ex)}'}), 500
    
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
@app.route('/movimiento/<int:id>', methods=['PUT'])
def actualizar_movimiento(id):
    try:
        cursor = conexion.connection.cursor()
        
        # Verificar si el movimiento existe
        cursor.execute("SELECT id FROM movimiento WHERE id = %s", (id,))
        if not cursor.fetchone():
            return jsonify({'mensaje': 'Movimiento no encontrado'}), 404
        
        data = request.json
        
        # Construir la consulta dinámicamente
        update_fields = []
        values = []
        
        if 'tipoSalida' in data:
            update_fields.append("tipoSalida = %s")
            values.append(data['tipoSalida'])
        
        if 'fechaSalida' in data:
            update_fields.append("fechaSalida = %s")
            values.append(data['fechaSalida'])
        
        if not update_fields:
            return jsonify({'mensaje': 'Nada que actualizar'}), 400
        
        values.append(id)  # Para el WHERE
        
        sql = f"UPDATE movimiento SET {', '.join(update_fields)} WHERE id = %s"
        cursor.execute(sql, values)
        conexion.connection.commit()
        
        return jsonify({'mensaje': 'Movimiento actualizado correctamente'})
    except Exception as ex:
        conexion.connection.rollback()
        return jsonify({'mensaje': f'Error al actualizar movimiento: {str(ex)}'}), 500
    
#----------------------------------------------------------------------------------------------------------------------------------------------------------------
# LOGIN
@app.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        correo = data['correo']
        contrasena = data['contrasena']

        cursor = conexion.connection.cursor()
        sql = """SELECT documento, nombre, apellido, rol, estado 
                 FROM usuario 
                 WHERE correo = %s AND contrasena = %s"""
        cursor.execute(sql, (correo, contrasena))
        usuario = cursor.fetchone()

        if not usuario:
            return jsonify({"success": False, "message": "Credenciales inválidas"}), 401
            
        if usuario[4] == 0:  # Si estado es inactivo
            return jsonify({"success": False, "message": "Usuario inactivo"}), 403

        # En lugar de devolver los datos, iniciamos verificación
        # Generar código de 6 dígitos
        code = ''.join(random.choices(string.digits, k=6))
        expiration = datetime.now() + timedelta(minutes=15)

        # Guardar código
        verification_codes[correo] = {
            'code': code,
            'expiration': expiration,
            'attempts': 0,
            'user_data': {  # Guardamos datos del usuario temporalmente
                'documento': usuario[0],
                'nombre': usuario[1],
                'apellido': usuario[2],
                'rol': usuario[3]
            }
        }

        return jsonify({
            "success": True,
            "message": "Código de verificación enviado al correo",
            "email": correo
        })

    except Exception as e:
        app.logger.error(f"Error en login: {str(e)}")
        return jsonify({"success": False, "message": "Error interno"}), 500
    
#----------------------------------------------------------------------------------------------------------------------------------------------------------------

@app.route('/forgot-password', methods=['POST'])
def forgot_password():
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
    
#----------------------------------------------------------------------------------------------------------------------------------------------------------------
# CAMBIO DE CONTRASEÑA
@app.route('/update-password', methods=['POST'])
def update_password():
    try:
        data = request.get_json()
        documento = data['documento']
        contrasena_actual = data['contrasenaActual']
        nueva_contrasena = data['nuevaContrasena']

        cursor = conexion.connection.cursor()
        
        # 1. Verificar contraseña actual
        sql_verificar = """
        SELECT documento FROM usuario 
        WHERE documento = %s AND contrasena = %s
        """
        cursor.execute(sql_verificar, (documento, contrasena_actual))
        usuario = cursor.fetchone()

        if not usuario:
            return jsonify({'success': False, 'message': 'Contraseña actual incorrecta'}), 401

        # 2. Actualizar contraseña
        sql_actualizar = """
        UPDATE usuario SET contrasena = %s 
        WHERE documento = %s
        """
        cursor.execute(sql_actualizar, (nueva_contrasena, documento))
        conexion.connection.commit()

        return jsonify({'success': True, 'message': 'Contraseña actualizada correctamente'})
    except Exception as ex:
        conexion.connection.rollback()
        return jsonify({'success': False, 'message': 'Error al actualizar contraseña'}), 500
    
#----------------------------------------------------------------------------------------------------------------------------------------------------------------

# Obtener estadísticas para el dashboard
@app.route('/dashboard/estadisticas', methods=['GET'])
def obtener_estadisticas_dashboard():
    try:
        cursor = conexion.connection.cursor()
        
        # 1. Total de ingresos (movimientos de entrada)
        sql_ingresos = "SELECT COUNT(*) FROM movimiento WHERE tipoIngreso IS NOT NULL"
        cursor.execute(sql_ingresos)
        total_ingresos = cursor.fetchone()[0]
        
        # 2. Porcentaje de marcas de equipos
        sql_marcas = """
        SELECT marca, COUNT(*) as cantidad 
        FROM equipos 
        GROUP BY marca 
        ORDER BY cantidad DESC
        """
        cursor.execute(sql_marcas)
        marcas_data = cursor.fetchall()
        total_equipos = sum([marca[1] for marca in marcas_data])
        porcentaje_marcas = [{'marca': marca[0], 'porcentaje': (marca[1]/total_equipos)*100} for marca in marcas_data]
        
        # 3. Porcentaje de ingresos por tipo
        sql_tipos_ingreso = """
        SELECT tipoIngreso, COUNT(*) as cantidad 
        FROM movimiento 
        WHERE tipoIngreso IS NOT NULL
        GROUP BY tipoIngreso
        """
        cursor.execute(sql_tipos_ingreso)
        tipos_ingreso_data = cursor.fetchall()
        porcentaje_ingresos = [{'tipo': tipo[0], 'porcentaje': (tipo[1]/total_ingresos)*100} for tipo in tipos_ingreso_data]
        
        # 4. Datos históricos (ejemplo - debes adaptarlo a tu estructura real)
        sql_historico = """
        SELECT 
            DATE_FORMAT(fechaIngreso, '%b') as mes, 
            COUNT(*) as ingresos
        FROM movimiento
        WHERE fechaIngreso >= DATE_SUB(NOW(), INTERVAL 6 MONTH)
        GROUP BY mes
        ORDER BY fechaIngreso
        """
        cursor.execute(sql_historico)
        historico_data = cursor.fetchall()
        historico_ingresos = [{'mes': mes[0], 'ingresos': mes[1]} for mes in historico_data]
        
        return jsonify({
            'total_ingresos': total_ingresos,
            'porcentaje_marcas': porcentaje_marcas,
            'porcentaje_ingresos': porcentaje_ingresos,
            'historico_ingresos': historico_ingresos,
            'mensaje': 'Datos del dashboard obtenidos'
        })
        
    except Exception as ex:
        return jsonify({'mensaje': 'Error al obtener datos del dashboard'}), 500
    
#----------------------------------------------------------------------------------------------------------------------------------------------------------------

@app.route('/send-verification', methods=['POST'])
def send_verification():
    try:
        data = request.get_json()
        email = data['email']

        # Verificar si el usuario existe en la base de datos
        cursor = conexion.connection.cursor()
        sql = "SELECT documento FROM usuario WHERE correo = %s"
        cursor.execute(sql, (email,))
        user = cursor.fetchone()

        if not user:
            return jsonify({'success': False, 'message': 'Correo no registrado'}), 404

        # Generar código de 6 dígitos
        code = ''.join(random.choices(string.digits, k=6))
        expiration = datetime.now() + timedelta(minutes=15)

        # Guardar código en el diccionario
        verification_codes[email] = {
            'code': code,
            'expiration': expiration,
            'attempts': 0,
            'user_data': {  # Almacenamos datos del usuario temporalmente
                'documento': user[0]
            }
        }

        # En desarrollo: Mostrar el código en consola
        print(f"\n--- Código de verificación para {email} ---")
        print(f"Código: {code}")
        print(f"Expira: {expiration.strftime('%Y-%m-%d %H:%M:%S')}")
        print("----------------------------------------\n")

        return jsonify({
            'success': True,
            'message': 'Código generado (ver consola del servidor)',
            'code': code,  # Solo para desarrollo, quitar en producción
            'email': email
        })

    except Exception as ex:
        return jsonify({'success': False, 'message': str(ex)}), 500

@app.route('/verify-code', methods=['POST'])
def verify_code():
    try:
        data = request.get_json()
        if not data:
            return jsonify({'success': False, 'message': 'Datos no proporcionados'}), 400
            
        email = data.get('email')
        code = data.get('code')
        
        if not email or not code:
            return jsonify({'success': False, 'message': 'Email y código requeridos'}), 400

        # Verificar si hay un código para este email
        if email not in verification_codes:
            return jsonify({'success': False, 'message': 'Código no encontrado o expirado'}), 404

        stored_code = verification_codes[email]

        # Verificar intentos (máximo 3)
        if stored_code['attempts'] >= 3:
            del verification_codes[email]
            return jsonify({'success': False, 'message': 'Demasiados intentos fallidos'}), 403

        # Verificar expiración
        if datetime.now() > stored_code['expiration']:
            del verification_codes[email]
            return jsonify({'success': False, 'message': 'Código expirado'}), 410

        # Verificar código
        if code == stored_code['code']:
            # Código correcto - obtener datos completos del usuario
            cursor = conexion.connection.cursor()
            sql = """SELECT documento, nombre, apellido, rol 
                     FROM usuario WHERE correo = %s"""
            cursor.execute(sql, (email,))
            user_data = cursor.fetchone()
            
            user = {
                'documento': user_data[0],
                'nombre': user_data[1],
                'apellido': user_data[2],
                'rol': user_data[3]
            }
            
            # Eliminar código verificado
            del verification_codes[email]
            
            return jsonify({
            'success': True,
            'message': 'Verificación exitosa',
            'user': {
                'documento': user_data[0],
                'nombre': user_data[1],
                'apellido': user_data[2],
                'rol': user_data[3]
            }
        })
        else:
            # Código incorrecto - incrementar intentos
            verification_codes[email]['attempts'] += 1
            remaining_attempts = 3 - verification_codes[email]['attempts']
            return jsonify({
                'success': False,
                'message': f'Código incorrecto. Te quedan {remaining_attempts} intentos.'
            }), 401

    except Exception as ex:
        return jsonify({'success': False, 'message': str(ex)}), 500

@app.route('/resend-code', methods=['POST'])
def resend_code():
    try:
        data = request.get_json()
        email = data['email']

        # Verificar si el usuario existe
        cursor = conexion.connection.cursor()
        sql = "SELECT documento FROM usuario WHERE correo = %s"
        cursor.execute(sql, (email,))
        user = cursor.fetchone()

        if not user:
            return jsonify({'success': False, 'message': 'Correo no registrado'}), 404

        # Generar nuevo código
        new_code = ''.join(random.choices(string.digits, k=6))
        expiration = datetime.now() + timedelta(minutes=15)

        # Actualizar o crear nueva entrada
        verification_codes[email] = {
            'code': new_code,
            'expiration': expiration,
            'attempts': 0,
            'user_data': {
                'documento': user[0]
            }
        }

        # En desarrollo: Mostrar el nuevo código en consola
        print(f"\n--- Nuevo código de verificación para {email} ---")
        print(f"Código: {new_code}")
        print(f"Expira: {expiration.strftime('%Y-%m-%d %H:%M:%S')}")
        print("----------------------------------------\n")

        return jsonify({
            'success': True,
            'message': 'Nuevo código generado (ver consola del servidor)',
            'code': new_code  # Solo para desarrollo, quitar en producción
        })

    except Exception as ex:
        return jsonify({'success': False, 'message': str(ex)}), 500
    
def pagina_no_encontrada(error):
    return "<h1>La pagina que intentas buscar no existe</h1>", 404

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(404, pagina_no_encontrada)
    app.run()