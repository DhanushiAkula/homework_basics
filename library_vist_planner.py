# Library Visit Planner

print("=== Library Visit Planner ===")
print("Answer 3 quick questions and I will suggest your library plan!\n")

day = input("What day is it? (Monday to Sunday): ").strip().capitalize()
weather = input("What is the weather? (sunny / rainy / cloudy): ").strip().lower()
book = input("Do you need to return a book? (yes / no): ").strip().lower()

print()
print(f"=== Your Library Plan for {day} ===")
print("-" * 40)

# Topic 1 -- if-elif-else: classify the day
if day in ("Saturday", "Sunday"):
    print("Day type    : Weekend - Great time to visit the library!")
elif day == "Monday":
    print("Day type    : Start the week by borrowing a new book.")
elif day == "Friday":
    print("Day type    : Return any borrowed books before the weekend.")
elif day in ("Tuesday", "Wednesday", "Thursday"):
    print("Day type    : Good day for reading after school.")
else:
    print("Day type    : Day not recognised. Please check the spelling.")

# Topic 2 -- AND operator
if weather == "sunny" and book == "yes":
    print("Library Tip : Return your book and enjoy a walk to the library.")

# Topic 3 -- OR operator
if weather == "rainy" or weather == "cloudy":
    print("Weather Tip : Take an umbrella when visiting the library.")

# Topic 4 -- NOT operator
if not (book == "yes"):
    print("Reminder    : No book to return. You can borrow a new one!")

# Topic 5 -- Combining AND + OR + NOT
if weather == "rainy" and not (book == "yes"):
    print("Best Plan   : Stay inside, read a book at home, and visit later.")
elif weather == "sunny" and book == "yes" and not (day in ("Saturday", "Sunday")):
    print("Best Plan   : Return your book after school and borrow another.")
elif day in ("Saturday", "Sunday") and weather == "sunny":
    print("Best Plan   : Perfect day to spend time at the library.")
else:
    print("Best Plan   : Read a few pages today and enjoy your book!")

print()
print("Have a great time reading!")