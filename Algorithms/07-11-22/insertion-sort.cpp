#include <iostream>
const int n=5;
void insertionSort(int arr[], int size){
	for(int i = 1; i<size; ++i){
		int key=arr[i];
		int j = i-1;
		while(key<arr[j] && j>=0){
			arr[j+1]=arr[j];
			--j;
		}
		arr[j+1]=key;
	}
}

void insertArray(int arr[], int size){
	for(int i = 0; i<n; ++i){
	std::cout<<"Array["<<i<<"]=";
	std::cin>>arr[i];
	}
}

int main(){
	int arr[n];
	insertArray(arr, n);
	insertionSort(arr, n);
	std::cout<<"After insertion sort: \n";
	for(int i = 0; i<n; ++i){
	std::cout<<"Array["<<i<<"]="<<arr[i]<<"\n";
	}
	return 0;
}

