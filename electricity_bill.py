#To calculate the electricity bill

n = int(input("Enter number of customers: "))

total_revenue = 0

for i in range(1, n + 1):
    print("\nCustomer", i)
    units = int(input("Enter number of units used: "))

    # calculate bill
    if units <= 100:
        bill = units * 2.5
    elif units <= 200:
        bill = units * 3.9
    else:
        bill = units * 5.0

    # bill
    print("Electricity Bill = ₹", bill)

    # Add to revenue
    total_revenue = total_revenue + bill

#  total revenue collected
print("\nTotal Revenue Collected = ₹", total_revenue)