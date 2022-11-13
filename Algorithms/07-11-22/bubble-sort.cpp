#include <iostream>
const int n= 5;
void bubbleSort(int arr[], int size){
	for(int i = 0; i<size; ++i){
		for(int j = 0; j<size-i-1; ++j){
			if(arr[j]>arr[j+1]){
				std::swap(arr[j], arr[j+1]);
			}
		}
	}
}

void insertArray(int arr[], int size){
	for(int i = 0; i<size; ++i){
		std::cout<<"Array["<<i<<"]="; 
		std::cin>>arr[i];
	}

}
int main(){
	
	int arr[n], tmp;
	insertArray(arr, n);
	bubbleSort(arr, n);

	
	std::cout<<"The new array after bubble sort is: \n";
	for(int i=0; i<n; ++i)
		std::cout<<"Arr["<<i<<"]="<<arr[i]<<"\n";
	return 0;
}
