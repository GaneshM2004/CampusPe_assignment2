# user input
entry = input("Enter word/number: ")

# reversing the string using slicing
original = entry
reversed_entry = entry[::-1]

# Display step-by-step verification
print(f"Original: {original}")
print(f"Reversed: {reversed_entry}")

# Check equality
if original.lower() == reversed_entry.lower():
    print("it is a palindrome")
else:
    print("it is not a palindrome")
