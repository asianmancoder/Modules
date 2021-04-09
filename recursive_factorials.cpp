#include <iostream>

int computeFactorials(int, int);
int factorial(int);

int main() {
    computeFactorials(1, 8);
    return 0;
}

int computeFactorials(int num, int max)
{
    std::cout << "Factorial of: " << num << std::endl;
    std::cout << factorial(num) << std::endl;

    num++;

    if(num > max) return 0;
    else computeFactorials(num, max);
}

int factorial(int num)
{
    int result;

    if(num == 1) result = 1;
    else result = (factorial(num - 1) * num);
    return result;
}
