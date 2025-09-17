print("Please enter the following information so I can sell it for a profit!\n")

first_name = str(input("First name: "))
last_name = str(input("Last name: "))
grade = int(input("Grade (9-12): "))
student_id = int(input("Student ID: "))
login = str(input("Login: "))
average = float(input("Average: "))

print(f"Your information:\nLogin: {login}\nID: {student_id}\nName: {last_name}, {first_name}\nAverage: {average} %\nGrade: {grade}")
