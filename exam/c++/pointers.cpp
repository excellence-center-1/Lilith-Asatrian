#include <iostream>
using namespace std;
int main(){
    int x = 10;

    // int* ptr = &x; //*ptr = x-ի պարունակությունը
    // int** ptr2 = &ptr; //*ptr2 = x-ի հասցեն
    // int* ptr3 = *ptr2;

    // std::cout<<"Address of x "<<ptr<<std::endl;
    // std::cout<<"Address of x "<<&x<<std::endl;
    // std::cout<<"x value through ptr "<<*ptr<<std::endl;
    // std::cout<<"Address of ptr "<<&ptr<<std::endl;
    // std::cout<<"Address of x through *ptr2 "<<*ptr2<<std::endl;
    // std::cout<<"Address of x through *ptr3 "<<ptr3<<std::endl;
    // std::cout<<ptr2<<std::endl;

    int arr[5] = {1,2,6,8, 9};
    int *ptr = arr;
    for(int i = 0; i<5; ++i){
        cout<<"Address: "<<ptr<<endl;
        cout<<"Value: "<<*ptr<<endl;
        ++ptr;
    }
    return 0;
}