students = {}

# Taking input for 5 students
for i in range(5):
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    students[name] = marks

# Finding topper
topper = max(students, key=students.get)
highest_marks = students[topper]

# Calculating class average
total = sum(students.values())
average = total / len(students)

print("\nStudent Grades:")
for name, marks in students.items():
    if marks >= 90:
        grade = "A"
    elif marks >= 75:
        grade = "B"
    elif marks >= 60:
        grade = "C"
    else:
        grade = "D"
    
    print(name, "-", marks, "Grade:", grade)

print("\nTopper:", topper, "with", highest_marks, "marks")
print("Class Average:", round(average, 2))