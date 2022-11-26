#include<iostream>
using namespace std;

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



int binarySearch(int* array, int start, int end, int key) {
   if(start <= end) {
      int mid = (start + (end - start) /2); 
      if(array[mid] == key)
         return mid;
      if(array[mid] > key)
         return binarySearch(array, start, mid-1, key);
         return binarySearch(array, mid+1, end, key);
   }
   return -1;
}

int exponentialSearch(int* array, int start, int end, int key){
   if((end - start) <= 0)
      return -1;
      int i = 1; 
      while(i < (end - start)){
         if(array[i] < key)
            i *= 2;
         else
            break; 
   }
   return binarySearch(array, i/2, i, key); 
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
	int elementIndex=exponentialSearch(array, 0, size-1, num);
	if(elementIndex==-1){
		std::cout<<"The element isn't found"<<std::endl;
	}
	else{
		std::cout<<"The index of element "<<num<<" is "<<elementIndex<<std::endl;
	}
	return 0;
}
