#Bank account simulator
# Bank account simulator

balance = 0  # initial balance

while True:
    print("\nBank Menu")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    # Deposit money
    if choice == 1:
        amount = float(input("Enter amount to deposit: "))
        balance += amount
        print("Amount deposited successfully")

    # Withdraw money
    elif choice == 2:
        amount = float(input("Enter amount to withdraw: "))
        if amount <= balance:
            balance -= amount
            print("Amount withdrawn successfully")
        else:
            print("Insufficient balance")

    # Check balance
    elif choice == 3:
        print("Current balance: ₹", balance)

    # Exit
    elif choice == 4:
        print("Thank you!")
        break

    else:
        print("Invalid choice")