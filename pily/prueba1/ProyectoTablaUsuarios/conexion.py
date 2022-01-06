import cx_Oracle
class Conexion:

    def __init__(self):

        #inicializar el wallet
        cx_Oracle.init_oracle_client(lib_dir = r"C:\Users\patri\Documents\ProyectosPython\ProyectoTablaUsuarios\instantclient_21_3")
        self.__connection = cx_Oracle.connect(user="admin", password="Patriciosilva2021", dsn="nuevabd_high")
        self.__cursor = self.__connection.cursor()

    @property
    def connection(self):
        return self.__connection

    @property
    def cursor(self):
        return self.__cursor
