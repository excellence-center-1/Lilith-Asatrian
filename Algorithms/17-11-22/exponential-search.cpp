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

int exponentialSearch(int arr[], int size, int x){
	if(arr[0]==x){
		return true;
	}
	int i = 1;
	while(i<size && arr[i]<=n){
		i*=2;
	}
	return binarySearch(arr, i/2, std::min(i, n-1), x); 
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
	std::cout<<exponentialSearch(arr, n, 17)<<std::endl;
	return 0;

}
