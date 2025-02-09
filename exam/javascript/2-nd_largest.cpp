#include <iostream>
int main(){
    int n = 6;
    int arr[n] = {69,321,-96,23,78,19};
    int first_max = arr[0];
    int second_max = arr[0];
    for (int i = 1; i<n; ++i){
        if(arr[i]>first_max){
            first_max = arr[i];
        }
        else if(arr[i]>second_max){
            second_max = arr[i];
        }
    }

    std::cout<<second_max<<std::endl;
    return 0;

}