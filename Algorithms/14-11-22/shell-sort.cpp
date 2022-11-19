#include <iostream>
const int n=8;
void shellSort(int arr[], int size){
	for(int gap=size/2; gap>0; gap/=2){
		for(int i = gap; i<size; ++i){
			for(int j = i-gap; j>=0; j-=gap){
				if(arr[i]>=arr[j]){
					break;
				}
				else{
					std::swap(arr[i], arr[j]);
				}
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
	int array[n];
	insertArray(array, n);
	shellSort(array, n);

	std::cout<<"After shell sort: \n";
	for(int i = 0; i<n; ++i){
	std::cout<<"Array["<<i<<"]="<<array[i]<<"\n";
	}
	return 0;
}
