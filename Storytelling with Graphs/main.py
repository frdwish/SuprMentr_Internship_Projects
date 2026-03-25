import matplotlib.pyplot as plt

# Sample data
subjects = ["Math", "Science", "English", "History", "Computer"]
marks = [85, 90, 75, 70, 95]

# Bar Chart
plt.figure()
plt.bar(subjects, marks)
plt.title("Marks in Different Subjects")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.show()

# Pie Chart
plt.figure()
plt.pie(marks, labels=subjects, autopct="%1.1f%%")
plt.title("Marks Distribution")
plt.show()

# Histogram
plt.figure()
plt.hist(marks, bins=5)
plt.title("Marks Distribution Histogram")
plt.xlabel("Marks Range")
plt.ylabel("Frequency")
plt.show()