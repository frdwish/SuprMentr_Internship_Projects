# Store student data
students = {
    "Aman": 85,
    "Riya": 92,
    "Karan": 76,
    "Sneha": 88,
    "Rahul": 69
}

# Find topper
topper = max(students, key=students.get)
highest_marks = students[topper]

# Calculate class average
total_marks = sum(students.values())
average = total_marks / len(students)

# Assign grades
print("Student Grades:")
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