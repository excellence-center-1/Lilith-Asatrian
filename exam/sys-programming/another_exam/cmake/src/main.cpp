#include <iostream>
#include "../include/add.h"
#include "../include/subtract.h"

using namespace std;
int main(){
    int operation;
    cin>>operation;
    int operator1;
    int operator2;
    cout<<"Operator1: ";
    cin>>operator1;
    cout<<"Operator2: ";
    cin>>operator2;

    switch (operation)
    {
    case 1:
        cout<<add(operator1, operator2);
        break;
    case 2:
        cout<<subtract(operator1, operator2);
    default:
        break;
    }
    cout<<endl;
    return 0;
}