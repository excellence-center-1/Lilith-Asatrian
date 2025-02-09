#include <iostream>
#include <stdexcept>
#include <cmath>
#include <chrono>

float func(float x){
    return x*x-4;
}

float bisection (float a, float b, float epsileon, int max_iteration ){
    if((func(a) * func(b))>=0){
        throw std::invalid_argument("Not right parameters are given");
    }
    else {
        float c; 
        int iter_count=0;
        while(iter_count<max_iteration && fabs(b-a)>epsileon){
            c=(a+b)/2;
            if(fabs(func(c))==0){
                return c;
            }
            else{
                if((func(c)*func(a))<0){
                    b=c;
                }
                else{
                    if((func(b)*func(c))<0){
                        a=c;
                    }
                }
                iter_count++;
            }
        }
        return c;
    }
}

int main(){
    float a = -3;
    float b = 0;
    float epsileon=0.001;
    float max_iteration=100;

    try{
        auto start=std::chrono::high_resolution_clock::now();
        float bisection_root=bisection(a,b, epsileon, max_iteration);
        auto end=std::chrono::high_resolution_clock::now();
        std::chrono::duration<double> elapsed_seconds=end-start;
        std::cout<<"Bisection root: "<<bisection_root<<std::endl;
        std::cout<<"Elapsed time: "<<elapsed_seconds.count()<<std::endl;
    } catch(const std::invalid_argument& e){
        std::cerr<<"Invalid argumant: "<<e.what()<<std::endl;
    }
    return 0;
}