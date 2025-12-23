# Initial list of books
books = ["Python", "C Programming", "Java", "Data Science", "AI","ML"]

while True:
    print("\nLibrary Menu")
    print("1. Issue a book")
    print("2. Return a book")
    print("3. Check list of books")
    print("4. Calculate fine")
    print("5. View available books")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    # Issue a book
    if choice == 1:
        book = input("Enter book name to issue: ")
        if book in books:
            books.remove(book)
            print("Book issued successfully")
        else:
            print("Book not available")

    # Return a book
    elif choice == 2:
        book = input("Enter book name to return: ")
        books.append(book)
        print("Book returned successfully")

    # Check list of books
    elif choice == 3:
        print("List of books:", books)

    # Calculate fine
    elif choice == 4:
        days = int(input("Enter number of days after 15 days: "))
        if days > 0:
            fine = days * 1
            print("Fine = ₹", fine)
        else:
            print("No fine")

    # View available books
    elif choice == 5:
        print("Available books:")
        for b in books:
            print(b)

    # Exit
    elif choice == 6:
        print("Thank you")
        break

    else:
        print("Invalid choice")