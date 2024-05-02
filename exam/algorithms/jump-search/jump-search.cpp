#include <iostream>
#include <cmath>
int jumpSearch(int * arr, int size, int item){
    int i=0;
    int gap=sqrt(size);
    while( arr[i]!=item && arr[i]<item ){        
        if(i>size-1){
            return -1;
        }
        i+=gap;

    }
    for(int j=i-gap; j<i; ++j){
        if(arr[j]==item){
            return j;
        }
    }
    return -1;
}


int main(){
    int A[5]={1,5,6,7,9};
    std::cout<<jumpSearch(A, 5, 7)<<std::endl;
    return 0;
}