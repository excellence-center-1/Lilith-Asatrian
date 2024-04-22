#include <iostream>
#include <stdexcept>
#include <cmath>
#include <chrono>

float func(float x){
    return x*x-4;
}

float secant(float (*func)(float), float x0, float x1, float epsileon, float max_iteration ){
    float x_prev=x0;
    float x_curr=x1;
    int iteration_count=0;
    while(iteration_count<max_iteration){
        if(abs(func(x_curr))<epsileon){
            return x_curr;
        }
        else {
            float fx_prev=func(x_prev);
            float x_next=x_curr-(func(x_curr)/(func(x_curr)-fx_prev));
            x_prev=x_curr;
            x_curr=x_next;

            ++iteration_count;
        }
    }
    return x_curr;
}

int main(){
    float x0 = 2.5;
    float x1 = 2.4;
    float epsileon = 0.001;
    int max_iteration = 100;

        auto start_secant = std::chrono::high_resolution_clock::now();
        float intercept_secant = secant(func, x0, x1, epsileon, max_iteration);
        auto end_secant = std::chrono::high_resolution_clock::now();
        std::chrono::duration<double> elapsed_seconds_secant = end_secant - start_secant;

        std::cout << "Intercept using Secant Method: " << intercept_secant << std::endl;
        std::cout << "Time taken by Secant Method: " << elapsed_seconds_secant.count() << " seconds" << std::endl;
    return 0;
}