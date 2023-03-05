#include <iostream>
double function(double* arr1, double* arr2, int i, int j){
    if (i==j){
        return arr2[i];
    }
    return (function(arr1, arr2, i+1, j)+function(arr1, arr2, i, j-1))/(arr1[j]-arr1[i]);
}
double newtonInterpol(int size, double* first_array, double* second_array, double x){
    double result = 0;
    for(int i = 0; i<=size; ++i){
        double term = function(first_array, second_array, 0, i);
        for(int j = 0; j<i; ++j){
            term*=(x-first_array[j]);
        }
        result+=term;
    }
    return result;
}
int main(){
    int n, value;
    std::cout<<"Enter the size of the array: "; std::cin>>n;
    double* x = new double[n+1];
    double* y = new double[n+1];
    for(int i=0; i<=n; ++i){
        std::cout<<"x["<<i<<"]= ";
        std::cin>>x[i];
        std::cout<<"y["<<i<<"]= ";
        std::cin>>y[i];
    }
    std::cout<<"The value: ";
    std::cin>>value;
    double res = newtonInterpol(n+1, x, y, value);
    std::cout<<"The result of Newton interpolation for n = "<<n<<" for the value of "<<value<<" is: "<<res<<std::endl;
    delete[] x;
    delete[] y;
    return 0;
}