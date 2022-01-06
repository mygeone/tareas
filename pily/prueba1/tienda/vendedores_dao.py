from conn import Conexion
from vendedores import Vendedores
from beautifultable import BeautifulTable

class VendedoresDAO:
    def __init__(self) -> None:
        pass

    def buscarVendedor(self,id_vendedor)->Vendedores:
        Conexion.cursor.execute("select * from VENDEDORES where ID_VENDEDOR=:1",[id_vendedor])
        row = Conexion.cursor.fetchone()
        if row is None:
            return None
        else:
            return Vendedores(row[0], row[1], row[2],row[3],row[4])
    
    def actualizarVendedor(self,vendedor)->str:
        if self.buscarVendedor(vendedor.id_vendedor) != None:
            Conexion.cursor.execute("""
            update VENDEDORES set NOMBRE=;1, APELLIDOS=:2, EMAIL=:3, ID_SUCURSAL=:4 where ID_VENDEDORES=:5
            """),[vendedor.nombre,vendedor.apellidos,vendedor.email,vendedor.sucursal,vendedor.id_vendedor]
            return 'Vendedor agregado correctamente'
        else:
            return 'Vendedor no existe'

    def insertarVendedor(self,vendedor)->str:
        if self.buscarVendedor(vendedor.id_vendedor) is None:
            Conexion.cursor.execute("insert into VENDEDORES values(:1,:2,:3,:4,:5)",[vendedor.id_vendedor,vendedor.nombre,vendedor.apellidos,vendedor.email,vendedor.id_sucursal])
            Conexion.connection.commit()
            return 'Vendedor ingresado correctamente!'
        else:
            return 'Vendedor ya existe!'

    def obtenerVendedores(self)->None:
        tabla = BeautifulTable()
        tabla.columns.header = ['ID Vendedor','Nombre','Apellidos','Email','ID Sucursal']
        for row in Conexion.cursor.execute('select * from VENDEDORES order by 1'):
            tabla.rows.append(row)
        if len(tabla.rows)>0:
            print(tabla)
        else:
            print('No existe vendedores ingresados')