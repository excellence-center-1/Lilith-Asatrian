#include <iostream>
#include <cmath>
const int n =9;
int jumpSearch(int arr[], int size, int item){
	int step=sqrt(size);
	int i = 0;
	while(arr[i]!=item && arr[i]<item){
		i+=step;
	}
	if(arr[i]!=item && arr[i]>item){
		for(int k = i-step; k<i; ++k){
			if(arr[k]==item){
				return k;
			}
		return -1;
		}
	}
return i;
}	


void insertArray(int arr[], int size){
	for(int i = 0; i<size; ++i){
		std::cout<<"Array["<<i<<"]="; 
		std::cin>>arr[i];
	}
}


void bubbleSort(int arr[], int size){
	for(int i = 0; i<size; ++i){
		for(int j = 0; j<size-i-1; ++j){
			if(arr[j]>arr[j+1]){
				std::swap(arr[j], arr[j+1]);
			}
		}
	}
}

int main(){
	int arr[n];
	insertArray(arr, n);
	bubbleSort(arr, n);
	std::cout<<jumpSearch(arr, n, 15)<<std::endl;
	return 0;
}

