#include <iostream>
#include <chrono>
const int n=5;
void insertion(int *arr, int size){
    for(int i = 1; i<size; ++i){
        for(int j=i; j>0; --j){
            if(arr[j]>arr[j-1]){
                break;
            }
            int temp=arr[j-1];
            arr[j-1]=arr[j];
            arr[j]=temp;
        }

    }
}
int main(){
    int arr[n]={9,5,4,1,3};
    auto t_start = std::chrono::high_resolution_clock::now();   
    insertion(arr, n);
    auto t_end = std::chrono::high_resolution_clock::now();
    double elapsed_time_ms = std::chrono::duration<double, std::milli>(t_end-t_start).count();
    for(int i =0; i<n; ++i){
        std::cout<<arr[i]<<" ";
    }
    std::cout<<std::endl;
    std::cout<<"The elapsed time is "<<elapsed_time_ms<<std::endl;
    return 0;
}


