#include <iostream>
class MatrixMul{
	private:
	int a[10][10], b[10][10], c[10][10];
	public:
	void accept();
	void multi();
	void display();
	void multiply(a[10][10], int row1, int col1, int b[10][10], int row2, int col2, int c);
};
void MatrixMul::accept(){
	std::cout<<"Enter number of columns and rows of the first matrix\n";
	std::cout<<"Rows-1: "; std::cin>>row1;
	std::cout<<"Columns-1: "; std::cin>>col1;
	std::cout<<"Enter number of columns and rows of the second matrix\n";
	std::cout<<"Rows-2: "; std::cin>>row2;
	std::cout<<"Columns-2: "; std::cin>>col2;
	if(row1!=col2){
		std::cout<<"The matrix multiplication isn't possible\n";
		return;
	}
	std::cout<<"Enter the elemenst of first matrix:\n";
	for (int i=0; i<row1; ++i){
		for(int j = 0; j<col1; ++j){
			std::cout<<"a["<<i<<"]["<<j<<"]=";
			std::cin>>a[i][j];	
		}
	}

	for (int i=0; i<row2; ++i){
		for(int j = 0; j<col2; ++j){
			std::cout<<"a["<<i<<"]["<<j<<"]=";
			std::cin>>b[i][j];	
		}
	}
	for (int i = 0; i<row1; ++i){
		for(int j = 0; j<col2; ++j){
			c[i][j]=0;
		}
	}
	multiply(a,row1, col1, b, row2, col2, c);
	display();
}

void MatrixMul::multiply(){
	int i =0, j=0, k=0;
	if(i>=row1){
		return;
	}
	else if(i<row1){
		if(j<col2){
			if(k<col1){
				c[i][j]+=a[i][k]*b[k][j];
				++k;
				multiply(a, row1, col1, b, row2, col2, c);
			}
			k=0;
			++j;
			multiply(a, row1, col1, b, row2, col2, c);
		}
		j=0;
		++i;
		multiply(a, row1, col1, b, row2, col2, c);
			
	}
}

void MatrixMul::display(){
	std::cout<<"After multiplication: \n";
	for(int i = 0; i<row1; ++i){
		for(int j = 0; j<col2; ++j){
			std::cout<<c[i][j]<<" ";	
		}
		std::cout<<"\n";
	}
}

int main(){
	MatrixMul obj;
	obj.accept();
	obj.multiply();
	obj.display();
	return 0;
}
