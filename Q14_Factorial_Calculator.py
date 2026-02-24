num = int(input("Enter a number: "))

if num < 0:
    print("Factorial cannot be negative")
elif num == 0:
    print("0! = 1")
else:
    factorial = 1
    steps = ""
    # Loop with decreasing range
    for i in range(num, 0, -1):
        factorial *= i
        
        # steps string to show like 5 x 4 x 3 x 2 x 1
        if i == 1:
            steps += str(i)
        else:
            steps += str(i) + " × "
    #output the result
    print(f"{num}! = {steps} = {factorial}")
