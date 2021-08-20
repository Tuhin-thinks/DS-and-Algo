#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/* to find the character that is lex. smaller than the character at its right */
int right_side_greater(char **ch, int size){
    printf("array length:%d\n", size);
    for(int i=(size-1); i>=0; i--){
        printf("comparing %s(left) with %s(right)\n", ch[i-1], ch[i]);
        if (strcmp(ch[i], ch[i-1])>0){  // if right character greater than left
            printf("returning at element:%s(%d)\n", ch[i-1], (i-1));
            return (i-1);  // then return left character
        }
    }
    return -1;
}

/* sort array in lexicographic order */
void sort_lexicographically(char **array, int from, int array_size) {
    char *temp;
    for (int i = from;i < array_size; i++){
        for (int j = from; j < array_size - i; j++)
        {
            if (strcmp(array[j], array[j+1]) > 0)
            {
                printf("position %d(%s) swapped with %d(%s)\n", i, array[i], j, array[j]);
                temp = array[j];
                array[j] = array[j+1];
                array[j+1] = temp;
            }
        }
    }
}

/* swap str_cmp with the minimum element greater than str_cmp in the [from, size] range */
void lowest_greater(char **ch, int size, int from, char * str_comp){
    char *min_char, *char_now;
    int min_greater_index= (from+1);
    min_char = ch[from+1];
    for (int i=(from+1); i<size; i++){
        char_now = ch[i];
        printf("\ncomparing %s with %s\n", char_now, str_comp);
        if (strcmp(char_now, str_comp) > 0){
            printf("  -> comparing %s with %s\n", char_now, min_char);
            if (strcmp(min_char, char_now) > 0)
                {
                    printf("  min_char changed to: %s(%d), from %s", char_now, i, min_char);
                    min_greater_index = i;
                    printf("  matching index changed to: %d\n\n", i);
                    min_char = char_now;
                }
        }
    }
    printf("min_char: %s(%d), str_cmp: %s\n", min_char, min_greater_index, str_comp);
    // swap the characters
    char *temp = ch[from];
    ch[from] = min_char;
    ch[min_greater_index] = temp;
}

/* Print elements in the array. */
void printArray(char *array[],int from, int len) {
    for (int i=from; i<len; i++) {
        printf("%s ", array[i]);
    }
    printf("\n");
}

int next_permutation(int n, char **s)
{
	/**
	* Complete this method
	* Return 0 when there is no next permutation and 1 otherwise
	* Modify array s to its next permutation
	*/
}

int main()
{
	// char **s;
	// int n;
	// scanf("%d", &n);
	// s = calloc(n, sizeof(char*));
	// for (int i = 0; i < n; i++)
	// {
	// 	s[i] = calloc(11, sizeof(char));
	// 	scanf("%s", s[i]);
	// }
	// do
	// {
	// 	for (int i = 0; i < n; i++)
	// 		printf("%s%c", s[i], i == n - 1 ? '\n' : ' ');
	// } while (next_permutation(n, s));
	// for (int i = 0; i < n; i++)
	// 	free(s[i]);
	// free(s);
	// return 0;

    int arrlen = 4;
    char* sa[20] = {"2", "1", "4", "3"} ;
    int pos = right_side_greater(sa, arrlen);
    if (pos != -1)
    {
        printf("stopped at element: %s, pos=%d\n", sa[pos], pos);
        printf("right side array: ");
        printArray(sa, pos+1, arrlen);
    }
    else{
        printf("no such instance found\n");
    }

    lowest_greater(sa, arrlen, pos, sa[pos]);
    sort_lexicographically(sa, pos+1, arrlen);
    
    printf("\nFinal array: ");
    printArray(sa, 0, arrlen);

    return 0;
}