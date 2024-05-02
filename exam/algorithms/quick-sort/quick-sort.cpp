#include <iostream>
#include <vector>
int partition(std::vector<float>& arr, int low, int high){
    int j=low;
    float pivot=arr[high];
    for(int i =low; i<high; ++i){
        if(arr[i]<pivot){
            std::swap(arr[i], arr[j]);
            ++j;
        }
    }
    std::swap(arr[j], arr[high]);
    return j;
}

void QuickSort(std::vector<float>& arr, int low, int high){
    if(low<high){
        int pivot_index=partition(arr, low, high);
        QuickSort(arr, low, pivot_index-1);
        QuickSort(arr, pivot_index+1, high);
    }
}
int main(){
    int size;
    std::cout<<"Input size of array: "; std::cin>>size;
    std::vector<float> arr(size);

    for(int i=0; i<size; ++i){
        std::cout<<"arr["<<i<<"]=";
        std::cin>>arr[i];
    }

    QuickSort(arr, 0,size-1);
    
    for(int i=0; i<size; ++i){
        std::cout<<arr[i]<<" ";
    }
    std::cout<<std::endl;
    return 0;
}