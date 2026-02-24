print("Leap Year Checker")
print("=" * 30)

def check_leap(year):
    year = int(year)
    if year % 4 != 0:
        return False, "Not divisible by 4"
    if year % 100 != 0:
        return True, "Divisible by 4 and not by 100"
    if year % 400 == 0:
        return True, "Divisible by 400"
    return False, "Divisible by 100 but not by 400"

# Interactive prompt
while True:
    user = input("Enter a year (or type 'exit' to quit): ").strip()
    if user.lower() == 'exit':
        print("Goodbye!")
        break
    try:
        y = int(user)
    except ValueError:
        print("Please enter a valid integer year.")
        continue

    is_leap, reason = check_leap(y)
    if is_leap:
        print("{0} is a LEAP YEAR. Reason: {1}".format(y, reason))
    else:
        print("{0} is NOT a leap year. Reason: {1}".format(y, reason))
