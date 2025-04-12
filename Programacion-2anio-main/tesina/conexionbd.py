import mysql.connector

def conectar_db():
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",  # PONER SU PROPIO USUARIO
            password="123",  # PONER SU PROPIA CLAVE
            database="base_peluqueria"
        )
        return mydb
    except mysql.connector.Error as err:
        print(f"Error de conexión: {err}")
        return None



def insertar_persona(apellido, nombre, dni, contacto, activo,tipo,id_tipo_p,correo):
    mydb = conectar_db()
    if mydb is None:
        return  # Si no se pudo conectar, salimos

    mycursor = mydb.cursor()
    try:
        
        activo= "Sí" if activo == 1 else "No"
        sql = "INSERT INTO persona (nombre,apellido , dni, contacto,tipo, activo,id_tipo_p,correo) VALUES (%s, %s, %s, %s, %s,%s,%s,%s)"
        val = (apellido, nombre, dni, contacto,tipo,activo,id_tipo_p,correo)
        mycursor.execute(sql, val)
        mydb.commit()
        print("Registro insertado correctamente.")
    except mysql.connector.Error as err:
        print(f"Error al insertar en la base de datos: {err}")
    finally:
        mycursor.close()
        mydb.close()

