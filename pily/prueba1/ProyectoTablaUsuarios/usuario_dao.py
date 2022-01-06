from usuario import Usuario
from conexion import Conexion
from beautifultable import BeautifulTable

class UsuarioDao:
    def __init__(self) -> None:
        self.__oracle = Conexion()
    
    @property
    def oracle(self):
        return self.__oracle

    def validarExistenciaTabla(self)->int:
        self.oracle.cursor.execute("select * from dba_tables where table_name = 'USUARIOS130043879'")
        row = self.oracle.cursor.fetchone()
        if row!=None:
            return 1
        else:
            return 0

    def eliminarTablaUsuario(self)->str:
        self.oracle.cursor.execute("""
        drop table USUARIOS130043879
        """)
        self.oracle.connection.commit()
        return 'Tabla eliminada correctamente!'

    def crearTablaUsuario(self)->str:
        self.oracle.cursor.execute("""
        create table USUARIOS130043879(
            id number(38),
            usuario varchar2(30),
            password varchar2(30),
            constraint USUARIOS130043879_PK primary key(id))
        """)
        self.oracle.connection.commit()
        return 'Tabla creada correctamente!'

    def buscarUsuario(self,id)->Usuario:
        self.oracle.cursor.execute("select * from USUARIOS130043879 where id=:1", [id])
        row = self.oracle.cursor.fetchone()
        if row is None:
            return None
        else:
            return Usuario(row[0], row[1], row[2])

    def insertarUsuario(self, usuario)->str:
        if self.buscarUsuario(usuario.id) is None:
            self.oracle.cursor.execute("insert into USUARIOS130043879 values(:1,:2,:3)", [usuario.id, usuario.usuario, usuario.password])
            self.oracle.connection.commit()
            return 'Usuario ingresado correctamente!'
        else:
            return 'Usuario ya existe!'

    def actualizarUsuario(self, id,usuario,password)->str:
        if self.buscarUsuario(id) != None:
            self.oracle.cursor.execute("update USUARIOS130043879 set usuario=:1,password=:2 where id=:3", [usuario,password,id])
            self.oracle.connection.commit()
            return 'Usuario actualizado correctamente!'
        else:
            return 'ID no existe!'

    def eliminarUsuario(self, id)->str:
        if self.buscarUsuario(id) != None:
            self.oracle.cursor.execute("delete from USUARIOS130043879 where id=:1", [id])
            self.oracle.connection.commit()
            return 'Usuario eliminado correctamente!'
        else:
            return 'ID no existe!'

    def obtenerUsuarios(self)->None:
        tabla = BeautifulTable()
        tabla.columns.header = ['ID', 'Usuario', 'Password']
        for row in self.oracle.cursor.execute('select * from USUARIOS130043879'):
            tabla.rows.append(row)
        print(tabla)