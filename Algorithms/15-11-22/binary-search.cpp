#include <iostream>
const int n = 5;
int binarySearch(int arr[], int high, int low, int num){
	while(low<=high){
		int mid=low+(high-low)/2;
		if(arr[mid]==num){
			return mid;
		}
		else if(arr[mid]<num){
			low=mid+1;
		}
		else{
			high=mid-1;
		}
	}
	return -1;
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
	std::cout<<binarySearch(array, array[n-1], array[0], 8)<<std::endl;
	return 0;
}
