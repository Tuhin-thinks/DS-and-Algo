#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main()
{
    int a, b, int_diff, int_sum;
    scanf("%d %d", &a, &b); // accepts 2 integers
	int_diff = a-b;
    int_sum = a+b;
    printf("%d %d\n", int_sum, int_diff);
    
    float x, y, double_diff, double_sum;
    
    scanf("%f %f", &x, &y);  // accepts 2 floating point numbers
    double_diff = x-y;
    double_sum = x+y;
    printf("%0.1f %0.1f\n", double_sum, double_diff);
    
    return 0;
}