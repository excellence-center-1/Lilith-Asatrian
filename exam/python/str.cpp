#include <iostream>
#include <string>
#include <vector>
#include <cmath>
using namespace std;
int main(){
    int n;
    int k;
    int quantity = 0;
    cout<<"k="; cin>>k;
    int temp_k = k;
    int q = 0;
    while (temp_k>0){
        q+=1;
        temp_k/=10;
    }
    cout<<q<<endl;
    n = 6;
    char l_arr[9] = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'};
    char l_ind[9] = {'1','2','3','4','5', '6','7','8','9'};
    vector<int> vect;
    // char *i_arr = new char[n];
    // char *k_arr = new char[m];
    // for(int i = 0; i<n; ++i){
    //     std::cout<<"i_arr["<<i<<"]=";
    //     std::cin>>i_arr[i];
    // }
    char i_arr[n] = {'a', 'b', 'b', 'g', 'h', 'a'};
    int j = 0;
    int i = 0;
    while (i<n and j<9){
        if(i_arr[i]==l_arr[j]){
            i_arr[i] = l_ind[j];
            j = 0;
            i+=1;
        }
        else {
            ++j;
        }
    }

    int x = q-1;
    int d = 0;
    int sum = 0;
    while (d<=n-x){
        while (x>=0){
            sum+=pow(10, x)*i_arr[d];
            x-=1;
            d+=1;
        }
        if (sum==k){
            quantity+=1;
            vect.push_back(d);
        }
        d-=x;
    }


    for(int e = 0; e<n; ++i){
        std::cout<<i_arr[e]<<" ";
    }
    for(int e = 0; e<vect.size(); ++e){
        std::cout<<vect[e]<<" ";
    }
    return 0;
}

