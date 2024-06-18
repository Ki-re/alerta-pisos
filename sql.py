import mysql.connector
from mysql.connector import Error
import config

def db_connect():
    try:
        global connection
        connection = mysql.connector.connect( # Configuración de la conexión con la base de datos
            host=config.host_mysql,
            database=config.nombreDB,
            user=config.user_sql,
            password=config.pass_sql)
    except Error as error:
        print("Se ha roto")
        print("Error while connecting to MySQL", error)
    else:
        print("Conexión DB Realizada Correctamente")
        
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version", db_Info)
            global cursor
            cursor = connection.cursor()

def db_insert(web, nombre, link): 
        try:
            linea = f"insert into pisos (web, nombre, enlace) VALUES (%s, %s, %s)"
            val = (web, nombre, link)
            cursor.execute(linea, val)
            connection.commit()
        except Error as err:
            if err.errno == 1062: # Error de primary key
                print("Primary key ya en la DB")
                input() # To-do
            else:
                print("Error al introducir los datos en la DB")
                print(f"\nError:{err.errno}")
                print(f"\nError:{err.msg}")
                print(f"\nError:{err.args}")
                input() # Pausa
        else:
            print("Datos Insertados Correctamente")

def db_disconnect():
    cursor.close()
    connection.close()
    print("Conexión DB Cerrada Existosamente")

def busqueda(nombre): # Se debe realizar la llamada de la función especificando de que tabla se quieren obtener los datos
    comando = f"select nombre from pisos where nombre = '{nombre}'"
    cursor.execute(comando)
    return cursor.fetchall()
