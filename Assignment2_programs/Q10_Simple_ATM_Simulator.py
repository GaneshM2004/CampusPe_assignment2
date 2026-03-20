print("ATM SIMULATOR")
print("=" * 30)

# Initial balance
initialbal = 10000

def check_balance(balance):
    return balance

def deposit(balance, amount):
    if amount <= 0:
        return balance, "Invalid deposit amount"
    balance += amount
    return balance, "Deposit successfull"

def withdraw(balance, amount):
    MIN_BALANCE = 500
    if amount <= 0:
        return balance, "invalid withdrawal amount"
    # to make sure minimum balance remains
    if balance - amount < MIN_BALANCE:
        return balance, "minimum balance of ₹500 must be there"
    balance -= amount
    return balance, "Withdrawal successfull"

balance = initialbal
while True:
    print("\n1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
    choice = input("Enter choice: ")

    if choice == '1':
        print("Current balance: ₹",round(balance,2))

    elif choice == '2':
        try:
           amt= int(input("Enter amount to deposit: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        balance, msg = deposit(balance, amt)
        print(msg)
        print("New balance: ₹",round(balance,2))

    elif choice == '3':  
        try:
            amt= int(input("Enter amount to withdraw: "))
        except ValueError:
            print("Please enter a valid number")
            continue
        balance, msg = withdraw(balance, amt)
        print(msg)
        print("New balance: ₹",round(balance,2))

    elif choice == '4':
        print("Exiting...")
        break

    else:
        print("Please select a valid option")
