#taking two inputs from the user with variables a and b
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
print("Results:")
#Mathematical Opeerations
print(f"Addition: {a} + {b} = {a+b}")
print(f"Subtraction: {a} - {b} = {a-b}")
print(f"Multiplication: {a} * {b} = {a*b}")
print(f"Division: {a} / {b} = {round(a/b, 2)}") #Rounded to 2 decimal places
print(f"Modulus: {a} % {b} = {a%b}")
print(f"Exponent: {a} ^ {b} = {a**b}")