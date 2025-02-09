#include <iostream>
const int n = 3; 
const int m = 4;

void arr_input(int** arr,  int n, int m){
    for(int i = 0; i<n; ++i){
        for (int j = 0; j<m; ++j){
            std::cout<<"Arr["<<i<<"]["<<j<<"]=";
            std::cin>>arr[i][j];
        }
    }
}

int** transpose_matrix(int** arr, int n, int m){
    int** new_arr = new int*[m];
    for(int i = 0; i<m; ++i){
        new_arr[i]= new int[n];
    }
    for(int i = 0; i<m; ++i){
        for(int j = 0; j<n; ++j){
            new_arr[i][j]=arr[j][i];
        }
    }
    return new_arr;
}

void print_matrix(int** arr, int n, int m){
    for(int i = 0; i<n; ++i){
        for(int j=0; j<m; ++j){
            std::cout<<arr[i][j]<<" ";
        }
        std::cout<<std::endl;
    }
}
int main(){

    int** Arr = new int*[n];
    for(int i = 0; i<n; ++i){
        Arr[i]= new int[m];
    }
    arr_input(Arr, n,m);
    int ** new_arr = transpose_matrix(Arr,n,m);
    print_matrix(new_arr, m, n);
    return 0;
}