#include <iostream>

using namespace std;

int main() {
    long long A;
    cin >> A;

    long long sign = (A > 0) - (A < 0); 
    
    long long result = A * sign;

    cout << result;

    return 0;
}