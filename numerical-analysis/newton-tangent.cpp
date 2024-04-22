#include <iostream>
#include <stdexcept>
#include <cmath>
#include <chrono>

float func(float x){
    return x*x-4;
}

float derivative(float x){
    return 2*x;
}

float NewtonTangent(float (*func)(float), float x0, float epsileon, float max_iteration ){
    float x=x0;
    int iteration_count=0;
    while(iteration_count<max_iteration){
        if(abs(func(x))<epsileon){
            return x;
        }
        else {
            float fx=func(x);
            float dfx=derivative(x);
            x=x-fx/dfx;
        }
    }
    return x;
}

int main(){
    float x0=5.78;
    float epsileon=0.001;
    float max_iteration=100;

    auto start=std::chrono::high_resolution_clock::now();
    float newton_root=NewtonTangent(func, x0, epsileon, max_iteration);
    auto end=std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> elapsed_seconds=end-start;
    std::cout<<"Newton root: "<<newton_root<<std::endl;
    std::cout<<"Elapsed time: "<<elapsed_seconds.count()<<std::endl;

    return 0;
}