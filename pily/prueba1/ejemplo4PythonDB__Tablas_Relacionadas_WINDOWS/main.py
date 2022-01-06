from conexion import Conexion
from base_datos import BaseDatos
from producto_dao import ProductoDao
from categoria_dao import CategoriaDao
from producto import Producto
from categoria import Categoria
from beautifultable import BeautifulTable
import os
import time

os.system('cls')
Conexion.getConnection()

menu = BeautifulTable()
menu.columns.header = ['========GESTION DE PRODUCTOS Y CATEGORIAS========'] 
menu.rows.append(['1. Crear Base de Datos'])
menu.rows.append(['2. Eliminar Base de Datos'])
menu.rows.append(['3. Buscar Categoria'])
menu.rows.append(['4. Insertar Categoria'])
menu.rows.append(['12. Actualizar Categoria'])
menu.rows.append(['5. Ver categorias'])
menu.rows.append(['6. Buscar Producto'])
menu.rows.append(['7. Insertar Producto'])
menu.rows.append(['8. Eliminar Producto'])
menu.rows.append(['9. Actualizar Producto'])
menu.rows.append(['10. Ver productos'])
menu.rows.append(['11. Salir'])
menu.columns.alignment = BeautifulTable.ALIGN_LEFT

def crearT():
    os.system('cls')
    bd = BaseDatos()
    print('____CREAR BASE DE DATOS_____')
    print()
    print(bd.crearTablas())
    print()
    time.sleep(3)

def eliminarT():
    os.system('cls')
    bd = BaseDatos()
    print('____ELIMINAR BASE DE DATOS_____')
    print()
    print(bd.eliminarTablas())
    print()
    time.sleep(3)

def buscarCat():
    os.system('cls')
    categoriadao = CategoriaDao()
    print('____BUSCAR CATEGORIA_____')
    print()
    id=int(input('Indique un id de categoria a buscar: '))
    c = categoriadao.buscarCategoria(id)
    if c!=None:
        print()
        print('Los datos de la categoria son id: ',c.id,' nombre: ',c.nombre_c,' descripcion: ',c.descripcion)
        print()
    else:
        print('Categoria no encontrada')
        print()
    time.sleep(5)

def insertarCat():
    os.system('cls')
    categoriadao = CategoriaDao()
    print('____NUEVA CATEGORIA_____')
    print()
    id = int(input('Indique el id de categoria: '))
    nombre_c = input('Indique el nombre de la categoria: ').upper()
    descripcion = input('Indique la descripcion de la categoria: ').upper()
    print(categoriadao.insertarCategoria(Categoria(id,nombre_c,descripcion)))
    time.sleep(5)

def obtenerTodasCategorias():
    os.system('cls')
    categoriadao = CategoriaDao()
    print('____LISTA DE CATEGORIAS_____')
    print()
    categoriadao.obtenerCategorias()
    time.sleep(5)

def buscarProd():
    os.system('cls')
    productodao = ProductoDao()
    print('____BUSCAR PRODUCTO_____')
    print()
    codigo=input('Indique un codigo de producto a buscar: ').upper()
    p = productodao.buscarProducto(codigo)
    if p!=None:
        print()
        print('Los datos del producto son codigo: ',p.codigo,' nombre: ',p.nombre,' precio: ',p.precio,
        ' stock: ',p.stock, 'categoria: ', p.categoria)
        print()
    else:
        print('Producto no encontrado')
        print()
    time.sleep(5)

def insertarProd():
    os.system('cls')
    productodao = ProductoDao()
    categoriadao = CategoriaDao()
    print('____NUEVO PRODUCTO_____')
    print()
    codigo = input('Indique el codigo de producto: ').upper()
    nombre = input('Indique el nombre del producto: ').upper()
    precio = int(input('Indique el precio del producto: '))
    stock = int(input('Indique el stock del producto: '))
    categoria = int(input('Indique el id de categoria: '))
    c = categoriadao.buscarCategoria(categoria)
    if c!=None:
        print(productodao.insertarProducto(Producto(codigo,nombre,precio,stock,categoria)))
        print()
    else:
        print('Categoria no encontrada, no se pudo ingresar producto')
        print()
    time.sleep(5)

def eliminarProd():
    os.system('cls')
    productodao = ProductoDao()
    print('____ELIMINAR PRODUCTO_____')
    print()
    codigo=input('Indique codigo de producto a eliminar: ').upper()
    print()
    print(productodao.eliminarProducto(codigo))
    print()
    time.sleep(5)

def editarProd():
    os.system('cls')
    productodao = ProductoDao()
    categoriadao = CategoriaDao()
    print('____EDITAR PRODUCTO_____')
    print()
    codigo=input('Indique un codigo de producto a editar: ').upper()
    p = productodao.buscarProducto(codigo)
    if p!=None:
        print('Los datos del producto son codigo: ',p.codigo,' nombre: ',p.nombre,' precio: ',p.precio,
        ' stock: ',p.stock, ' categoria: ', p.categoria)
        nombre=input('Indique un nombre: ')
        precio=int(input('Indique el nuevo precio: '))
        stock=int(input('Indique el nuevo stock: '))
        categoria = int(input('Indique el id de categoria: '))
        c = categoriadao.buscarCategoria(categoria)
        if c!=None:
            print(productodao.actualizarProducto(Producto(codigo,nombre,precio,stock,categoria)))
            print()
        else:
            print('Categoria no encontrada, no se pudo editar producto')
            print()
    else:
        print('Producto no encontrado')
    time.sleep(5)

def obtenerTodosProductos():
    os.system('cls')
    productodao = ProductoDao()
    print('____LISTA DE PRODUCTOS_____')
    print()
    productodao.obtenerProductos()
    time.sleep(5)

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

def editarCat():
    os.system('cls')
    categoriadao = CategoriaDao()
    print('____EDITAR CATEGORIA_____')
    print()
    id=input('Indique un codigo de categoría a editar: ').upper()
    c = categoriadao.buscarCategoria(id)
    if c!=None:
        print('Los datos de la categoría son id: ',c.id,' nombre: ',c.nombre_c, ' descripción: ',c.descripcion)
        nombre=input('Indique un nombre: ')
        descripcion=input('Indique una descripción: ')
        print(categoriadao.actualizarCategoria(Categoria(id,nombre,descripcion)))        
        print()
    else:
        print('Categoría no encontrada')
    time.sleep(5)

while True:
    os.system('cls')
    print(menu)
    opcion = input('Opcion: ')
    if opcion == '1':
        crearT()
    elif opcion == '2':
        eliminarT()
    elif opcion == '3':
        buscarCat()
    elif opcion == '4':
        insertarCat()
    elif opcion == '5':
        obtenerTodasCategorias()
    elif opcion == '6':
        buscarProd()  
    elif opcion == '7':
        insertarProd()
    elif opcion == '8':
        eliminarProd()
    elif opcion == '9':
        editarProd()
    elif opcion == '10':
        obtenerTodosProductos()
    elif opcion == '12':
        editarCat()
    elif opcion == '11':
        salir()
        break
    else:
        incorrecto()