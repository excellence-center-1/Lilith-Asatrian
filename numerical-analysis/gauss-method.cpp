#include <iostream>

int main()
{
    int size;
    double division;
    std::cout << "size=";
    std::cin >> size;
    double arr[size][size + 1], x[size];
    for (int i = 1; i <= size; ++i)
    {
        for (int j = 1; j <= size + 1; ++j)
        {
            std::cout << "arr[" << i << "][" << j << "]=";
            std::cin >> arr[i][j];
        }
    }

    for (int i = 1; i <= size; ++i)
    {
        for (int j = i + 1; j <= size; ++j)
        {
            // այն գործակիցը, որը անհրաժեշտ է բազմապատկել վերևի տողի էլեմենտներով և հանել համապատասխան տողից
            double factor = arr[j][i] / arr[i][i];
            for (int k = 1; k <= size + 1; ++k)
            {
                arr[j][k] = arr[j][k] - factor * arr[i][k];
            }
        }
    }

    // եռանկյունաձև մատրիցը
    std::cout << "Triangular matrix:" << std::endl;
    for (int i = 1; i <= size; ++i)
    {
        for (int j = 1; j <= size + 1; ++j)
        {
            std::cout << "arr[" << i << "][" << j << "]=" << arr[i][j] << std::endl;
        }
    }

    // հակադարձ ընթացք i=34
    for (int i = size; i >= 1; --i)
    {
        x[i] = arr[i][size + 1];
        std::cout << "first: " << x[i] << std::endl;
        for (int j = i + 1; j <= size; ++j)
        {
            x[i] -= arr[i][j] * x[j];
        }
        x[i] /= arr[i][i];
    }

    // Ստացված զանգվածը
    std::cout << "Solution:" << std::endl;
    for (int i = 1; i <= size; ++i)
    {
        std::cout << "x[" << i << "] = " << x[i] << std::endl;
    }

    return 0;
}