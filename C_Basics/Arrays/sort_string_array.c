#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int lexicographic_sort(const char* a, const char* b) {
    return strcmp(a, b);
}

int lexicographic_sort_reverse(const char* a, const char* b) {
    return strcmp(b, a);
}

int get_distinct_characters_count(const char* a){
    char distinct_characters[26] = {0};
    int distinct_count = 0;
    while (*a != '\0') {
        int chr = (*a++) - 'a';
        if (chr < 26)
            distinct_characters[chr]++;
    }
    
    for (int i = 0; i < 26; i++)
        if (distinct_characters[i])
            distinct_count++;

    return distinct_count;
}

int sort_by_number_of_distinct_characters(const char* a, const char* b) {
    int count_a = get_distinct_characters_count(a);
    int count_b = get_distinct_characters_count(b);
    int res = count_a - count_b;
    return (res) ? (res) : lexicographic_sort(a, b);
}

int sort_by_length(const char* a, const char* b) {
    int len_diff = strlen(a) - strlen(b);
    return len_diff ? len_diff : lexicographic_sort(a, b);

}

void string_sort(char** arr,const int len,int (*cmp_func)(const char* a, const char* b)){
    int sorted = 0;
    int top = len - 1;
    while (!sorted) {
        sorted = 1;
        for (int i = 0; i < top; i++) {
            if (cmp_func(arr[i], arr[i + 1]) > 0) {
                char *tmp = arr[i];
                arr[i] = arr[i + 1];
                arr[i + 1] = tmp;
                sorted = 0;
            }
        }
        top--;
    }
}


int main() 
{
    int n;
    scanf("%d", &n);
  
    char** arr;
	arr = (char**)malloc(n * sizeof(char*));
  
    for(int i = 0; i < n; i++){
        *(arr + i) = malloc(1024 * sizeof(char));
        scanf("%s", *(arr + i));
        *(arr + i) = realloc(*(arr + i), strlen(*(arr + i)) + 1);
    }
  
    string_sort(arr, n, lexicographic_sort);
    for(int i = 0; i < n; i++)
        printf("%s\n", arr[i]);
    printf("\n");

    string_sort(arr, n, lexicographic_sort_reverse);
    for(int i = 0; i < n; i++)
        printf("%s\n", arr[i]); 
    printf("\n");

    string_sort(arr, n, sort_by_length);
    for(int i = 0; i < n; i++)
        printf("%s\n", arr[i]);    
    printf("\n");

    string_sort(arr, n, sort_by_number_of_distinct_characters);
    for(int i = 0; i < n; i++)
        printf("%s\n", arr[i]); 
    printf("\n");
}