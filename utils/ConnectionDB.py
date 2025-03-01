import psycopg2

class ConnectionDB:
    @staticmethod
    def get_connection():
        try:
            conn = psycopg2.connect(
                dbname='Dashboard Serial Port',
                user='postgres',
                password='10032004',
                host='localhost',
                port='5432'
            )
            return conn
        except psycopg2.Error as e:
            print(f"Error al conectar a la base de datos: {e}")
            return None
