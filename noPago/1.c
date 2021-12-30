#include <stdio.h>
#include <stdlib.h>

#define N 9


// ordenar arreglo
void ordenar(long *array , int n)
{ 
    // declaramos variables a utilizar
    int i=0;
    int j=0;
    int temp=0;

    for(i=0 ; i<n ; i++)
    {
        for(j=0 ; j<n-1 ; j++)
        {
            if(array[j]>array[j+1])
            {
                temp        = array[j];
                array[j]    = array[j+1];
                array[j+1]  = temp;
            }
        }
    }

    printf("\nEl arreglo ordenado es: \n");
    for(i=0 ; i<n ; i++)
    {
        printf("\nV[%d] : %ld",i,array[i]);
    }
}

// funcion para calcular la media
float mediana(long array[],int n)
{
    float valorMedio=0;
    
    if(n%2 == 0)
        valorMedio = (array[(n-1)/2] + array[n/2])/2.0;
    else
        valorMedio = array[n/2];
    return valorMedio;
}

int main()
{
    // declaramos variables a utilizar
    long v[N] = {10,2,40,1,57,67,7,98,99};
    float medianaValor = 0;
    int i=0;

    ordenar(v , N);
    medianaValor = mediana(v,N);
    
    printf("\n La mediana del arreglo es : %f\n",medianaValor);
    return 0;
}