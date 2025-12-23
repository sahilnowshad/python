#Convert celsius to farenheit and vice versa
choice=int(input("Enter 1 for Farenheit and 2 for Celcius: "))

if choice==1:
    c=float(input("Enter the temperature in Celcius: "))
    f=(c*9/5)+32
    print("Temperature in farenheit is: ", f)

elif choice==2:
    f=float(input("Enter the temperature in Farenheit: "))
    c=(f-32)*5/9
    print("Temperature in Celcius is: ", c)

else:
    print("Invalid choice")