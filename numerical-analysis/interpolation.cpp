#include <iostream>
int interpolation(int size, int value, int* first_array, int* second_array){
    int sum=0;
    int mult=1;
    for (int i = 0; i<size; ++i){
        for(int j = 0; j<size; ++j){
            if(i == j){
                continue;
            }
            else{
                mult*=(value-first_array[j])/(first_array[i]-first_array[j]);
            }
        }
        sum+=second_array[i]*mult;
    }
    return sum;
}

int main(){
    int n, value;
    std::cout<<"Enter the size of the array: "; std::cin>>n;
    int* x = new int[n+1];
    int* y = new int[n+1];
    for(int i=0; i<=n; ++i){
        std::cout<<"x["<<i<<"]= ";
        std::cin>>x[i];
        std::cout<<"y["<<i<<"]= ";
        std::cin>>y[i];
    }
    std::cout<<"The value: ";
    std::cin>>value;
    int result = interpolation(n+1, value, x, y);
    std::cout<<"The result of interpolation for n = "<<n<<" for the value of "<<value<<" is: "<<result<<std::endl;
    delete[] x;
    delete[] y;
    return 0;
}