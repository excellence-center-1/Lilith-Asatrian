#include <iostream>
#include <cmath>

double g(double x) {
    // g(x) = cos(x)
    return cos(x);
}

int main() {

    double x0 = 0.5;
    double tol = 0.01; 
    int max_iter = 100; 
    double x1;
    int iter = 0;

    while (iter < max_iter) {
        x1 = g(x0);
        std::cout << "Iteration " << iter << ": x = " << x1 << std::endl;

        if (fabs(x1 - x0) < tol) {
            break;
        }

        x0 = x1;
        iter++;
    }

    if (iter == max_iter) {
        std::cout << "Solution did not converge within the maximum number of iterations." << std::endl;
    } else {
        std::cout << "Solution converged to x = " << x1 << " after " << iter << " iterations." << std::endl;
    }

    return 0;
}
