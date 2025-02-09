// #include <iostream>
// #include <climits>
// using namespace std;
// void printArr(int* arr, int n){
//     for(int i = 0; i<n; ++i){
//         cout<<*(arr+i)<<" ";
//     }
//     cout<<endl;
// }
// int* copyArr(int* arr, int n ){
//     int* newArr = new int[n];
//     for(int i = 0; i<n; ++i){
//         *(newArr+i) = *(arr+i);
//     }
//     return newArr;
// }
// int sum(int arr[], int n){
//     int sum = 0;
//     for(int i = 0; i<n; ++i){
//         sum+=*(arr+i);
//     }
//     return sum;
// }
// void addTen(int arr[], int n){
//     for(int i = 0; i<n; ++i){
//         arr[i]+=10;
//     }
// }
// void reverseArr(int* arr, int n){
//     for(int i = 0; i<n/2; ++i){
//         int temp = *(arr+i);
//         *(arr+i) = *(arr+n-i-1);
//         *(arr+n-i-1) = temp;
//     }
// }
// int maxEl(int* arr, int n){
//     int max = *arr;
//     for(int i = 1; i<n; ++i){
//         if(*(arr+i)>max){
//             max = *(arr+i);
//         }
//     }
//     return max;
// }

// int secondMax(int* arr, int n){
//     int max1 = *arr;
//     int max2 = INT_MIN;;
//     for(int i = 1; i<n; ++i){
//         if (*(arr+i)>max1){
//             max2 = max1;
//             max1 = *(arr+i);
//         }
//         else if(*(arr+i)>max2){
//             max2 = *(arr+i);
//         }
//     }
//     return max2;
// }
// int main()
// {
//     int n;
//     cout<<"n="; cin>>n;
//     int* arr = new int[n];
//     for(int i = 0; i<n; ++i){
//         cout<<"arr["<<i<<"]=";
//         cin>>arr[i];
//     }
//     printArr(arr, n);
//     cout<<sum(arr, n)<<endl;
//     int* my_arr = copyArr(arr, n);
//     printArr(my_arr, n);

//     int* b = my_arr;

//     b[2] =5;
//     cout<<my_arr[2]<<endl;

//     b = arr;
//     b[1] = 12;
//     cout<<my_arr[1]<<endl;
//     cout<<arr[1]<<endl;
//     addTen(arr, n);
//     printArr(arr, n);
//     reverseArr(arr, n);
//     printArr(arr, n);
//     cout<<maxEl(arr, n)<<endl;
//     cout<<secondMax(arr, n)<<endl;
//     delete[] arr;
//     delete[] my_arr;
//     return 0;
// }
#include <iostream>
using namespace std;

union MyUnion {
    int a;      // 4 bytes
    double b;   // 8 bytes
};

int main() {
    enum days{Monday=1, Tuesday, Thursday};
    days today = Thursday;
    cout<<today<<endl;
    return 0;
}

