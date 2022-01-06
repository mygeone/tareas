from conn import Conexion
from v_totalventasxvendedores import V_totalventasxvendedores
from beautifultable import BeautifulTable

class V_totalventasxvendedoresDAO:
    def __init__(self) -> None:
        pass

    def buscarVentas(self,vendedor)->V_totalventasxvendedores:
        Conexion.cursor.execute('SELECT v_totalventasxvendedores."SUM(MONTO)" AS "monto", v_totalventasxvendedores."NOMBRE", v_totalventasxvendedores."APELLIDOS" FROM v_totalventasxvendedores WHERE v_totalventasxvendedores.nombre=:1',[vendedor])
        row = Conexion.cursor.fetchone()
        if row is None:
            return None
        else:
            return V_totalventasxvendedores(row[0], row[1], row[2])


    def actualizarVentas(self,ventas)->str:
        if self.buscarVentas(ventas.nombre) != None:
            Conexion.cursor.execute("""
            update V_TOTALVENTASXVENDEDORES set sumMonto=:1 apellidos=:2 where nombre:3"""),
            [ventas.sumMonto,ventas.apellidos,ventas.nombre]
            Conexion.connection.commit()
            return 'Ventas actualizada correctamente!'
        else:
            return 'Vendedor no existe'

    def insertarVentas(self,ventas)->str:
        if self.buscarVentas(ventas.nombre) is None:
            Conexion.cursor.execute("insert into V_TOTALVENTASXVENDEDORES values(:1,:2,:3)",[ventas.sumMonto,ventas.nombre,ventas.apellidos])
            Conexion.connection.commit()
            return 'Ventas ingresada correctamente!'
        else:
            return 'Ventas ya existe!'

    def obtenerVentas(self)->None:
        tabla = BeautifulTable()
        tabla.columns.header = ['Suma','Nombre','Apellidos']
        for row in Conexion.cursor.execute('select * from V_TOTALVENTASXVENDEDORES order by 1'):
            tabla.rows.append(row)
        if len(tabla.rows)>0:
            print(tabla)
        else:
            print('No existen ventas')

    def eliminarVentas(self,vendedor)->None:
        if self.buscarVentas(vendedor) != None:
            Conexion.cursor.execute("""
            delete from V_TOTALVENTASXVENDEDORES where nombre:1"""),[vendedor]
            Conexion.connection.commit()
            return 'Ventas eliminada correctamente!'
        else:
            return 'Vendedor no existe'
