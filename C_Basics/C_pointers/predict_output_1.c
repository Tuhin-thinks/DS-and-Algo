#include <stdio.h>
#include <stdlib.h>
 
int main()
{
    float arr[5] = {12.5, 10.0, 13.5, 90.5, 0.5};
    float *ptr1 = &arr[0];
    float *ptr2 = ptr1 + 3;
 
    printf("%f ", *ptr2);
    printf("%ld", ptr2 - ptr1);
    printf("\n");
 
   return 0;
}