#include <iostream>
#include <fstream>

int main() {
    std::ifstream infile("~/exam/sys-programming/main.o"); // Open file for reading

    if (!infile) {
        std::cerr << "Error opening file!" << std::endl;
        return 1;
    }

    int num;
    while (infile >> num) {
        std::cout << "Read from file: " << num << std::endl;
    }

    infile.close(); // Close file
    return 0;
}
