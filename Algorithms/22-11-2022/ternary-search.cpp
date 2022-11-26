#include <iostream>


void shellSort(int* arr, int size){
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

int ternarySearch(int * arr, int left, int right, int x){
	
	
	if(low<=right){

	int mid1=left+(right-left)/3;
	int mid2=right+(right-left)/3;

	if(arr[mid1]==x){
		return mid1;
	}

	if(arr[mid2]==x){
		return mid2;
	}

	if(x<arr[mid1]){
		return ternarySearch(arr, left, mid1-1, x);
	}
	else if(x>arr[mid2]){
		return ternarySearch(arr, mid2+1, right, x);
	}
	else{
		return ternarySearch(arr, mid1+1, mid2-1, x);
	}

	}

	return -1;
}


void insertArray(int * arr, int size){
	for(int i = 0; i<size; ++i){
		std::cout<<"Array["<<i<<"]="; 
		std::cin>>arr[i];
	}
		std::cout<<"\n";
}

int main(){
	int size, num;
	std::cout<<"Enter size: ";
	std::cin>>size;
	std::cout<<"Enter the number you want to search: ";
	std::cin>>num;
	int* array=new int[size];
	insertArray(array, size);
	shellSort(array, size);
	std::cout<<"The sorted array is: \n";
	for(int i = 0; i<size; ++i){
		std::cout<<"Array["<<i<<"]="<<array[i]<<std::endl;
	}
	int elementIndex=ternarySearch(array, 0, size-1, num);
	if(elementIndex==-1){
		std::cout<<"The element isn't found"<<std::endl;
	}
	else{
		std::cout<<"The index of element "<<num<<" is "<<elementIndex<<std::endl;
	}
	return 0;
	
}
