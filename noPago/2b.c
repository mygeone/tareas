#include <stdio.h>
#include <stdlib.h>

#define F 3
#define C 3

int main()
{

    long v[F*C] = {10,2,40,1,57,67,7,98,99};

    int i = 0;
    int f = F*C;

    float suma = 0;
    
    start: ;
        if(v[i]%2 == 1){
            suma = suma + v[i];
        };
        i++;
    if(i<=F*C){
        goto start;
    }
    
    printf("\n La suma de los numeros impares es: %f\n",suma);
    return 0;
}

