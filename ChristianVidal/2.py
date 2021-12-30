opcion = int(input('Ingrese una opcion \n'))

estudiante = {
'Nombre': 'Juan',
'Matem?ticas': 90,
'Programaci?n': 100,
'Ingl?s': 75,
'Econom?a': 70,
'Carrera':'Instrumentaci?n y automatizaci?n',
'Semestre': 'Segundo',
'A?o': '2020'
}


if(opcion == 1):
    print("Ingrese clave a modificar \n")
    llave = input()
    if llave in estudiante.keys():
        valor = str(input("Ingrese nuevo valor \n"))
        estudiante[llave] = valor
    else:
        print("La llave no existe")

elif(opcion == 2):
    print("Ingrese clave a visualizar")
    llave = str(input())
    if llave in estudiante.keys():
        print(estudiante[llave])
    else:
        print("La llave no existe")

elif(opcion == 3):
    print(estudiante)

elif(opcion == 4):
    print("Ingrese clave a eliminar")
    llave = str(input())
    if llave in estudiante.keys():
        estudiante.pop(llave,None)
        print("Clave",llave, "eliminada")
    else:
        print("La llave no existe")

elif(opcion == 5):
    print("Ingrese clave a insertar")
    llave = str(input())
    print("Ingrese valr a insertar")
    valor = str(input())
    estudiante[llave] = valor

else:
    print("opcion ingresada no valida")

        
        
        
        