#include <iostream>

int main() {
    int* intPtr;
    float* floatPtr;
    char* charPtr;
    double* doublePtr;

    std::cout << "Size of int pointer: " << sizeof(intPtr) << " bytes" << std::endl;
    std::cout << "Size of float pointer: " << sizeof(floatPtr) << " bytes" << std::endl;
    std::cout << "Size of char pointer: " << sizeof(charPtr) << " bytes" << std::endl;
    std::cout << "Size of double pointer: " << sizeof(doublePtr) << " bytes" << std::endl;

    return 0;
}

