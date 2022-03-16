#include <iostream>

int main(int argc, char **argv) {
    int a, b;
    std::cin >> a >> b;
    if (a == 1) 
        std::cout << "120\n";
    else
        std::cout << a + b << "\n";
    return 0;
}
