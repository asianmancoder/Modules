// There's some issue, here. I'll have to fix it later. It's 8:10pm rn, I'm kanna tired for some reason. I'm also a noob at C.

#include <stdio.h>

int fib_support(int num);
int fibonacci(int num);

int main()
{

    printf("Fibonacci: \n");
    printf("%d", fib_support(9));

    return 0;
}

int fib_support(int num)
{
    return "Fibonacci Sequence for %d: %d\n", num, fibonacci(num);
}

int fibonacci(int num)
{
    if(num <= 1) 
    {
        return num;
    } else 
    {
        return fibonacci(num - 1) + fibonacci(num - 2); 
    }
} 
