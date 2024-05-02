#include <iostream>
void reverse_array(int * arr, int size){
    for(int i=0; i<size; ++i){
        arr[i]=arr[size-i];
    }
}

void print_array( int* const &arr, int size){
    for(int i = 0; i<size; ++i){
        std::cout<<arr[i]<<" ";
    }
    std::cout<<std::endl;
}
int main(){
    int size;
    std::cin>>size;
    int *arr=new int[size];
    
    reverse_array(arr, size);
    for(int i =0; i<size; ++i){
        std::cout<<arr[i]<<" ";
    }
    std::cout<<std::endl;
    return 0;
}