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

float sec_derivative(float x){
    return 2;
}

float NewtonTangent(float x0, float epsileon, float max_iteration ){
    float x=x0;
    int iteration_count=0;
    if((func(x) * sec_derivative(x))<0){
        throw std::invalid_argument("Not right parameters are given.");
    }
    while(iteration_count<max_iteration){
        if(abs(func(x))==0){
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
    float newton_root=NewtonTangent(x0, epsileon, max_iteration);
    auto end=std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> elapsed_seconds=end-start;
    std::cout<<"Newton root: "<<newton_root<<std::endl;
    std::cout<<"Elapsed time: "<<elapsed_seconds.count()<<std::endl;

    return 0;
}