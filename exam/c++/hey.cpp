#include <iostream>
using namespace std;
int main(){
    int a = 12;
    char c = 'a';
    int* x = &a;
    cout<<"a value "<<a<<endl;
    cout<<"x value "<<*x<<endl;

    *x=44;

    cout<<"a value "<<a<<endl;
}