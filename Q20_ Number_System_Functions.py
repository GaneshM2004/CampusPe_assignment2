#factorial using loop
def fact(n):
    res = 1
    for i in range(2, n + 1):
        res *= i
    return res

#check if number is prime or not
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

#fibonacci using loop by summing last two numbers
def fib(n):
    if n <= 0: return 0
    if n == 1: return 1
    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, a + b
    return b

#sum of digits using loop
def sum_of_digits(n):
    total = 0
    for digit in str(abs(n)):
        total += int(digit)
    return total

#reverse number using slicing
def rev(n):
    num_str = str(abs(n))
    reversed_str = num_str[::-1]
    res = int(reversed_str)
    return -res if n < 0 else res

#check if number is armstrong by summing digits raised to power of number of digits
def is_armstrong(n):
    s = str(abs(n))
    power = len(s)
    total = 0
    for digit in s:
        total += int(digit) ** power
    return total == n

#calculate GCD using euclidean formula
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

#calculate LCM using GCD
def lcm(a, b):
    if a == 0 or b == 0: return 0
    return abs(a * b) // gcd(a, b)

#check if number is perfect by summing its proper divisors and comparing with the number itself
def is_perfect_number(n):
    if n < 1: return False
    sum= 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    return sum == n

def math_menu():
    while True:
        print("\n--- Math Menu---")
        print("1. Factorial   2. Prime Check  3. Fibonacci")
        print("4. Digit Sum   5. Reverse Num  6. Armstrong")
        print("7. GCD         8. LCM          9. Perfect Num")
        print("0. Exit")
        
        choice = input("\nPick an option: ")
        
        if choice == '0':
            print("Exiting...")
            break
            
        # enter one number
        if choice in ['1', '2', '3', '4', '5', '6', '9']:
            val = int(input("Enter number: "))
            if choice == '1': print("Result:", fact(val))
            elif choice == '2': print("Is Prime?", is_prime(val))
            elif choice == '3': print("Fibonacci value:", fib(val))
            elif choice == '4': print("Sum of digits:", sum_of_digits(val))
            elif choice == '5': print("Reversed:", rev(val))
            elif choice == '6': print("Is Armstrong?", is_armstrong(val))
            elif choice == '9': print("Is Perfect?", is_perfect_number(val))
            
        # enter two numbers for GCD and LCM
        elif choice in ['7', '8']:
            num1 = int(input("First number: "))
            num2 = int(input("Second number: "))
            if choice == '7': print("GCD is:", gcd(num1, num2))
            elif choice == '8': print("LCM is:", lcm(num1, num2))
        else:
            print("Not a valid option, try again.")

# Start the program
math_menu()