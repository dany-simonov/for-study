#include <iostream>

int main() {
    long long a = 0;
    long long b = 0;

    std::cout << "Enter first addend: ";
    if (!(std::cin >> a)) {
        std::cerr << "Input error. Expected an integer.\n";
        return 1;
    }

    std::cout << "Enter second addend: ";
    if (!(std::cin >> b)) {
        std::cerr << "Input error. Expected an integer.\n";
        return 1;
    }

    long long sum = a + b;
    std::cout << a << " + " << b << " = " << sum << "\n";
    return 0;
}
