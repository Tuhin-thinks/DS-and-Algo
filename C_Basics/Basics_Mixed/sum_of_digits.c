#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

/**
 * @brief sum of digits of an entered number
 * 
 * @return int 
 */
int main() {
	
    int n;
    scanf("%d", &n);
    int sum_o_digits = 0;
    while (n) {
        int r = n % 10;
        sum_o_digits += r;
        n /= 10;
    }
    printf("%d", sum_o_digits);
    return 0;
}