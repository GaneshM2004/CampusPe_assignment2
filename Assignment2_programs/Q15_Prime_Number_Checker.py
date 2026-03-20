#check if number is prime or not
number = int(input("Enter a number: "))
is_prime = True

if number <= 1:
    is_prime = False
elif number == 2:
    is_prime = True
else:
    # check for factors from 2 to number-1
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break

if is_prime:
    print(f"{number} is a PRIME number")
else:
    print(f"{number} is NOT a prime number")

# find all prime in range
start = int(input("\nEnter start range: "))
end = int(input("Enter end range: "))

prime_list = []

for length in range(start, end + 1):
    if length > 1:
        # Check if length is prime
        for i in range(2, int(length**0.5) + 1):
            if length % i == 0:
                break
        else:
            # It runs only if the loop finishes without 'break' statement
            prime_list.append(str(length))

#output the result using join to convert list to string with comma inbetween them
print(f"Prime numbers: {', '.join(prime_list)}")