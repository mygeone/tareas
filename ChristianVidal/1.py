import numpy as np

cantidadPacientes = int(input('Ingrese la cantidad de pacientes \n'))
tempPromPacientes = []
if(cantidadPacientes < 1 or cantidadPacientes > 10):
    print("Cantidad de pacientes es un numero no valido")
else:
    cantidadTemp = int(input('Ingrese la cantidad de temperaturas \n'))
    if(cantidadTemp < 1 or cantidadTemp > 7):
        print("Numero de temperaturas no valido")
    else:
        for i in range(cantidadPacientes):
            tempArray = list()
            for j in range(cantidadTemp):
                print("Ingrese la temperatura",j+1," del paciente",i+1,"\n")
                temperaturaTemp = int(input())
                if(temperaturaTemp > 30 and temperaturaTemp < 40):
                    tempArray.append(temperaturaTemp)
                else:
                    print("Valor de tempratura no valido. Debe ser menor a 40 grados y mayor a 30 grados")
            tempPromPacientes.append(round(np.mean(tempArray),1))

print("Arreglo de temperaturas de pacientes :")
print(tempPromPacientes)
print("Temperatura maxima almacenada :")
print(np.amax(tempPromPacientes))
