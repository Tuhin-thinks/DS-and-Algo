#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(){

    int size;
    printf("Enter the size of the diamond:");  // width=half-height of the diamond
    scanf("%d", &size);

    int last, mid = size/2;
    for (int i=0; i<2*size;i++){
        for(int j=0; j<i;j++){
            if(j<=i && i <= size){
                printf("*");
            }
            else if(i > size && j<=((2*size)-i-1)){
                printf("*");
            }
        }
        printf("\n");
    }

    return 0;
}