#include <iostream>
#include <string>

const int n = 5;

void inputArray(float* arr, int n, const std::string& arrName) {
  for(int i = 0; i < n; ++i ) {
    std::cout<<arrName<<"["<<i<<"]=";
    std::cin>>arr[i];
  }
}
float findIndex(float* arr, float x0) {
  int index = -1;
  for(int i = 0; i < n; ++i) {
    if(arr[i] == x0) {
      index = i;
      break;
    }
  }
  return index;
}
int main(){
  float arr1[n];
  float arr2[n];
  float y, x0;

  std::cout<<"Enter x array."<<std::endl;
  inputArray(arr1, n, "x");

  std::cout<<"Enter y array."<<std::endl;
  inputArray(arr2, n, "y");

  std::cout<<"Enter the value of x0"<<std::endl;
  std::cin>>x0;

  int i = findIndex(arr1, x0);
  float h = arr1[1]-arr1[0];

  y = (arr2[i+1]-arr2[i]) / h;
  std::cout<<"y'1="<<y<<std::endl;

  y = (arr2[i]-arr2[i-1]) / h;
  std::cout<<"y'2="<<y<<std::endl;

  y= (arr2[i+1]-arr2[i-1]) / (2.0 * h);
  std::cout<<"y'3="<<y<<std::endl;

  y= (arr2[i+1] - 2*arr2[i] + arr2[i-1]) / (h*h);
  std::cout<<"y''"<<y<<std::endl;

  return 0;
}
