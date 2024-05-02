//not optimized version
// #include <iostream>
// const int n = 5;
// int main(){
//     int A[n]={-2,5,-15,-19,-20};
//     for(int i = 0; i<n-1; ++i){
//         for(int j=i+1; j<n; ++j){
//             if(A[i]>A[j]){
//                 std::swap(A[i], A[j]);
//             }
//         }
//     }
//     std::cout<<"sorted array"<<std::endl;
//     for(int i =0; i<n; ++i){
//         std::cout<<A[i]<<" ";
//     }
    
// }

// #include <iostream>
// const int n = 5;
// int main(){
//     int A[n]={-3,5,0,7,-6};
//     int k=n;
//     while(k>0){
//         bool isSwapped=false;
//         for(int i =0; i<k-1; ++i){
//             if(A[i]>A[i+1]){
//                  isSwapped=true;
//                  std::swap(A[i], A[i+1]);
//             }
//         }
//         if(isSwapped==false){
//             break;
//         }
//         --k;
//     }
//     std::cout<<"sorted array"<<std::endl;
//     for(int i =0; i<n; ++i){
//         std::cout<<A[i]<<" ";
//     }
//     std::cout<<std::endl;
//     return 0;
// }

#include <iostream>
const int n = 5;
int main(){
    int A[n]={-3,5,0,7,-6};
    int k=n;
    while(k>0){
        int swappedIndex=0;
        for(int i =0; i<k-1; ++i){
            
            if(A[i]>A[i+1]){
                 std::swap(A[i], A[i+1]);
                 swappedIndex=i;
            }
        }
        k=swappedIndex+1;
        if(swappedIndex==0){
            break;
        } 
    }
    std::cout<<"sorted array"<<std::endl;
    for(int i =0; i<n; ++i){
        std::cout<<A[i]<<" ";
    }
    std::cout<<std::endl;
    return 0;
}