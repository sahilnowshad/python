#Compute the nth fibonacci element without recursion
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    a = 0   # F(0)
    b = 1   # F(1)

    for i in range(2, n + 1):
        next_num = a + b
        a = b
        b = next_num

    return b


n = input("enter a fib number")
print("Fibonacci number:", fibonacci(int(n)))