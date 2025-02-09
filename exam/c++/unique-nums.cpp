#include <iostream>
#include <cmath>
#include <unordered_set>
int main(){
    int n; 
    int quantity=0;
    std::cin>>n;
    for(int i = 0; i<pow(10, n); ++i){
        std::string str = std::to_string(i);
        std::unordered_set<char> my_set;
        bool flag = false;
        for(char c: str){
            if(my_set.count(c)==0){
                my_set.insert(c);
            }
            else{
                flag=true;
                break;
            }    
        }
        if(!flag){
            ++quantity;
        }
    }

    std::cout<<"Quantity for unique numbers from 0 to 10^n is "<<quantity<<std::endl;
    return 0;
}