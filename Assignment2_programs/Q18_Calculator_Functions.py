# all functions for calculator
def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b): return a / b if b != 0 else "cannot divide by zero"
def modulus(a, b): return a % b if b != 0 else "cannot modulus by zero"
def power(a, b): return a ** b

def calculator():
    while True:
        print("\n1.Add 2.Sub 3.Mul 4.Div 5.Mod 6.Pow 7.Exit")
        choice = input("Enter choice: ")
        if choice == '7': break
        if choice in ('1', '2', '3', '4', '5', '6'):
            try:
                n1 = float(input("Num 1: ")); n2 = float(input("Num 2: "))
                #using a dictionary to map key to function
                ops = {'1':add, '2':subtract, '3':multiply, '4':divide, '5':modulus, '6':power}
                print("Result:", ops[choice](n1, n2))
            except ValueError: print("Invalid input")
        else: print("Invalid choice")
#calling the calculator function to run the calculator
calculator()
