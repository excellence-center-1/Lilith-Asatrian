#include <iostream>
using namespace std;
int interpolationSearch(int *arr, int low, int high, int item){

    while(low<=high && item>=arr[low] && item<=arr[high]){
        int pos=low+((item-arr[low])*(high-low))/(arr[high]-arr[low]);
        if (arr[pos]==item){
            return pos;
        }
        else if(arr[pos]>item){
            low=pos+1;
        }
        else {
            high=pos-1;
        }
    }
    return -1;
}

int main(){
    int A[5]={1,5,6,7,8};
    std::cout<<interpolationSearch(A, 0, 4, 8)<<std::endl;
    return 0;
}