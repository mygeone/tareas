from conexion import Conexion

class BaseDatos():
    def __init__(self) -> None:
        pass

    def validarExistenciaTabla(self)->bool:
        Conexion.cursor.execute("""
        select * from user_tables where table_name = UPPER('producto')
        UNION
        select * from user_tables where table_name = UPPER('categoria')
        """)
        rows = Conexion.cursor.fetchall()
        if len(rows)>0:
            return True
        else:
            return False   

    def eliminarTablas(self)->str:
        if self.validarExistenciaTabla() == True:
            Conexion.cursor.execute("""
            drop table producto
            """)
            Conexion.cursor.execute("""
            drop table categoria
            """)
            Conexion.connection.commit()
            return 'Tablas eliminadas correctamente!'
        else:
            return 'No se pueden eliminar porque no existen'

    def crearTablas(self)->str:
        if self.validarExistenciaTabla() == False:    
            Conexion.cursor.execute("""
            create table categoria(
                id integer,
                nombre_c varchar2(30),
                descripcion varchar2(100),
                constraint Categoria_PK primary key(id))
            """)
            Conexion.cursor.execute("""
            create table producto(
                codigo varchar2(10),
                nombre varchar2(30),
                precio integer,
                stock integer,
                categoria integer,
                constraint Producto_PK primary key(codigo))
            """)    
            Conexion.cursor.execute("""alter table producto 
                add constraint Categoria_Producto_FK foreign key(categoria)
                references categoria(id) ON DELETE CASCADE
            """)
            Conexion.connection.commit()
            return 'Tablas creadas correctamente!'
        else:
            return 'No se pueden crear porque ya existen'