from producto import Producto
from conexion import Conexion
from beautifultable import BeautifulTable
from categoria_dao import CategoriaDao

class ProductoDao:
    def __init__(self) -> None:
        pass
    
    def buscarProducto(self,codigo)->Producto:
        Conexion.cursor.execute("select * from producto where codigo=:1", [codigo])
        row = Conexion.cursor.fetchone()
        if row is None:
            return None
        else:
            return Producto(row[0], row[1], row[2], row[3], row[4])

    def insertarProducto(self, producto)->str:
        if self.buscarProducto(producto.codigo) is None:
            Conexion.cursor.execute("insert into producto values(:1,:2,:3,:4,:5)", [producto.codigo, producto.nombre, producto.precio, producto.stock, producto.categoria])
            Conexion.connection.commit()
            return 'Producto ingresado correctamente!'
        else:
            return 'Producto ya existe!'

    def actualizarProducto(self, producto)->str:
        if self.buscarProducto(producto.codigo) != None:
            Conexion.cursor.execute("""
            update producto set nombre=:1,precio=:2,stock=:3,categoria=:4 where codigo=:5
            """, [producto.nombre,producto.precio,producto.stock,producto.categoria,producto.codigo])
            Conexion.connection.commit()
            return 'Producto actualizado correctamente!'
        else:
            return 'Codigo no existe!'

    def eliminarProducto(self, codigo)->str:
        if self.buscarProducto(codigo) != None:
            Conexion.cursor.execute("delete from producto where codigo=:1", [codigo])
            Conexion.connection.commit()
            return 'Producto eliminado correctamente!'
        else:
            return 'Codigo no existe!'

    def obtenerProductos(self)->None:
        tabla = BeautifulTable()
        tabla.columns.header = ['Codigo', 'Nombre', 'Precio', 'Stock','Categoria']
        for row in Conexion.cursor.execute("""
            select p.codigo, p.nombre, p.precio, p.stock, c.nombre_c 
            from producto p
            inner join categoria c
            on p.categoria = c.id  
            order by 1
            """):
            tabla.rows.append(row)
        if len(tabla.rows)>0:
            print(tabla)
        else:
            print('No hay productos ingresados')