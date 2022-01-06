import requests #importar la libreria requests
import os
from beautifultable import BeautifulTable
import time

os.system('cls')

try:
    #Validando conexion a Internet
    print("Solicitando informacion de conexion a Internet")
    
    #Ejemplo de prueba de conexion
    #request = requests.get("http://www.google.com",timeout=5)
    #print("Con Conexion :)")
    URL = 'https://random-data-api.com/api/commerce/random_commerce?size=50' #configuramos la URL
    #Solicitamos la informacion y guardamos la respuesta en data
    res = requests.get(URL)
    #Convertimos la respuesta en diccionario
    data = res.json()


except (requests.ConnectionError, requests.Timeout):
    print("Sin conexion :(")

print(data[0])
time.sleep(5)

# Menu
menu = BeautifulTable()

output = BeautifulTable(max_width=200)
output.columns.header = data[0].keys()

menu.columns.header = ['====== MENU CONSULTA DATOS TIENDA COMERCIAL ====='] 
menu.rows.append(['1. Consultar datos por nombre de producto.'])
menu.rows.append(['2. Consultar producto por nombre de departamento.'])
menu.rows.append(['3. Mostrar 50 productos y datos asociados'])
menu.rows.append(['4. Salir'])
menu.columns.alignment = BeautifulTable.ALIGN_LEFT



# Funciones
def salir():
    os.system('cls')
    print()
    print('Adios...')
    time.sleep(2)
    exit()

def incorrecto():
    os.system('cls')
    print()
    print('Opcion incorrecta, vuelva a intentar...')
    time.sleep(1)

def limpiarTabla():
    if len(output.rows) == 0:
        print('tabla vacia')
    else:    
        del output.rows[0:]

def consultarPorNombreProd():
    os.system('cls')
    nombre = input('Ingrese nombre de producto a buscar: ')
    limpiarTabla()
    for producto in data:
        if producto['product_name'] == nombre:
            output.rows.append(list(producto.values()))
            print(output)
            time.sleep(5)

            with open('Productos.txt', 'w') as w:
                w.write(str(output))

            return

    print('Producto no encontrado, intente nuevamente')
    time.sleep(3)

def consultarNombreDepto():
    os.system('cls')
    nombre = input('Ingrese nombre de departamento a buscar: ')
    result = 0
    limpiarTabla()
    for producto in data:
        if producto['department'] == nombre:
            result =+ 1
            output.rows.append(list(producto.values()))
    if (result != 0):
        print(output)
        time.sleep(3)
    else:
        print('Departamento no encontrado, intente nuevamente')
        time.sleep(3)

    with open('Productos.txt', 'w') as w:
        w.write(str(output))

def consultar50():
    for i in range(50):
        output.rows.append(data[i].values())
    print(output)
    time.sleep(5)

    with open('Productos.txt', 'w') as w:
        w.write(str(output))

while True:
    os.system('cls')
    print(menu)
    opcion = input('Opcion: ')
    if opcion == '1':
        consultarPorNombreProd()
    elif opcion == '2':
        consultarNombreDepto()
    elif opcion == '3':
        consultar50()
    elif opcion == '4':
        salir()
    else:
        incorrecto()