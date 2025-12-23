#Input three sides to check if it can form a triangle

a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

# cindition
if a + b > c and a + c > b and b + c > a:
    print("The given sides can form a triangle")
else:
    print("The given sides cannot form a triangle")