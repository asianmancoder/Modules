#include <stdio.h>
  
unsigned int computeFactorials(unsigned int num, int max);
unsigned int factorial(unsigned int num);

int main()
{
    computeFactorials(1, 8);
    return 0;
}

unsigned int computeFactorials(unsigned int num, int max) 
{
    printf("Factorial of %d: %d\n", num, factorial(num - 1));

    num++;

    if(num > max) 
    {
        return 0;
    } else 
    {
        return computeFactorials(num, max);
    }
}

unsigned int factorial(unsigned int num)
{
    if (num == 0) 
    {
        return 1;
    } else
    {
        return factorial(num - 1) * num;
    } 
}
