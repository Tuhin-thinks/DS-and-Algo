#include <stdio.h>
#include <stdlib.h>

void calculate_the_maximum(int n, int k) {
    int and_now, or_now, xor_now;
    int and_max = 0, or_max = 0, xor_max = 0;
    
    for (int i=1; i<n; i++){
        for (int j=i+1; j<=n; j++) {
            and_now = i & j;
            or_now = i | j;
            xor_now = i ^ j;

            if((and_now > and_max) && (and_now < k)){
                and_max = and_now;
            }
            if((or_now > or_max) && (or_now < k)){
                or_max = or_now;
            }
            if((xor_now > xor_max) && (xor_now < k)){
                xor_max = xor_now;
            }
        }
    }
    printf("%d\n", and_max);
    printf("%d\n", or_max);
    printf("%d\n", xor_max);
}

int main() {
    int n, k;
  
    scanf("%d %d", &n, &k);
    calculate_the_maximum(n, k);
 
    return 0;
}