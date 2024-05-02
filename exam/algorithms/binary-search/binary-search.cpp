#include <iostream>
#include "../quick-sort/quick_sort.h"
int binarySearch(int *arr, int size, int key){

    if(key==arr[size/2]){
        return size/2;
    }
    else if(key<arr[size/2]){
        return binarySearch(arr, size/2, key);
    }
    else {
        
        int result = binarySearch(arr+size/2+1, size-size/2-1, key);
        if(result==-1){
            return -1;
        }
        else {
            return size/2+result+1;
        }
    }
    
}
// int main(){
//     int n;
//     std::cin>>n;
//     std::vector<float> arr(n);
//     for(float &element: arr){
//         std::cout<<"el: ";
//         std::cin>>element;
//     }
//     QuickSort(arr, 0, n-1);

// }
int main(){
    int A[6] ={2,3,4,109,280,290};
    std::cout<<binarySearch(A, 6, 4)<<std::endl;
    return 0;
}