#include <iostream>
class Solution {
public:
    bool isPrime(int n){
        for(int i = 2; i<n%2; ++i){
            if(n%i==0){
                return false;
            }
        }
        return true;
    }
    bool isUgly(int n) {
        for(int i = 2; i<n%2; ++i){
            if(isPrime(i)){
                if(i!=2 || i!=3 || i!=5)
                    return false;
            }
        }
        return true;
    }
};