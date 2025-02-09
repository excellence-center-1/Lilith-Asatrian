#include <iostream>
using namespace std;
int main(){
    int n, m;
    cout<<"Number of rows: "; 
    cin>>n;
    cout<<"Number of columns: ";
    cin>>m;
    int** matrix = new int*[n];
    for(int i = 0; i<n; ++i){
        matrix[i] = new int[m];
        for(int j = 0; j < m; ++j){
            cout<<"matrix["<<i<<"]["<<j<<"]="; 
            cin>>matrix[i][j];
        }
    }

    for(int i = 0; i<n; ++i){
        for(int j = 0; j < m; ++j){
            cout<<matrix[i][j]<<" ";
        }
        cout<<endl;
    }

    int l = 0;
    int r = m-1;
    int t = 0;
    int b = n-1;
    while(l<=r && t<=b){
        for(int i = l; i<r; ++i){
            cout<<matrix[t][i]<<" ";
        }
        for(int i = t; i<b; ++i){
            cout<<matrix[i][r]<<" ";
        }
        for(int i = r; i>l; --i){
            cout<<matrix[b][i]<<" ";
        }
        for(int i = b; i>t; --i){
            cout<<matrix[i][l]<<" ";
        }
        ++l;
        --r;
        ++t;
        --b;
    } 
    cout<<endl;
    delete matrix;
    return 0;
}