#include <iostream>
int main(){
    int arr[3][3]={
        {1,3,6},
        {7,8,9}, 
        {6,9,10}
    };
    int sum=0;
    for(int i=0; i<3;++i){
        sum+=arr[i][i];
    }
    std::cout<<sum<<std::endl;
}
    



    

