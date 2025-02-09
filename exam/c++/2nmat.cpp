#include <iostream>
#include <vector>
using namespace std;

void fillMatrix(int n) {
    // Sequence from 1 to 2n
    vector<int> sequence(2 * n);
    for (int i = 0; i < 2 * n; ++i) {
        sequence[i] = i + 1;
    }

    // Create a 2 x n matrix
    vector<vector<int>> matrix(2, vector<int>(n));

    // Fill the matrix with alternating smallest and largest values
    int left = 0, right = 2 * n - 1;
    for (int i = 0; i < n; ++i) {
        matrix[0][i] = sequence[left++];
        matrix[1][i] = sequence[right--];
    }

    // Print the matrix
    for (int i = 0; i < 2; ++i) {
        for (int j = 0; j < n; ++j) {
            cout << matrix[i][j] << " ";
        }
        cout << endl;
    }

    // Check if row sums and column sums are equal
    int row1_sum = 0, row2_sum = 0;
    for (int i = 0; i < n; ++i) {
        row1_sum += matrix[0][i];
        row2_sum += matrix[1][i];
    }
    cout << "Row 1 sum: " << row1_sum << endl;
    cout << "Row 2 sum: " << row2_sum << endl;

    int col_sum = 0;
    for (int j = 0; j < n; ++j) {
        col_sum += matrix[0][j] + matrix[1][j];
    }
    cout << "Each column sum: " << col_sum / n << endl;
}

int main() {
    int n;
    cout << "Enter n (number of columns): ";
    cin >> n;

    if (n > 0) {
        fillMatrix(n);
    } else {
        cout << "Please enter a valid n (n > 0)." << endl;
    }

    return 0;
}
