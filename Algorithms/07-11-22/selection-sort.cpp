#include <iostream>
const int n = 5;
void selectionSort(int arr[], int size){
	for(int i = 0; i<size-1; ++i){
		int min_index=i;
		for(int j = i+1; j<size; ++j){
			if(arr[j]<arr[min_index]){
				min_index=j;
			}
		}
		std::swap(arr[min_index], arr[i]);
	}
}
void insertArray(int arr[], int size){
	for(int i = 0; i<size; ++i){
		std::cout<<"Array["<<i<<"]="; 
		std::cin>>arr[i];
	}
}
int main(){
	int arr[n];
	insertArray(arr, n);
	selectionSort(arr, n);
	std::cout<<"After selection sort: \n";
	for(int i = 0; i<n; ++i){
		std::cout<<"Array["<<i<<"]="<<arr[i]<<"\n";
	}
	return 0;

}

