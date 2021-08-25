/**
 * C hollow star pattern
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(){

    int size, i=0, j;
    printf("Enter the size of the hollow triangle:");
    scanf("%d",&size);

    int first = size-1;
    int last = size-1;
    for(i=0; i<size;i++){
        if (i < size-1){
            for(j=0;j<size*2;j++){  // size x 2 columns
                
                // determine first and last position to draw * at each row
                if (j == first || j == last){
                    printf("*");
                }
                else{
                    printf(" ");
                }
            }
            first -= 1;
            last += 1;
        }
        else{  // base line for the triangle
            for (j=0; j<size*2;j++){
                if (j >= first && j <= last)
                    printf("*");
                else{
                    printf(" ");}
            }
        }
        
        printf("\n");  // new line
    }

    return 0;
}