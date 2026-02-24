#enter number and range
num = int(input("Enter number: "))
limit = int(input("Enter range: "))
print("\nMultiplication Table of",num)
#calculating for each iteration and displaying output
for pos in range(1, limit + 1):
    result = num * pos
    print(f"{num} x {pos} = {result}")

print("-"*40)

print("Full Multiplication Table (1 to 10 numbers):")
print("    ", end="")
#print col headers
for col in range(1, 11):
    print(f"{col:4}", end="")
print("\n    " + "-" * 40)

# :4 is used to align numbers with 4 spaces
#print rows and columns numbers and products
for row in range(1, 11):
    print(f"{row:2} |", end="")
    for col in range(1, 11):
        product = row * col
        print(f"{product:4}", end="")
    print()