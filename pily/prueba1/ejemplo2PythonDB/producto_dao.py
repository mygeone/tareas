from producto import Producto
from conexion import Conexion
from beautifultable import BeautifulTable

class ProductoDao:
    def __init__(self) -> None:
        self.__oracle = Conexion()
    
    @property
    def oracle(self):
        return self.__oracle

    def validarExistenciaTabla(self)->int:
        self.oracle.cursor.execute("select * from dba_tables where table_name = 'producto'")
        row = self.oracle.cursor.fetchone()
        if row!=None:
            return 0
        else:
            return 1

    def eliminarTablaProducto(self)->str:
        self.oracle.cursor.execute("""
        drop table producto
        """)
        self.oracle.connection.commit()
        return 'Tabla eliminada correctamente!'

    def crearTablaProducto(self)->str:
        self.oracle.cursor.execute("""
        create table producto(
            codigo varchar2(10),
            nombre varchar2(30),
            precio integer,
            stock integer,
            constraint Producto_PK primary key(codigo))
        """)
        self.oracle.connection.commit()
        return 'Tabla creada correctamente!'

    def buscarProducto(self,codigo)->Producto:
        self.oracle.cursor.execute("select * from producto where codigo=:1", [codigo])
        row = self.oracle.cursor.fetchone()
        if row is None:
            return None
        else:
            return Producto(row[0], row[1], row[2], row[3])

    def insertarProducto(self, producto)->str:
        if self.buscarProducto(producto.codigo) is None:
            self.oracle.cursor.execute("insert into producto values(:1,:2,:3,:4)", [producto.codigo, producto.nombre, producto.precio, producto.stock])
            self.oracle.connection.commit()
            return 'Producto ingresado correctamente!'
        else:
            return 'Producto ya existe!'

    def actualizarProducto(self, codigo,nombre,precio,stock)->str:
        if self.buscarProducto(codigo) != None:
            self.oracle.cursor.execute("update producto set nombre=:1,precio=:2,stock=:3 where codigo=:4", [nombre,precio,stock,codigo])
            self.oracle.connection.commit()
            return 'Producto actualizado correctamente!'
        else:
            return 'Codigo no existe!'

    def eliminarProducto(self, codigo)->str:
        if self.buscarProducto(codigo) != None:
            self.oracle.cursor.execute("delete from producto where codigo=:1", [codigo])
            self.oracle.connection.commit()
            return 'Producto eliminado correctamente!'
        else:
            return 'Codigo no existe!'

    def obtenerProductos(self)->None:
        tabla = BeautifulTable()
        tabla.columns.header = ['Codigo', 'Nombre', 'Precio', 'Stock']
        for row in self.oracle.cursor.execute('select * from producto'):
            tabla.rows.append(row)
        print(tabla)