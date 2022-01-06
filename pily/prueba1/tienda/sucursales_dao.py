from conn import Conexion
from sucursales import Sucursales
from beautifultable import BeautifulTable

class SucursalesDAO:
    def __init__(self) -> None:
        pass

    def buscarSucursal(self,id_sucursal)->Sucursales:
        Conexion.cursor.execute("select * from SUCURSALES where ID_SUCURSAL=:1",[id_sucursal])
        row = Conexion.cursor.fetchone()
        if row is None:
            return None
        else:
            return Sucursales(row[0], row[1], row[2],row[3],row[4],row[5])


    def actualizarSucursal(self,sucursal)->str:
        if self.buscarSucursal(sucursal.id_sucursal) != None:
            Conexion.cursor.execute("update SUCURSALES set nombre=:1, direccion=:2, telefono=:3, email=:4, id_comuna=:5 where ID_SUCURSAL =:6",
            [sucursal.nombre,sucursal.direccion,sucursal.telefono,sucursal.email,sucursal.id_comuna,sucursal.id_sucursal])
            Conexion.connection.commit()
            return 'Sucursal actualizada correctamente!'
        else:
            return 'Sucursal no existe'

    def insertarSucursal(self,sucursal)->str:
        if self.buscarSucursal(sucursal.id_sucursal) is None:
            Conexion.cursor.execute("insert into SUCURSALES (ID_SUCURSAL,NOMBRE,DIRECCION,TELEFONO,EMAIL,ID_COMUNA) values(:1,:2,:3,:4,:5,:6)",[sucursal.id_sucursal,sucursal.nombre,sucursal.direccion,sucursal.telefono,sucursal.email,sucursal.id_comuna])
            Conexion.connection.commit()
            return 'Sucursal ingresada correctamente!'
        else:
            return 'Sucursal ya existe!'

    def obtenerSucursales(self)->None:
        tabla = BeautifulTable()
        tabla.columns.header = ['ID Sucursal','Nombre','Direccion','Telefono','Email','ID Comuna']
        for row in Conexion.cursor.execute('select * from SUCURSALES order by 1'):
            tabla.rows.append(row)
        if len(tabla.rows)>0:
            print(tabla)
        else:
            print('No existe sucursales ingresadas')