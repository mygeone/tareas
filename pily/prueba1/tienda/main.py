from conn import Conexion
from db import DB
from sucursales_dao import SucursalesDAO
from sucursales import Sucursales
from v_totalventasxvendedores import V_totalventasxvendedores
from vendedores import Vendedores
from ventas import Ventas
from v_totalventasxvendedores_dao import V_totalventasxvendedoresDAO
from vendedores_dao import VendedoresDAO
from vendedores_dao import VendedoresDAO
from ventas_dao import VentasDAO
from beautifultable import BeautifulTable
import os
import time

os.system('cls')
Conexion.getConnection()

menu = BeautifulTable()
menu.columns.header = ['========GESTION DE VENTAS========'] 
menu.rows.append(['1. Crear Base de Datos'])
menu.rows.append(['2. Eliminar Base de Datos'])

menu.rows.append(['3. Buscar Sucursal'])
menu.rows.append(['4. Insertar Sucursal'])
menu.rows.append(['5. Actualizar Sucursal'])
menu.rows.append(['6. Listar Sucursales'])

menu.rows.append(['7. Buscar Ventas Totales por Vendedor'])
#menu.rows.append(['8. Insertar Ventas Totales por Vendedor'])
#menu.rows.append(['9. Eliminar Ventas Totales por Vendedor'])
#menu.rows.append(['10. Actualizar Ventas Totales por Vendedor'])
menu.rows.append(['11. Listar Ventas Totales por Vendedor'])

menu.rows.append(['12. Buscar Vendedor'])
menu.rows.append(['13. Insertar Vendedor'])
menu.rows.append(['14. Actualizar Vendedor'])
menu.rows.append(['15. Listar Vendedores'])

menu.rows.append(['16. Buscar Venta'])
menu.rows.append(['17. Insertar Venta'])
menu.rows.append(['18. Eliminar Venta'])
menu.rows.append(['19. Actualizar Venta'])
menu.rows.append(['20. Listar Ventas'])
menu.rows.append(['0. Salir'])
menu.columns.alignment = BeautifulTable.ALIGN_LEFT


def crearT():
    os.system('cls')
    bd = DB()
    print('____CREAR BASE DE DATOS_____')
    print()
    print(bd.crearTablas())
    print()
    time.sleep(3)

def eliminarT():
    os.system('cls')
    bd = DB()
    print('____ELIMINAR BASE DE DATOS_____')
    print()
    print(bd.eliminarTablas())
    print()
    time.sleep(3)




def buscarSucursal():
    os.system('cls')
    sucursalDAO = SucursalesDAO()
    print('____BUSCAR SUCURSAL_____')
    print()
    id=int(input('Indique un id de sucursal a buscar: '))
    c = sucursalDAO.buscarSucursal(id)
    if c!=None:
        print()
        print('Los datos de la sucursal son id: ',c.id_sucursal,' nombre: ',c.nombre,' direccion: ',c.direccion,' email: ',c.email,' id comuna',c.id_comuna)
        print()
    else:
        print('Sucursal no encontrada')
        print()
    time.sleep(5)

def insertarSucursal():
    os.system('cls')
    sucursalDAO = SucursalesDAO()
    print('____INSERTAR SUCURSAL_____')
    print()
    id=int(input('Indique un id de sucursal a ingresar: '))
    nombre = input('Indique el nombre de la sucursal a ingresar:  ').upper()
    direccion = input('Indique la direccion de la sucursal ingresar:  ').upper()
    telefono = int(input('Indique el telefono de la sucursal ingresar:  '))
    email = input('Indique el email de la sucursal ingresar:  ').upper()
    id_comuna =int( input('Indique id comuna de la sucursal ingresar:  '))
    print(sucursalDAO.insertarSucursal(Sucursales(id,nombre,direccion,telefono,email,id_comuna)))
    time.sleep(5)

def actualizarSucursal():
    os.system('cls')
    sucursalDAO = SucursalesDAO()
    print('____ACTUALIZAR SUCURSAL_____')
    print()
    id=int(input('Indique un id de sucursal a actualizar: '))
    nombre = input('Indique el nombre de la sucursal a actualizar:  ').upper()
    direccion = input('Indique la direccion de la sucursal actualizar:  ').upper()
    telefono = int(input('Indique el telefono de la sucursal actualizar:  '))
    email = input('Indique el email de la sucursal actualizar:  ').upper()
    id_comuna =int( input('Indique id comuna de la sucursal actualizar:  '))
    print(sucursalDAO.actualizarSucursal(Sucursales(id,nombre,direccion,telefono,email,id_comuna)))

