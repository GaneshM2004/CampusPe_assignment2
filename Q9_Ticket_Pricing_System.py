print("Ticket Pricing System")
print("=" * 40)

#function to calculate base price based on age
def base_price(age):
    age =int(age)
    if age<3:
        return 0
    if 3<=age<=12:
        return 150
    if 13<=age<=59:
        return 300
    return 200

#function to calculate discount percentage based on day of week
def day_discount(day_name):
    d = day_name.strip().lower()
    if d in ["friday","saturday","sunday"]:
        return 20.0
    return 0.0

#function to calculate discount amount, price after discount and total amount
def totals(base_price, discount, numtickets):
    discountamt= base_price*(discount/100.0)
    price_after_discount = base_price-discountamt
    totalamt = price_after_discount*numtickets
    return round(discountamt, 2), round(price_after_discount, 2), round(totalamt, 2)

#taking inputs
age= int(input("Enter age of the ticketholder: "))
day = input("Enter day of week: ")
numtickets = int(input("Enter number of tickets: "))

#calling the functions to calculate the base price, discount and total amount
baseprice = base_price(age)
discount = day_discount(day)
discountamt, price_after, total = totals(baseprice, discount, numtickets)

#displaying output
print("=" * 40)
print("\n--- Ticket Pricing---")
print("Base price per ticket: ₹",round(baseprice,2))
print("Discount per ticket: ₹{discountamt:.2f} ({discount:.2f}%)")
print("Price after discount (per ticket): ₹",round(price_after,2))
print("Number of tickets: ",numtickets)
print("Total amount: ₹",round(total,2))
print("=" * 40)
