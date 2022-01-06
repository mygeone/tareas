from conn import Conexion
from ventas import Ventas
from beautifultable import BeautifulTable

class VentasDAO:
    def __init__(self) -> None:
        pass

    def buscarVentas(self,venta)->Ventas:
        Conexion.cursor.execute("select * from VENTAS where ID_VENTA=:1",[venta])
        row = Conexion.cursor.fetchone()
        if row is None:
            return None
        else:
            return Ventas(row[0], row[1], row[2],row[3])


    def actualizarVentas(self,ventas)->str:
        if self.buscarVentas(ventas.id_venta) != None:
            Conexion.cursor.execute("update VENTAS set MONTO=:1, FECHA=:2, ID_VENDEDOR=:3 where ID_VENTA =:4",[ventas.monto,ventas.fecha,ventas.id_vendedor,ventas.id_venta])
            Conexion.connection.commit()
            return 'Venta actualizada correctamente!'
        else:
            return 'Venta no existe'

    def insertarVenta(self,ventas)->str:
        if self.buscarVentas(ventas.id_venta) is None:
            Conexion.cursor.execute("insert into VENTAS values(:1,:2,:3,:4)",[ventas.id_venta,ventas.monto,ventas.fecha,ventas.id_vendedor])
            Conexion.connection.commit()
            return 'Venta ingresada correctamente!'
        else:
            return 'Venta ya existe!'

    def obtenerVentas(self)->None:
        tabla = BeautifulTable()
        tabla.columns.header = ['ID Venta','Monto','Fecha','ID Vendedor']
        for row in Conexion.cursor.execute('select * from VENTAS order by 1'):
            tabla.rows.append(row)
        if len(tabla.rows)>0:
            print(tabla)
        else:
            print('No existe ventas ingresadas')

    def eliminarVentas(self,venta)->None:
        if self.buscarVentas(venta) != None:
            Conexion.cursor.execute("delete from VENTAS where ID_VENTA=:1""",[venta])
            Conexion.connection.commit()
            return 'Venta eliminada correctamente!'
        else:
            return 'Venta no existe'
