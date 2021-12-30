import cx_Oracle
class Conexion:
    connection = None
    cursor = None

    def __init__(self):
        pass

    
    @classmethod
    def getConnection(cls):
        cx_Oracle.init_oracle_client(lib_dir=r"C:\Users\patri\Documents\ProyectosPython\ejemplo4PythonDB__Tablas_Relacionadas_WINDOWS\instantclient_21_3")
        if cls.connection is None:
            conex = cx_Oracle.connect(user="admin", password="Patriciosilva2021", dsn="nuevabd_high")
            cls.cursor = conex.cursor()
            cls.connection = conex