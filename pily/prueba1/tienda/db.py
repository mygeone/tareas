from conn import Conexion

class DB():
    def __init__(self) -> None:
        pass


    def validarExistenciaTabla(self)->bool:
        Conexion.cursor.execute("""
        select * from user_tables where table_name = UPPER('sucursales')
        UNION
        select * from user_tables where table_name = UPPER('v_totalventasxvendedores')
        UNION
        select * from user_tables where table_name = UPPER('vendedores')
        UNION
        select * from user_tables where table_name = UPPER('ventas')
        """)
        rows = Conexion.cursor.fetchall()
        if len(rows)>0:
            return True
        else:
            return False   


    def eliminarTablas(self)->str:
        if self.validarExistenciaTabla() == True:
            Conexion.cursor.execute("""
            drop table UPPER('sucursales')
            """)
            Conexion.cursor.execute("""
            drop table UPPER('v_totalventasxvendedores')
            """)
            Conexion.cursor.execute("""
            drop table UPPER('vendedores')
            """)
            Conexion.cursor.execute("""
            drop table UPPER('ventas')
            """)
            Conexion.connection.commit()
            return 'Tablas eliminadas correctamente!'
        else:
            return 'No se pueden eliminar porque no existen'


    def crearTablas(self)->str:
        if self.validarExistenciaTabla() == False:    
            Conexion.cursor.execute("""
            create table sucursales(
                ID_SUCURSAL integer,
                NOMBRE varchar2(15),
                DIRECCION varchar2(40),
                EMAIL varchar2(50),
                ID_COMUNA integer,
                constraint Sucursales_PK primary key(ID_SUCURSAL))
            """)
            Conexion.cursor.execute("""
            create table V_TOTALVENTASXVENDEDORES(
                SUM(MONTO) integer,
                NOMBRE varchar2(15),
                APELLIDOS varchar2(20)
            """)
            Conexion.cursor.execute("""
            create table VENDEDORES(
                ID_VENDEDOR integer,
                NOMBRE varchar2(15),
                APELLIDOS varchar2(20),
                EMAIL varchar2(50),
                ID_SUCURSAL integer,
                constraint VENDEDORES_PK primary key(ID_VENDEDOR))
            """)
            Conexion.cursor.execute("""
            create table VENDEDORES(
                ID_VENTA integer,
                MONTO integer,
                FECHA date,
                ID_VENDEDOR integer,
                constraint VENDEDORES_PK primary key(ID_VENTA))
            """)
            Conexion.connection.commit()
            return 'Tablas creadas correctamente!'
        else:
            return 'No se pueden crear porque ya existen'