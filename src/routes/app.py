from flask import Flask, render_template, jsonify, request
from ..database.db import connect_db, mysql
from ..database.controller import read_user, add_user


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
    data = read_user(app, query) # Usar la función consultar para obtener los datos
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
@app.route('/api/data/<cedula>', methods=['GET'])
def get_data_by_id(cedula):
    query = 'SELECT * FROM usuarios WHERE cedula = %s'
    params = (cedula,)
    data = read_user(app, query, params) # Usar la función consultar para obtener los datos
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
    
#Registrar usuario 
@app.route('/api/data', methods=['POST'])
def api_add_user():
    query = '''
    INSERT INTO usuarios (cedula, rif, nombres, apellidos, telefono, email, direccion, password) 
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    '''
    
    data = request.get_json() 
    print(data)
    # 2. Tupla de Parámetros
    params = (
        data['cedula'], 
        data['rif'], 
        data['nombres'], 
        data['apellidos'], 
        data['telefono'], 
        data['email'], 
        data['direccion'], 
        data['password']
    )
    # 3. Llamada a la función de controlador
    if add_user(app, query, params):
        return jsonify({'mensaje': 'Usuario agregado con éxito'})
    else:
        return jsonify({'mensaje': 'Error al agregar usuario', 'error': 'Revisa el log'}), 500

if __name__ == '__main__':
    app.run(debug=True)