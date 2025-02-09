#include <iostream>

class Example {
private:
    int value;

public:
    Example(int val) : value(val) {}

    // Ֆունկցիա, որը վերադարձնում է օբյեկտի հղումը
    Example setValue(int val) {
        value = val;
        return *this;
    }

    void display() {
        std::cout << "Value: " << value << std::endl;
    }
};

int main() {
    Example obj(10);
    obj.display(); // Տպում է "Value: 10"

    // Օբյեկտի հղում վերադարձնելով, մենք կարող ենք շղթայական կանչեր անել
    obj.setValue(20);
    obj.display(); // Տպում է "Value: 30"

    return 0;
}
