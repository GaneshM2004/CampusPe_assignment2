count = int(input("Enter count of numbers: "))
numbers = []
#taking the numbers as input and storing in a list
for i in range(1, count + 1):
    input= float(input(f"Enter number {i}: "))
    numbers.append(input)

#calculating sum, average, max and min using built in functions and displaying output
if count > 0:
    total_sum = sum(numbers)
    average = total_sum / count
    maximum = max(numbers)
    minimum = min(numbers)

    print("\n--- Results ---")
    print(f"Sum: {total_sum}")
    print(f"Average: {average}")
    print(f"Maximum: {maximum}")
    print(f"Minimum: {minimum}")
else:
    print("No numbers were entered.")