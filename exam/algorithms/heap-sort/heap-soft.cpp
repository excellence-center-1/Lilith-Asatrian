#include <iostream>
#include <cmath>
void heapify(int* arr, int size, int i){
    int root=i;
    int left_node = 2*i+1;
    int right_node=2*i+2;
    if( left_node<size && arr[left_node]>arr[root]){
        root=left_node;
    } 
    if(right_node<size && arr[right_node]>arr[root]){
        root=right_node;
    }

    if(root!=i){
        std::swap(arr[i], arr[root]);
            heapify(arr, size, root);
    }
}

void HeapSort(int* arr, int size){
    for(int i=size/2-1; i>=0; --i){
        heapify(arr, size, i);
    }

    for(int i=size-1; i>=0; --i){
        std::swap(arr[i], arr[0]);
        heapify(arr, i, 0);
    }
}

int main(){
    int A[5]={2,6,10,19,8};
    HeapSort(A, 5);
    for(int i =0; i<5; ++i){
        std::cout<<A[i]<<" ";
    }
    std::cout<<std::endl;
    return 0;
}
