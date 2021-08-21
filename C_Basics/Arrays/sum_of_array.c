#include <stdio.h>
#include <stdlib.h>

int main(){
    int n;
    scanf("%d", &n);
    int array[n]; // to store input array elements
    for(int i=0; i<n; i++){
        scanf("%d", &array[i]);
    }
    int sum = 0;
    for(int i=0; i<n; i++){
        sum += array[i];
    }
    printf("%d\n", sum);
    
    return 0;
}