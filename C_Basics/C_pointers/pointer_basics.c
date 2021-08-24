#include <stdio.h>
#include <stdlib.h>

int main()
{
    int *ptr;
    int x;
 
    ptr = &x;
    *ptr = 0;
 
    printf(" x = %dn", x);
    printf(" *ptr = %dn", *ptr);
    printf("\n");
 
    *ptr += 5;
    printf(" x  = %dn", x);
    printf(" *ptr = %dn", *ptr);
    printf("\n");
 
    (*ptr)++;
    printf(" x = %dn", x);
    printf(" *ptr = %dn", *ptr);
    printf("\n");
 
    return 0;
}