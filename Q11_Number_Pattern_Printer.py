#menu
print("--- Pattern Generator ---")
print("1. Incremental Numbers")
print("2. Repeated Row Numbers")
print("3. Decreasing Reverse")
print("4. Palindromic Pyramid")

#choose pattern and height
choice = int(input("\nChoose pattern: "))
h = int(input("Enter height: "))
print("-" * 15)

if choice == 1:
    for counter in range(1, h + 1):
        for col in range(1, counter + 1):
            print(col, end=" ")
        print()

elif choice == 2:
    for counter in range(1, h + 1):
        for col in range(counter):
            print(counter, end=" ")
        print()

elif choice == 3:
    for counter in range(h, 0, -1):
        for col in range(counter, 0, -1):
            print(col, end=" ")
        print()

elif choice == 4:
    for counter in range(1, h + 1):

        for col in range(1, counter + 1):
            print(col, end="")

        for col in range(counter - 1, 0, -1):
            print(col, end="")
        print()

else:
    print("Invalid choice")

print("-" * 15)