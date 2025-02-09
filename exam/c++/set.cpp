#include <iostream>
#include <set>
int main(){
    std::set<int> my_set;
    my_set.insert(5);
    my_set.insert(6);
    my_set.insert(0);
    for(int i: my_set){
        std::cout<<i<<" ";
    }
    std::cout<<std::endl;
    return 0;
}