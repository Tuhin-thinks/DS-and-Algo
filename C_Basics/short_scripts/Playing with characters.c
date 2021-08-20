#include <string.h>
#include <stdio.h>
#include <stdlib.h>

#define MAX_LEN 1000

int main(){

    char ch;
    char sem[MAX_LEN];
    char s[20];
    
    scanf("%c", &ch);
    scanf("%s", s);
    scanf("\n");
    scanf("%[^\n]%*c", sem);

    printf("%c\n", ch);
    printf("%s\n", s);
    printf("%s\n", sem);
    
    return 0;
}