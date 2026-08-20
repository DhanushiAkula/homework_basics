def total_calc(bill_amount, tip_perc):
    total = bill_amount * (1 + 0.01 * tip_perc)
    total = round(total, 2)
    print("Please pay $", total)
total_calc(150, 20)
def seating_arrangements(people):
    '''This is a recursive function to find the number of seating arrangements'''
    if people == 0 or people == 1:
        return 1
    return people * seating_arrangements(people - 1)
print(seating_arrangements.__doc__)
print("Seating arrangements for 1 person:", seating_arrangements(1))
print("Seating arrangements for 2 people:", seating_arrangements(2))
print("Seating arrangements for 3 people:", seating_arrangements(3))
print("Seating arrangements for 4 people:", seating_arrangements(4))
print("Seating arrangements for 5 people:", seating_arrangements(5))