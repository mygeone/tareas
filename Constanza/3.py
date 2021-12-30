def preprocesarMatriz(matriz):
    #Definimos rango M,N
    (filas, columnas) = (len(matriz), len(matriz))
 
    matrizTemp = [[0 for x in range(len(matriz[0]))] for y in range(len(matriz))]
    matrizTemp[0][0] = matriz[0][0]

    for j in range(1, len(matriz[0])):
        matrizTemp[0][j] = matriz[0][j] + matrizTemp[0][j - 1]
 
    for i in range(1, len(matriz)):
        matrizTemp[i][0] = matriz[i][0] + matrizTemp[i - 1][0]
 
    for i in range(1, len(matriz)):
        for j in range(1, len(matriz[0])):
            matrizTemp[i][j] = matriz[i][j] + matrizTemp[i - 1][j] + matrizTemp[i][j - 1] - matrizTemp[i - 1][j - 1]
    return matrizTemp
 
#p,q,r,s son los indices entre los cuales calculamos las sumas
def sumaSubMatrizPorIndices(matriz, p, q, r, s):
 
    matriz = preprocesarMatriz(matriz)
    sumaSubMatriz = matriz[r][s]
    if q - 1 >= 0:
        sumaSubMatriz -= matriz[r][q - 1]
    if p - 1 >= 0:
        sumaSubMatriz -= matriz[p - 1][s]
    if p - 1 >= 0 and q - 1 >= 0:
        sumaSubMatriz += matriz[p - 1][q - 1]
    return sumaSubMatriz
 
 


rangoMatriz = int(input('Ingrese rango N > 1 de la matriz'))

for i in range(rangoMatriz):
    for j in range(rangoMatriz):
        print('Ingrese valor de celda',str(i+1),',',str(j+1))
        matriz[i][j] = int(input())



if(rangoMatriz%2 == 0):
    #par
    matrizSuperiorIzquierda = SI = sumaSubMatrizPorIndices(matriz,0,0,rangoMatriz-2,rangoMatriz-2)
    matrizSuperiorDerecha = SD = sumaSubMatrizPorIndices(matriz,0,1,rangoMatriz-2,rangoMatriz-1)
    matrizInferiorDerecha = ID = sumaSubMatrizPorIndices(matriz,1,1,rangoMatriz-1,rangoMatriz-1)
    matrizInferiorIzquierda = II = sumaSubMatrizPorIndices(matriz,1,0,rangoMatriz-1,rangoMatriz-2)
    
    flag = False
    sumas = [SI,SD,ID,II]
    
    if(2*SD < SI or 2*ID < SI or 2*II < SI):
        print(sumas)
        print("La matriz es cuarto dominante")
    elif(2*SI < SD or 2*ID < SD or 2*II < SD):
        print(sumas)
        print("La matriz es cuarto dominante")
    elif(2*SI < ID or 2*SD < ID or 2*II < ID):
        print(sumas)
        print("La matriz es cuarto dominante")
    elif(2*SI < II or 2*SD < II or 2*ID < II):
        print(sumas)
        print("La matriz es cuarto dominante")
    else:
        print(sumas)
        print("La matriz NO es cuarto dominante")
        
        
else:
    #impar
    eliminar = N//2
    for i in range(rangoMatriz):
        matriz[eliminar-1][i] = 0
        matriz[i][eliminar-1] = 0
        
    matrizSuperiorIzquierda = SI = sumaSubMatrizPorIndices(matriz,0,0,rangoMatriz-2,rangoMatriz-2)
    matrizSuperiorDerecha = SD = sumaSubMatrizPorIndices(matriz,0,1,rangoMatriz-2,rangoMatriz-1)
    matrizInferiorDerecha = ID = sumaSubMatrizPorIndices(matriz,1,1,rangoMatriz-1,rangoMatriz-1)
    matrizInferiorIzquierda = II = sumaSubMatrizPorIndices(matriz,1,0,rangoMatriz-1,rangoMatriz-2)
    
    flag = False
    sumas = [SI,SD,ID,II]
    
    if(2*SD < SI or 2*ID < SI or 2*II < SI):
        print(sumas)
        print("La matriz es cuarto dominante")
    elif(2*SI < SD or 2*ID < SD or 2*II < SD):
        print(sumas)
        print("La matriz es cuarto dominante")
    elif(2*SI < ID or 2*SD < ID or 2*II < ID):
        print(sumas)
        print("La matriz es cuarto dominante")
    elif(2*SI < II or 2*SD < II or 2*ID < II):
        print(sumas)
        print("La matriz es cuarto dominante")
    else:
        print(sumas)
        print("La matriz NO es cuarto dominante")