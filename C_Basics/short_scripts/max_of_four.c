#include <stdio.h>
/*
takes 4 integers and return the max of 4 integers
*/
int max_of_four(int a, int b, int c, int d){
    int x = a>b?a:b;
    int y = c>d?c:d;
    return x>y?x:y;
}

int main() {
    int a, b, c, d;
    scanf("%d %d %d %d", &a, &b, &c, &d);
    int ans = max_of_four(a, b, c, d);
    printf("%d", ans);
    
    return 0;
}