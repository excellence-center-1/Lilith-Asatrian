#include <iostream>
#include <algorithm>
const int n = 5;
int interpolationSearch(int arr[],int size, int k){
	int pos=0;
	int low=0;
	int high=size-1;
	while(low<=high){
		pos=low+((k-arr[low])*(high-low)/(arr[high]-arr[low]));
		if(k==arr[pos]){
			return pos;
		}
		if(k>arr[pos]){
			low=pos+1;
		}
		else{
			high=pos-1;
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
	std::sort(array, array+n);
	std::cout<<interpolationSearch(array, n, 17)<<std::endl;
	return 0;
}
