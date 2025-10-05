from flask import Flask, render_template, jsonify, request
from ..database.db import connect_db, mysql
from ..database.controller import execute_query


app = Flask(__name__) 

# Se llama a la funcion para conectar la base de datos con la app
connect_db(app)
# Registrar la extensión mysql en el objeto app para acceso en las rutas
app.mysql = mysql

@app.route('/')
def home():
    return render_template('ej1.html')

# Primera Prueba de API
@app.route('/api/data', methods=['GET'])
def get_data():
    query = 'SELECT * FROM usuarios'
    users = []
    data = execute_query(app, query) # Usar la función consultar para obtener los datos
    for fila in data: # Iterar sobre los resultados y construir la lista de usuarios
        users.append({
            'id': fila[0],
            'cedula': fila[1],
            'rif': fila[2],
            'nombres': fila[3],
            'apellidos': fila[4],
            'telefono': fila[5],
            'email': fila[6],
            'direccion': fila[7],
            'password': fila[8]
        })
    return jsonify({'users': users, 'mensaje': 'Datos obtenidos con éxito'}) # Respuesta JSON con mensaje de éxito
    #return jsonify(users) # Respuesta JSON con los datos sin mensaje
    
#Routa para consultar datos con parametros
@app.route('/api/data/<int:user_id>', methods=['GET'])
def get_data_by_id(user_id):
    query = 'SELECT * FROM usuarios WHERE id = %s'
    params = (user_id,)
    data = execute_query(app, query, params) # Usar la función consultar para obtener los datos
    if data:
        fila = data[0] # Obtener la primera fila del resultado
        user = {
            'id': fila[0],
            'cedula': fila[1],
            'rif': fila[2],
            'nombres': fila[3],
            'apellidos': fila[4],
            'telefono': fila[5],
            'email': fila[6],
            'direccion': fila[7],
            'password': fila[8]
        }
        return jsonify({'user': user, 'mensaje': 'Datos obtenidos con éxito'}) # Respuesta JSON con mensaje de éxito
    else:
        return jsonify({'mensaje': 'Usuario no encontrado'}), 404 # Respuesta JSON si no se encuentra el usuario

if __name__ == '__main__':
    app.run(debug=True)