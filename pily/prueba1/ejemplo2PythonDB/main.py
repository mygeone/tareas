from producto_dao import ProductoDao
from producto import Producto
from os import system
system('cls')

producto = ProductoDao()

#Verificar existencia de tabla
opc = producto.validarExistenciaTabla()
if opc==1:
    print(producto.eliminarTablaProducto())
    print()
    print(producto.crearTablaProducto())
    print()
else:
    print(producto.crearTablaProducto())
    print()

#Crear productos
p1 = Producto('P-1', 'Aceite', 1690, 10)
p2 = Producto('P-2', 'Coca Cola 3 lts', 1950, 15)
p3 = Producto('P-3', 'Arroz', 890, 20)
p4 = Producto('P-4', 'Semola', 780, 8)
p5 = Producto('P-5', 'Te Supremo 50 bolsas', 1790, 5)

print(producto.insertarProducto(p1))
print()
print(producto.insertarProducto(p2))
print()
print(producto.insertarProducto(p3))
print()
print(producto.insertarProducto(p4))
print()
print(producto.insertarProducto(p5))
print()

#Buscar producto
codigo=input('Indique un codigo de producto a buscar: ')
codigo = codigo.upper()
p = producto.buscarProducto(codigo)

if p!=None:
    print()
    print('Los datos del producto son codigo: ',p.codigo,' nombre: ',p.nombre,' precio: ',p.precio,
    ' stock: ',p.stock)
    print()
else:
    print('Producto no encontrado')
    print()

#Eliminar producto
codigo=input('Indique un codigo de producto a eliminar: ')
codigo = codigo.upper()
print()
print(producto.eliminarProducto(codigo))
print()

#Editar un producto
codigo=input('Indique un codigo de producto a editar: ')
codigo = codigo.upper()
p = producto.buscarProducto(codigo)
print('Los datos del producto son codigo: ',p.codigo,' nombre: ',p.nombre,' precio: ',p.precio,
    ' stock: ',p.stock)
if p!=None:
    nombre=input('Indique un nombre: ')
    precio=int(input('Indique el nuevo precio: '))
    stock=int(input('Indique el nuevo stock: '))
    print(producto.actualizarProducto(codigo,nombre,precio,stock))
    print()
else:
    print('Producto no encontrado')    

#Mostrar los productos
producto.obtenerProductos()
print()