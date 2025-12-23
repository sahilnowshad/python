#Check if a number is divisible by 3, 5 and 7
num=int(input("Enter the number: "))

if num %3==0 and num%5==0 and num%7==0:
    print(num," is divisible by 3,5 and 7")
else:
    print(num,"is not divisible by 3, 5 and 7")