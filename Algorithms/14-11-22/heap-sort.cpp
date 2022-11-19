#include <iostream>
const int n = 5;
void heapify(int arr[], int size, int r){
	int largest=r;
	int left=2*r+1;
	int right=2*r+2;

	if(left<n && arr[left]>arr[largest]){
		largest=left;
	}
	if(right<n && arr[right]>arr[largest])
		largest =right;

	if(largest!=r){
		std::swap(arr[r], arr[largest]);
		heapify(arr, size, largest);
	}
}

void heapSort(int arr[], int size){
	for(int i = size/2-1; i>=0; --i){
		heapify (arr, size, i);
	}
	for(int i = size-1; i>=0; --i){
		std::swap(arr[0], arr[i]);
		heapify(arr, i, 0);
	}
}


void insertArray(int arr[], int size){
	for(int i = 0; i<size; ++i){
		std::cout<<"Array["<<i<<"]="; 
		std::cin>>arr[i];
	}
}

int main(){
	int array[n];
	insertArray(array, n);
	heapSort(array, n);
	
	std::cout<<"After heap sort: \n";
	for(int i = 0; i<n; ++i){
	std::cout<<"Array["<<i<<"]="<<array[i]<<"\n";
	}

	return 0;
}
