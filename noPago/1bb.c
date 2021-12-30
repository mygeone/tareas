#include <stdio.h>
#include <stdlib.h>

#define N 9


void mediana(long v[],int n, int opcion){
    float medianaValor = 0;

    if(opcion == 1){
        goto ordenar;
    }

    ordenar: ;
        // declaramos variables a utilizar
        int i=0;
        int j=0;
        int temp=0;

    start: ;
        for(j=0 ; j<N-1 ; j++)
        {
            if(v[j]>v[j+1])
            {
                temp        = v[j];
                v[j]    = v[j+1];
                v[j+1]  = temp;
            }
        }
        i++;
        if(i<=N){
            goto start;
        }
    

        printf("\nEl arreglo ordenado es: \n");
        for(i=0 ; i<N ; i++)
        {
            printf("\nV[%d] : %ld",i,v[i]);
        }


    media: ;
        float valorMedio=0;
        if(N%2 == 0)
            medianaValor = (v[(N-1)/2] + v[N/2])/2.0;
        else
            medianaValor = v[N/2];

        printf("\n La mediana del arreglo es : %f\n",medianaValor);

    }
int main()
{
    // declaramos variables a utilizar
    long v[N] = {10,2,40,1,57,67,7,98,99};
 
    int i=0;
    
    mediana(v,N,1);

    return 0;
}
