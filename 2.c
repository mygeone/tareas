#include <stdio.h>
#include <stdlib.h>

#define F 3
#define C 3


void sumaImpar(long array[],int n){

    // declaramos variables a utilizar
    int i=0;
    int j=0;
    float suma=0;

    for(i=0;i<n;i++){
        if(array[i]%2 == 1){
            suma = suma + array[i];
        }
    }
    printf("\n La suma de los numeros impares es: %f\n",suma);
}

int main()
{
    // declaramos variables a utilizar:
    // v como una matriz de 1d
    long v[F*C] = {10,2,40,1,57,67,7,98,99};

    sumaImpar(v,F*C);
    
    return 0;
}

