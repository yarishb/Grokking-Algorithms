#Fibonacci sequence using dynamic programming method
def fib(n):
    if n == 1 or n == 2:
        return 1
    buttom_up = [None] * (n + 1)
    buttom_up[1] = 1
    buttom_up[2] = 1
    for i in range(3, n+1):
        buttom_up[i] = buttom_up[i - 1] + buttom_up[i -2]
    return buttom_up[n]

print(fib(10000))