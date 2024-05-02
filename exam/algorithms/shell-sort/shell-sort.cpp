#include <iostream>
void ShellSort(int * arr, int size){
    for(int gap=size/2; gap>0; gap/=2){
        for(int i=gap; i<size; ++i){
            int j;
            int temp=arr[i];
            for(j=i; j>=gap && arr[j-gap]>temp; j-=gap){
                arr[j]=arr[j-gap];
            }
            arr[j]=temp;
        }
    }
}
