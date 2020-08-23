#include <iostream>
using namespace std;

void heapify(int arr[], int n, int i){
    int largest = i;  // initially we consider the largest value to be a position 0
    int left = 2*i+1;
    int right = 2*i+2;


    // if left is greater than root
    if(left<n && arr[left] > arr[largest])
        largest = left;  // update the position of the largest element
    
    // if right is greater than root
    if(right < n && arr[right] > arr[largest])
        largest = right;  // update the position of the largest element
    
    if (largest != i){  // if pos[0] is not the largest node
        swap(arr[i], arr[largest]);  // swap with the last node

        heapify(arr, n, largest);  // heapify again to maintain the max-heap structure
    }
}

void heapsort(int arr[], int n){
    for(int i=n/2-1; i>=0; i--){
        swap(arr[0], arr[i]);  // swap root with last node
        heapify(arr, i, 0);  // heapify to maintain the max-heap structure
    }
}

void printArray(int arr[], int n){  // print the sorted array
    for(int i=0; i<n;++i)
        cout << arr[i] << " ";
    cout << "\n";
}

int main(){
    int arr[] = {12,11,13,5,6,7};
    int n = sizeof(arr) / sizeof(arr[0]);

    heapsort(arr, n);

    cout << "Sorted array is: \n";
    printArray(arr, n);
}