
total_homework = 4
original_count = total_homework
print("===== HOMEWORK COMPLETION TRACKER =====")
print(f"You have {original_count} homework tasks to complete today!\n")
completed_count = 0
homework_num = 1
while homework_num <= total_homework:
    if homework_num == 1:
        next_homework = "Math Homework"
    elif homework_num == 2:
        next_homework = "Science Homework"
    elif homework_num == 3:
        next_homework = "English Homework"
    else:
        next_homework = "Computer Homework"
    answer = input(f"Have you completed {next_homework}? (yes/no): ")
    if answer == "yes":
        completed_count += 1
        homework_num += 1
        print("Great! Homework completed.")
    else:
        print("Please finish it and check again.")
    print("Homework remaining:", total_homework - completed_count)
    print()
print("===== ALL HOMEWORK COMPLETED! =====")
print("Excellent! You finished all your homework.\n")
print("\n===== HOMEWORK SUMMARY =====")
print("Homework Assigned:", original_count)
print("Homework Completed:", completed_count)
print("Homework Remaining:", total_homework - completed_count)
print("============================")