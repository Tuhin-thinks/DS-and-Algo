#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(){
    int size;
    printf("Enter size of the diamond:");
    scanf("%d", &size);

    int max_cols=size*2, max_rows=2*size;
    int start, end;

    start =( max_cols/2)-1;
    end = (max_cols/2)+1;
    int increment_factor = 1;
    int star_count = 0;

    for(int i=0; i < max_rows; i++){
        
        
        for(int j=0; j < max_cols; j++){
            if (j > start && j < end){
                printf("*");
                star_count ++;
            }
            else
                printf(" ");
        }

        if (i >= max_rows/2-1){
            increment_factor = -1; // reverse the change
        }

        start -= increment_factor;
        end += increment_factor;
        printf("\n");
    }
    printf("(%d) stars.\n", star_count);
    return 0;
}