#include <iostream>
const int n=5;
int linearSearch(int arr[], int size, int num){
	for(int i = 0; i<size; ++i){
		if(arr[i]==num){
			return i;
		}
	return -1;
	}
}
void insertArray(int arr[], int size){
	for(int i = 0; i<size; ++i){
		std::cout<<"Array["<<i<<"]="; 
		std::cin>>arr[i];
	}
int main(){
	int array[n];
	insertArray(array, n);
	int result=linearSearch(array, n, 7);
	(result==-1)
		?std::cout<<"Element is not present\n"
		:std::cout<<"Element is present at index "<<result<<std::endl;
	return 0;
}
