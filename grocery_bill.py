print("=== Grocery Billing Queue ===\n")
customers_served = 0
total_sales = 0
low_items = 0
medium_items = 0
high_items = 0
serving = True
while serving:                         
    name = input("Enter customer name: ")
    item_count = int(input(f"Hello {name}! How many grocery items? "))
    if item_count <= 0:
        print("Invalid number of items. Please enter a positive number.\n")
        continue
    customer_total = 0
    item_no = 1
    while item_no <= item_count:       
        item = input(f"Enter item {item_no} name: ")
        price = float(input(f"Enter price of {item}: "))
        if price <= 0:
            print("Invalid price. Please enter a positive price.\n")
            continue
        customer_total += price
        if price < 10:
            low_items += 1
        elif price <= 50:
            medium_items += 1
        else:
            high_items += 1
        item_no += 1
    print(f"\nBill for {name}: {customer_total:.2f}")
    print("Transaction complete!\n")
    customers_served += 1
    total_sales += customer_total
    again = input("Next customer? (yes/no): ").strip().lower()
    if again != "yes":
        serving = False
print("\n=== Final Price Category Report ===")
for category in range(1, 4):            
    if category == 1:
        name = "Low Price (< 10)"
        total = low_items
    elif category == 2:
        name = "Medium Price (10 - 50)"
        total = medium_items
    else:
        name = "High Price (> 50)"
        total = high_items
    if total > 0:
        print(f"  {name} : {total} item(s)", end=" ")
        for item in range(total):       # inner for - one symbol per item
            print("=", end="")
        print()
print(f"\nCustomers served : {customers_served}")
print(f"Total sales      : {total_sales:.2f}")
print("Grocery billing session closed. Goodbye!")
    