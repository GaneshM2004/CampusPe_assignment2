print("Restaurant Bill Splitter")
print("=====================")
# taking valid input total bill
while True:
	try:
		subtotal = float(input("Enter total bill: ").strip())
		if subtotal < 0:
			print("Bill cant be negative")
			continue
		break
	except ValueError:
		print("invalid number")

# taking valid input number of people
while True:
	try:
		num= int(input("Enter number of people: ").strip())
		if num <= 0:
			print("No. of people should be at least 1")
			continue
		break
	except ValueError:
		print("invalid number")

# taking valid input tax percentage
while True:
	try:
		taxpercentage= float(input("Enter tax percentage: ").strip())
		if taxpercentage < 0:
			print("Tax percentage cannot be negative")
			continue
		break
	except ValueError:
		print("invalid number")

# taking valid input tip percentage
while True:
	try:
		tippercentage= float(input("Enter tip percentage: ").strip())
		if tippercentage < 0:
			print("Tip percentage cannot be negative.")
			continue
		break
	except ValueError:
		print("invalid number")

print("=======================")
# Calculations
taxamt = subtotal * (taxpercentage / 100.0)
billaftertax= subtotal + taxamt
tip= subtotal * (tippercentage / 100.0)
total = billaftertax + tip
perperson = total / num

#displaying output by rounding to 2 decimal places
print("\nBill Breakdown")
print("=======================")
print("Subtotal: ₹",round(subtotal,2))
print("Tax amount: ₹",round(taxamt,2))
print("Bill after tax: ₹",round(billaftertax,2))
print("Tip amount: ₹",round(tip,2))
print("Total bill: ₹",round(total,2))
print("Amount per person: ₹",round(perperson,2))
print("=======================")
