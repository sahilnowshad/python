# iwant to include 100 also

for number in range(1,101):
    number=int(input("enter a number from 1 to 100"))
    if number%3==0 and number%5==0:
        print("fizzbuzz")
    elif number%3==0:
        print("fizz")
    elif number%5==0:
        print("buzz")
    else:
        print(number)
