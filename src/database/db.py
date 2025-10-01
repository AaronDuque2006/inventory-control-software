from flask_mysqldb import MySQL

mysql = MySQL() # crear el objeto mysql

def connect_db(app): #funcion para conectar la base de datos con la app
    # Configuraciones de la base de datos MySQL
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'       
    app.config['MYSQL_PASSWORD'] = ''
    app.config['MYSQL_DB'] = 'inventory_control_db'      
    
    mysql.init_app(app)


