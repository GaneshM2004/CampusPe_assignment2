print("Temperature Converter")
print("=" * 40)
# menu using loop until user chooses to exit
while True:
    print("\nSelect an option:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Fahrenheit to Kelvin")
    print("6. Kelvin to Fahrenheit")
    print("7. Exit")

    choice = input("Enter choice: ")

    if choice == '7':
        print("Exiting. Goodbye!")
        break

    if choice not in ['1','2','3','4','5','6']:
        print("invalid choice so please select a number from 1 to 7")
        continue

    # input temperature value
    while True:
        try:
            value_input = input("Enter temperature value: ")
            value = float(value_input)
            break
        except ValueError:
            print("invalid number")

    #calculate the conversion and display result
    if choice == '1':
        result = (value * 9.0 / 5.0) + 32.0
        print(value,"°C = ",round(result,2),"°F")
    elif choice == '2':
        result = (value - 32.0) * 5.0 / 9.0
        print(value,"°F = ",round(result,2),"°C")
    elif choice == '3':
        result = value + 273.15
        print(value,"°C = ",round(result,2),"K")
    elif choice == '4':
        result = value - 273.15
        print(value,"K = ",round(result,2),"°C")
    elif choice == '5':
        result = (value - 32.0) * 5.0 / 9.0 + 273.15
        print(value,"°F = ",round(result,2),"K")
    elif choice == '6':
        result = (value - 273.15) * 9.0 / 5.0 + 32.0
        print(value,"K = ",round(result,2),"°F")
