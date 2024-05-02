#include <iostream>
const int n = 5;
void selectionSort(int * arr, int size){
    for(int i = 0; i<size; ++i){
        int minimum=arr[i];
        int min_index=i;
        for(int j=i+1; j<size; ++j){
            if(minimum>arr[j]){
                minimum=arr[j];
                min_index=j;
                
            }
        }
        if(min_index!=i){
            std::swap(arr[i], arr[min_index]);
        }
        
    }
}
int main(){
    int arr[n];
    for(int i =0; i<n; ++i){
        std::cout<<"arr["<<i<<"]=";
        std::cin>>arr[i];
    }
    selectionSort(arr, n);
    std::cout<<"sorted array"<<std::endl;
    for(int i =0; i<n; ++i){
        std::cout<<arr[i]<<" ";
    }
    std::cout<<std::endl;

    return 0;
}