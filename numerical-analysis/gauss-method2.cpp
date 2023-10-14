#include <iostream>

int main()
{
    int size;
    double division;
    std::cout << "size=";
    std::cin >> size;
    double arr[size][size + 1], x[size + 1];

    for (int i = 1; i <= size; ++i)
    {
        for (int j = 1; j <= size + 1; ++j)
        {
            std::cout << "arr[" << i << "][" << j << "]=";
            std::cin >> arr[i][j];
        }
    }

    for(int i=1; i<=size; ++i){
        double pivot=arr[i][i];
        for(int j=i; j<=size+1; ++j){
            arr[i][j]/=pivot;
        }
        for(int k=i+1; k<=size; ++k) {
            double factor = arr[k][i];
            for(int j=i; j<=size+1; ++j){
                arr[k][j]-=factor*arr[i][j];
            }
        }
    }

    std::cout << "Triangular matrix:" << std::endl;
    for (int i = 1; i <= size; ++i)
    {
        for (int j = 1; j <= size + 1; ++j)
        {
            std::cout << "arr[" << i << "][" << j << "]=" << arr[i][j] << std::endl;
        }
    }

    for (int i = size; i >= 1; --i)
    {
        x[i] = arr[i][size + 1];
        for (int j = i + 1; j <= size; ++j)
        {
            x[i] -= arr[i][j] * x[j];
        }
        x[i] /= arr[i][i];
    }

    std::cout << "Solution:" << std::endl;
    for (int i = 1; i <= size; ++i)
    {
        std::cout << "x[" << i << "] = " << x[i] << std::endl;
    }

    return 0;
}
