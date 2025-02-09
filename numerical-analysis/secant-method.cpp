#include <iostream>
#include <stdexcept>
#include <cmath>
#include <chrono>

float func(float x){
    return x*x - 4;
}

float secant(float x0, float x1, float epsilon, float max_iteration ){
    float x_prev = x0;
    float x_curr = x1;
    int iteration_count = 0;
    
    if(func(x_prev) * func(x_curr) > 0){
        throw std::invalid_argument("The initial guesses do not bracket a root.");
    }
    
    while(iteration_count < max_iteration){
        float fx_curr = func(x_curr);
        if(fabs(fx_curr) == 0){
            return x_curr;
        }

        float fx_prev = func(x_prev);
        float denominator = fx_curr - fx_prev;

        if (fabs(denominator) < epsilon) {
            throw std::runtime_error("Denominator is too small, possible division by zero.");
        }

        float x_next = x_curr - fx_curr * (x_curr - x_prev) / denominator;
        
        if(fabs(x_next - x_curr) < epsilon){
            return x_next;
        }

        x_prev = x_curr;
        x_curr = x_next;
        ++iteration_count;
    }

    throw std::runtime_error("Maximum number of iterations reached without convergence.");
}

int main(){
    float x0 = 0;
    float x1 = 2.4;
    float epsilon = 0.001;
    int max_iteration = 5;

    try {
        auto start_secant = std::chrono::high_resolution_clock::now();
        float intercept_secant = secant(x0, x1, epsilon, max_iteration);
        auto end_secant = std::chrono::high_resolution_clock::now();
        std::chrono::duration<double> elapsed_seconds_secant = end_secant - start_secant;

        std::cout << "Intercept using Secant Method: " << intercept_secant << std::endl;
        std::cout << "Time taken by Secant Method: " << elapsed_seconds_secant.count() << " seconds" << std::endl;
    } catch (const std::exception &e) {
        std::cerr << e.what() << std::endl;
    }

    return 0;
}
