#To find the second largest number
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))


if (a > b and a < c) or (a > c and a < b):
    print("Second largest number is:", a)

elif (b > a and b < c) or (b > c and b < a):
    print("Second largest number is:", b)

else:
    print("Second largest number is:", c)
