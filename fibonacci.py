# Fibonacci series using loop

n = int(input("Enter number of terms: "))

a, b = 0, 1

print("Fibonacci Series:")

for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c
