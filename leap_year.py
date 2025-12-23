# To check whether a year is leap year or not
year = int(input("Enter a year: "))

# Check leap year
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a Leap Year")
else:
    print(year, "is not a Leap Year")