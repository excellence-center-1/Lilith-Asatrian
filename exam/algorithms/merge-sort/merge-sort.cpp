#include <iostream>
#include <chrono>
void merge(int *arr, int* leftArr, int* rightArr, int leftSize, int rightSize){
    int i=0;
    int j=0;
    int k=0;
    while(j<leftSize && k<rightSize){
        if(leftArr[j]< rightArr[k]){
            arr[i]=leftArr[j];
            ++j;
        }
        else {
            arr[i]=rightArr[k];
            ++k;
        }
        ++i;
    }

    while(j<leftSize){
        arr[i]=leftArr[j];
        ++j;
        ++i;
    }

    while(k<rightSize){
        arr[i]=rightArr[k];
        ++k;
        ++i;
    }
}
void mergeSort(int *arr, int size){
    if(size<=1){
        return;
    }
    int midpoint=size/2;
    int *newArrLeft=new int[midpoint];
    int *newArrRight=new int[midpoint];

    for(int i =0; i<midpoint; ++i){
        newArrLeft[i]=arr[i];
    }

    for(int i =midpoint; i<size; ++i){
        newArrRight[i-midpoint]=arr[i];
    }

    mergeSort(newArrLeft, midpoint);
    mergeSort(newArrRight, size-midpoint);

    merge(arr, newArrLeft, newArrRight, midpoint, size-midpoint);

    delete[] newArrLeft;
    delete[] newArrRight;
}
int main(){
    int size;
    std::cout<<"Size=";
    std::cin>>size;
     
    int *arr=new int[size];
    for(int i = 0; i<size; ++i){
        std::cout<<"arr["<<i<<"]=";
        std::cin>>arr[i];
    }
    auto t_start = std::chrono::high_resolution_clock::now();   
    mergeSort(arr, size);
    auto t_end = std::chrono::high_resolution_clock::now();
    double elapsed_time=std::chrono::duration<double, std::milli>(t_end-t_start).count();
    std::cout<<"Sorted array: "<<std::endl;
    for(int i =0; i<size; ++i){
        std::cout<<arr[i]<<" ";
    }
    std::cout<<std::endl;
    std::cout<<"Elapsed time: "<<elapsed_time<<std::endl;
    return 0;
}