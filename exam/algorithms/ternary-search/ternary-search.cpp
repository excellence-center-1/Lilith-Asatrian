#include <iostream>
int ternarySearch(int* arr, int left, int right, int key){
    if(left<=right){
        int mid1=left+(right-left)/3;
        int mid2=right-(right-left)/3;

        if(key==arr[mid1]){
            return mid1;
        }
        if(key==arr[mid2]){
            return mid2;
        }
       if(key<arr[mid1]){
            return ternarySearch(arr, left, mid1-1, key);
        }
        else if(key>arr[mid2]){
            return ternarySearch(arr, mid2+1, right, key);
        }
        else {
            return ternarySearch(arr, mid1+1, mid2-1, key);
        }
    }
    return -1;
}
int main(){
    int A[5]={1,5,6,7,9};
    std::cout<<ternarySearch(A, 0, 4, 7)<<std::endl;
    return 0;
}