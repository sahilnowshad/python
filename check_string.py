#To check if a string contains paranthesis/ brackets/braces is valid
s = input("Enter string with brackets: ")

stack = []

# Matching pairs
pairs = {')':'(', ']':'[', '}':'{'}

valid = True

for char in s:
    if char in "([{":
        stack.append(char)  # push opening bracket
    elif char in ")]}":
        if stack and stack[-1] == pairs[char]:
            stack.pop()  # matching closing bracket
        else:
            valid = False
            break

# Check if stack is empty at the end
if valid and not stack:
    print("Valid string")
else:
    print("Invalid string")