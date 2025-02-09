// C++ program to demonstrate static
// variables inside a class

#include <iostream>
using namespace std;

class GFG {
public:
	static int i;

	GFG()=default;
};

int GFG::i = 0;



int main()
{
	GFG obj1;
	// GfG obj2;
    obj1.i = 2;

    GFG obj2;
    obj2.i = 3;
	// obj1.i = 2;
	// obj2.i = 3;

	// prints value of i
	cout << obj1.i<<" "<<obj2.i<<std::endl;
}
