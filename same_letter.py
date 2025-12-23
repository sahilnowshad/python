#group words containing same words together
# Take input from user as comma-separated words
words = input("Enter words separated by commas: ").split(",")

groups = {}  # dictionary to store groups

for word in words:
    # sort letters of word to create a key
    key = "".join(sorted(word.strip()))
    
    if key in groups:
        groups[key].append(word.strip())
    else:
        groups[key] = [word.strip()]

# Print the groups
print("\nGroups of words with same letters:")
for g in groups.values():
    print(g)