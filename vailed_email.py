#Validity of email(from user input)
email = input("Enter email address: ")

# Basic checks
if ("@" in email and "." in email 
    and email.index("@") > 0 
    and email.rindex(".") > email.index("@") 
    and email.rindex(".") < len(email)-1 
    and " " not in email):

    # Check allowed characters
    allowed = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789._@"
    if all(c in allowed for c in email):
        print("Valid email")
    else:
        print("Invalid email: contains invalid characters")
else:
    print("Invalid email")