print("====== DAILY ACTIVITY PLANNER ======")

temperature = int(input("Enter today's temperature in Celsius: "))

if temperature < 20:
    print("It is cold today.")
    activity = "Read a book indoors"
else:
    print("It is warm today.")
    activity = "Go for a walk outside"

is_raining = input("Is it raining today? (yes/no): ")

if is_raining == "yes":
    print("Better stay indoors.")
    activity = "Watch a movie"

homework_time = int(input("How much homework do you have? "))

if homework_time > 2:
    print("You have a lot of homework.")
    homework_plan = "Finish homework first"
else:
    print("You have less homework.")
    homework_plan = "Complete homework and relax"

free_time = int(input("How many hours of free time do you have? "))
if free_time >= 2:
    fun_activity = "Play games or sports"
else:
    fun_activity = "Read a story or listen to music"

print("")
print("====== DAILY ACTIVITY PLAN ======")
print("Temperature:", temperature, "°C")
print("Raining:", is_raining)
print("Suggested Activity:", activity)
print("Homework Plan:", homework_plan)
print("Free Time:", free_time, "hours")
print("Fun Activity:", fun_activity)
print("=================================")