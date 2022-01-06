import cx_Oracle
class Conexion:
    connection = None
    cursor = None

    def __init__(self):
        pass
    
    @classmethod
    def getConnection(cls):
        cx_Oracle.init_oracle_client(lib_dir=r"C:\Users\myge\Documents\instantclient_21_3")
        if cls.connection is None:
            conex = cx_Oracle.connect(user=" admin", password="AlumnoPoo2021", dsn="clases_high")
            cls.cursor = conex.cursor()
            cls.connection = conex