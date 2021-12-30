import cx_Oracle
class Conexion:

    def __init__(self):

        #inicializar el wallet
        cx_Oracle.init_oracle_client(lib_dir = r"C:\oraclecloud\ejemplo2PythonDB\instantclient_21_3")
        self.__connection = cx_Oracle.connect(user="ADMIN", password=".Inacap2021.", dsn="db2021ina_high")
        self.__cursor = self.__connection.cursor()

    @property
    def connection(self):
        return self.__connection

    @property
    def cursor(self):
        return self.__cursor
