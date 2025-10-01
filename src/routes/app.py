from flask import Flask, render_template, jsonify, request
from ..database.db import connect_db, mysql
from ..database.controller import consultar


app = Flask(__name__) 

# Se llama a la funcion para conectar la base de datos con la app
connect_db(app)
# Registrar la extensión mysql en el objeto app para acceso en las rutas
app.mysql = mysql

# Primera Prueba de API
@app.route('/api/data', methods=['GET'])
def get_data():
    query = 'SELECT * FROM usuarios'
    users = []
    data = consultar(app, query) # Usar la función consultar para obtener los datos
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


@app.route('/')
def home():
    return render_template('ej1.html')

if __name__ == '__main__':
    app.run(debug=True)