#include <iostream>
int main(){
    int arr[] = {1,4,5,5,9,10};
    int num;
    std::cout<<"Enter the element you wnat to remove: ";
    std::cin>>num;
    for(int i = 0; i<5; ++i){
        if(arr[i]==num){
            for(int j = i; j<4; ++j){
                arr[j] = arr[j+1];
            }
        }
    }
    int* new_arr = new int[4];
    for(int i = 0; i<4; ++i){
        new_arr[i] = arr[i];
    }

    for(int i = 0; i<4; ++i){
        std::cout<<new_arr[i]<<" ";
    }
    std::cout<<std::endl;

    return 0;
}