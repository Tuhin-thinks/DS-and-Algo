/**
 * @file C_box_struct.c
 * @author your name (you@domain.com)
 * @brief program to print volume of boxes that has volume less than MAX_HEIGHT
 * @version 0.1
 * @date 2021-08-20
 * 
 * @copyright Copyright (c) 2021
 * 
 */
#include <stdio.h>
#include <stdlib.h>
#define MAX_HEIGHT 41

struct box
{
	int length, width, height;
};

typedef struct box box;

int get_volume(box b) {
	return (b.length * b.width * b.height);
}

int is_lower_than_max_height(box b) {
	if (b.height < MAX_HEIGHT){
        return 1;
    }
    return 0;
}

int main()
{
	int n;
	scanf("%d", &n);
	box *boxes = malloc(n * sizeof(box));
	for (int i = 0; i < n; i++) {
		scanf("%d%d%d", &boxes[i].length, &boxes[i].width, &boxes[i].height);
	}
	for (int i = 0; i < n; i++) {
		if (is_lower_than_max_height(boxes[i])) {
			printf("%d\n", get_volume(boxes[i]));
		}
	}
	return 0;
}