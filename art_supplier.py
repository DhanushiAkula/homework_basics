def greet_customer():
    print("Welcome to the Art Supplies Store!")
    print("We have everything you need for your creativity.")
greet_customer()
price_per_item = float(input("Enter the price of the art supply: "))
quantity = int(input("Enter the quantity: "))
def calculate_total(price, quantity):
    total = price * quantity
    return total
total_cost = calculate_total(price_per_item, quantity)
rounded_total = round(total_cost, 2)
print("Total Cost:", rounded_total)
amount_paid = float(input("Enter the amount paid by the customer: "))
def calculate_change(paid, total):
    change = paid - total
    return change
change_due = calculate_change(amount_paid, rounded_total)
rounded_change = round(change_due, 2)
def thank_you_message(quantity):
    if quantity >= 5:
        return "Wow, big order! Thanks for shopping with us!"
    else:
        return "Thanks for shopping at the Art Supplies Store!"
closing_message = thank_you_message(quantity)
print("")
print("===== ART SUPPLIES RECEIPT =====")
print("Price Per Item:", price_per_item)
print("Quantity:", quantity)
print("Total Cost:", rounded_total)
print("Amount Paid:", amount_paid)
print("Change Due:", rounded_change)
print(closing_message)
print("================================")