def obtenerTodasSucursales():
    os.system('cls')
    sucursalDAO = SucursalesDAO()
    print('____LISTA DE SUCURSALES_____')
    print()
    sucursalDAO.obtenerSucursales()
    time.sleep(5)



def buscarTotalVentas():
    os.system('cls')
    ventasxvendedor = V_totalventasxvendedoresDAO()
    print('____BUSCAR VENTAS POR VENDEDOR_____')
    print()
    nombre=input('Indique nombre de vendedor a buscar: ')
    c = ventasxvendedor.buscarVentas(nombre)
    if c!=None:
        print()
        print('Los datos de venta del vendedor son: Monto total: ',c.sumMonto,' nombre: ',c.nombre,' apellidos: ',c.apellidos)
        print()
    else:
        print('Vendedor no encontrado')
        print()
    time.sleep(5)

def insertarTotalVentas():
    os.system('cls')
    ventasxvendedor = V_totalventasxvendedoresDAO()
    print()
    print('____INSERTAR VENTA POR VENDEDOR_____')
    print()
    monto=int(input('Indique un monto a ingresar: '))
    nombre = input('Indique el nombre de la sucursal a ingresar:  ').upper()
    apellido = input('Indique la direccion de la sucursal ingresar:  ').upper()
    print(ventasxvendedor.insertarVentas(V_totalventasxvendedores(monto,nombre,apellido)))
    time.sleep(5)

def obtenerTodasVentasPorVendedor():
    os.system('cls')
    ventasxvendedor = V_totalventasxvendedoresDAO()
    print('____LISTA DE VENTAS POR VENDEDORES_____')
    print()
    ventasxvendedor.obtenerVentas()
    time.sleep(5)

def eliminarVentasPorVendedor():
    os.system('cls')
    ventasxvendedor = V_totalventasxvendedoresDAO()
    print('____ELIMINAR DE VENTAS POR VENTAS_____')
    print()
    nombre=int(input('Indique nombre de vendedor a eliminar: '))
    ventasxvendedor.eliminarVentas(nombre)
    time.sleep(5)

def actualizarVentasTotalesPorVendedor():
    os.system('cls')
    ventasxvendedor = V_totalventasxvendedoresDAO()
    print()
    print('____ACTUALIZAR VENTA POR VENDEDOR_____')
    print()
    monto=int(input('Indique un monto a ingresar: '))
    nombre = input('Indique el nombre de la sucursal a ingresar:  ').upper()
    apellido = input('Indique la direccion de la sucursal ingresar:  ').upper()
    print(ventasxvendedor.actualizarVentas(V_totalventasxvendedores(monto,nombre,apellido)))


def buscarVendedor():
    os.system('cls')
    vendedorDAO = VendedoresDAO()
    print('____BUSCAR VENDEDOR_____')
    print()
    id=int(input('Indique id de vendedor a buscar: '))
    c = vendedorDAO.buscarVendedor(id)
    if c!=None:
        print()
        print('Los datos del vendedor son: ',c.id_vendedor,' nombre: ',c.nombre,' apellidos: ',c.apellidos,' email:',c.email,' id sucursal ',c.id_sucursal)
        print()
    else:
        print('Vendedor no encontrado')
        print()
    time.sleep(5)

def insertarVendedor():
    os.system('cls')
    vendedorDAO = VendedoresDAO()
    print('____INSERTAR VENDEDOR_____')
    print()
    id=int(input('Indique un id de vendedpr a ingresar: '))
    nombre = input('Indique el nombre de vendedor a ingresar:  ').upper()
    apellido = input('Indique apellido de vendedor a ingresar:  ').upper()
    email = input('Indique el email de la sucursal ingresar:  ').upper()
    id_sucursal = int(input('Indique el id_sucursal de vendedor a ingresar:  '))
    print(vendedorDAO.insertarVendedor(Vendedores(id,nombre,apellido,email,id_sucursal)))
    time.sleep(5)

def obtenerTodosVendedores():
    os.system('cls')
    vendedorDAO = VendedoresDAO()
    print('____LISTA DE VENDEDORES_____')
    print()
    vendedorDAO.obtenerVendedores()
    time.sleep(5)

