from categoria import Categoria
from conexion import Conexion
from beautifultable import BeautifulTable

class CategoriaDao:
    def __init__(self) -> None:
        pass

    def buscarCategoria(self,id)->Categoria:
        Conexion.cursor.execute("select * from categoria where id=:1", [id])
        row = Conexion.cursor.fetchone()
        if row is None:
            return None
        else:
            return Categoria(row[0], row[1], row[2])
    
    def actualizarCategoria(self, categoria)->str:
        if self.buscarCategoria(categoria.id) != None:
            Conexion.cursor.execute("""
            update categoria set nombre_c=:1, descripcion=:2 where id=:3
            """, [categoria.nombre_c,categoria.descripcion,categoria.id])
            Conexion.connection.commit()
            return 'Categoría actualizada correctamente!'
        else:
            return 'ID no existe!'

    def insertarCategoria(self, categoria)->str:
        if self.buscarCategoria(categoria.id) is None:
            Conexion.cursor.execute("""
            insert into categoria values(:1,:2,:3)
            """, [categoria.id, categoria.nombre_c, categoria.descripcion])
            Conexion.connection.commit()
            return 'Categoria ingresada correctamente!'
        else:
            return 'Categoria ya existe!'

    def obtenerCategorias(self)->None:
        tabla = BeautifulTable()
        tabla.columns.header = ['Id', 'Nombre', 'Descripcion']
        for row in Conexion.cursor.execute('select * from categoria order by 1'):
            tabla.rows.append(row)
        if len(tabla.rows)>0:
            print(tabla)
        else:
            print('No hay categorias ingresadas')