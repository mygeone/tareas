import numpy as np

#definimos tablero inicial
inicial = np.zeros((8, 8))


#definimos tablero final
final = np.zeros((8, 8))

print('Ingresa posiciones 1 \n', end = '')
input1 = input()  
print('Ingresa posiciones 2 \n', end = '')
input2 = input()  

pos1 = input1.split(' ')
pos2 = input2.split(' ')

#seteamos posiciones iniciales
inicial[int(pos1[0])][int(pos1[1])] = 1
inicial[int(pos1[2])][int(pos1[3])] = 1
inicial[int(pos1[4])][int(pos1[5])] = 1
inicial[int(pos1[6])][int(pos1[7])] = 1

#seteamos posiciones finales
inicial[int(pos2[0])][int(pos2[1])] = 1
inicial[int(pos2[2])][int(pos2[3])] = 1
inicial[int(pos2[4])][int(pos2[5])] = 1
inicial[int(pos2[6])][int(pos2[7])] = 1
                


flag = True
for i in range(4):
    tempInicial = [pos1[2*i],pos1[2*i+1]]
    tempFinal = [pos2[2*i],pos2[2*i+1]]
    
    #esvecina?
    if(tempInicial[0] - tempFinal[0] == 1 and tempInicial[1] - tempFinal[1] == 1):
        #estaVacia?
        if( inicial[tempFinal[0]][tempFinal[1]] == 1):
            flag = False
            break
    #noEsVecina
    else:
        #hayUnaEntreMedio?
        
        
        