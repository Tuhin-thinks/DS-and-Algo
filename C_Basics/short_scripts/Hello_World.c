#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(){
    char s[100];

    scanf("%[^\n]%*c", s);  // to take input multiple characters

    printf("Hello, World!\n");
    printf("%s\n", s);
}