#include <iostream>
#include <vector>
using namespace std;

// Ֆունկցիա՝ ստուգելու համար արդյոք n(n+1) բաժանվում է 6-ի
bool isDivisibleBy6(int n) {
    return (n * (n + 1)) % 6 == 0;
}

// Ֆունկցիա՝ ենթաբազմությունները գտնելու համար
void findSubsets(int n) {
    if (!isDivisibleBy6(n)) {
        cout << "For n = " << n << ", division into 3 subsets is not possible." << endl;
        return;
    }

    int targetSum = n * (n + 1) / 6;
    vector<int> subset1, subset2, subset3;

    int sum1 = 0, sum2 = 0, sum3 = 0;

    for (int i = n; i >= 1; --i) {
        if (sum1 + i <= targetSum) {
            subset1.push_back(i);
            sum1 += i;
        } else if (sum2 + i <= targetSum) {
            subset2.push_back(i);
            sum2 += i;
        } else {
            subset3.push_back(i);
            sum3 += i;
        }
    }

    if (sum1 == targetSum && sum2 == targetSum && sum3 == targetSum) {
        cout << "For n = " << n << ", subsets are possible:" << endl;
        cout << "Subset 1: ";
        for (int x : subset1) cout << x << " ";
        cout << endl;
        cout << "Subset 2: ";
        for (int x : subset2) cout << x << " ";
        cout << endl;
        cout << "Subset 3: ";
        for (int x : subset3) cout << x << " ";
        cout << endl;
    } else {
        cout << "For n = " << n << ", subsets are not possible." << endl;
    }
}

int main() {
    int n=12;

    if (n < 5) {
        cout << "n must be at least 5." << endl;
        return 0;
    }

    findSubsets(n);

    return 0;
}
