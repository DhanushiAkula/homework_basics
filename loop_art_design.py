print("===================================")
print("        LOOP ART DESIGNER")
print("===================================")
rows = int(input("Enter the number of rows: "))
print("\n1. Floyd's Triangle")
number = 1
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(number, end=" ")
        number = number + 1
    print()
print("\n2. Diamond Pattern")
if rows % 2 == 0:
    halfdiamondrow = int(rows / 2)
else:
    halfdiamondrow = int(rows / 2) + 1
space = halfdiamondrow - 1
for i in range(1, halfdiamondrow + 1):
    for j in range(1, space + 1):
        print(end=" ")
    space = space - 1
    num = 1
    for j in range(2 * i - 1):
        print(num, end="")
        num = num + 1
    print()
space = 1
for i in range(1, halfdiamondrow):
    for j in range(1, space + 1):
        print(end=" ")
    space = space + 1
    num = 1
    for j in range(1, 2 * (halfdiamondrow - i)):
        print(num, end="")
        num = num + 1
    print()
print("\n===================================")
print("        END OF LOOP ART")
print("===================================")