def actualizarVendedor():
    os.system('cls')
    vendedorDAO = VendedoresDAO()
    print('____ACTUALIZAR VENDEDOR_____')
    print()
    id=int(input('Indique un id de vendedpr a ingresar: '))
    nombre = input('Indique el nombre de vendedpr a ingresar:  ').upper()
    apellido = input('Indique apellido de vendedor a ingresar:  ').upper()
    email = input('Indique el email de la sucursal ingresar:  ').upper()
    id_sucursal = int(input('Indique el id_sucursal de vendedor a ingresar:  '))
    print(vendedorDAO.actualizarVendedor(Vendedores(id,nombre,apellido,email,id_sucursal)))
    time.sleep(5)


def buscarVenta():
    os.system('cls')
    ventasDAO = VentasDAO()
    print('____BUSCAR VENTA_____')
    print()
    id=int(input('Indique id de venta a buscar: '))
    c = ventasDAO.buscarVentas(id)
    if c!=None:
        print()
        print('Los datos de la venta son: ',c.id_venta,' monto : ',c.monto,' fecha: ',c.fecha,' id vendedor:',c.id_vendedor)
    else:
        print('Venta no encontrada')
        print()
    time.sleep(5)

def insertarVenta():
    os.system('cls')
    ventasDAO = VentasDAO()
    print('____INSERTAR VENTA_____')
    print()
    id=int(input('Indique un id de venta a ingresar: '))
    monto = int(input('Indique el monto de venta a ingresar:  '))
    fecha = input('Indique fecha de venta a ingresar. Siga formato DATE SQL (dd-mm-aa):  ').upper()
    id_vendedor = int(input('Indique el id_vendedor de venta a ingresar:  '))
    print(ventasDAO.insertarVenta(Ventas(id,monto,fecha,id_vendedor)))
    time.sleep(5)

def obtenerTodasVentas():
    os.system('cls')
    ventasDAO = VentasDAO()
    print('____LISTA DE VENTAS POR VENTAS_____')
    print()
    ventasDAO.obtenerVentas()
    time.sleep(5)

def eliminarVenta():
    os.system('cls')
    ventasDAO = VentasDAO()
    print('____ELIMINAR VENTA_____')
    print()
    id=int(input('Indique un id de venta a eliminar: '))
    print(ventasDAO.eliminarVentas(id))

def actualizarVenta():
    os.system('cls')
    ventasDAO = VentasDAO()
    print('____ACTUALIZAR VENTA_____')
    print()
    id=int(input('Indique un id de venta a actualizar: '))
    monto= int(input('Ingrese monto de venta a actualizar'))
    fecha = input('Ingrese fecha a actualizar. Siga formato DATE SQL')
    id_vendedor = int(input('Ingrese id de vendedor de venta a actualizar'))
    print(ventasDAO.actualizarVentas(Ventas(id,monto,fecha,id_vendedor)))


def salir():
    os.system('cls')
    print()
    print('Adios...')
    time.sleep(2)

def incorrecto():
    os.system('cls')
    print()
    print('Opcion incorrecta, vuelva a intentar...')
    time.sleep(2)

while True:
    os.system('cls')
    print(menu)
    opcion = input('Opcion: ')
    if opcion == '1':
        crearT()
    elif opcion == '2':
        eliminarT()
    elif opcion == '3':
        buscarSucursal()
    elif opcion == '4':
        insertarSucursal()
    elif opcion == '5':
        actualizarSucursal()
    elif opcion == '6':
        obtenerTodasSucursales()
    elif opcion == '7':
        buscarTotalVentas()

    elif opcion == '8':
        insertarTotalVentas()
    elif opcion == '9':
        eliminarVentasPorVendedor()
    elif opcion == '10':
        actualizarVentasTotalesPorVendedor()
    
    elif opcion == '11':
        obtenerTodasVentasPorVendedor()
    elif opcion == '12':
        buscarVendedor()
    elif opcion == '13':
        insertarVendedor()
    elif opcion == '14':
        actualizarVendedor()
    elif opcion == '15':
        obtenerTodosVendedores()
    elif opcion == '16':
        buscarVenta()
    elif opcion == '17':
        insertarVenta()
    elif opcion == '18':
        eliminarVenta()
    elif opcion == '19':
        actualizarVenta()
    elif opcion == '20':
        obtenerTodasVentas()
    elif opcion == '0':
        salir()
    else:
        incorrecto()