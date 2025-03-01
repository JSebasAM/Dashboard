from utils.ConnectionDB import ConnectionDB
def saveData(data, tiempo):
    try:

        conn = ConnectionDB.get_connection()
        cursor = conn.cursor()
        valores = data.split(';')
        fecha = tiempo
        dato1 = float(valores[0])
        dato2 = float(valores[1])
        dato3 = float(valores[2])
        dato4 = float(valores[3])

        query = "INSERT INTO datos (fecha, dato1, dato2, dato3, dato4) VALUES (%s, %s, %s, %s, %s)" 
        cursor.execute(query, (fecha, dato1, dato2, dato3, dato4))

        conn.commit()
        cursor.close()
        conn.close()
        print('Datos insertados correctamente') 
    except Exception as e:
        print(f"Error al guardar los datos: {e}")
    finally:
        if 'conn' in locals():
            conn.close()