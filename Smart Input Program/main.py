name = input("Enter your name: ")
age = int(input("Enter your age: "))
hobby = input("Enter your hobby: ")

# Age categorization
if age < 13:
    category = "Child"
elif age < 20:
    category = "Teenager"
elif age < 60:
    category = "Adult"
else:
    category = "Senior"

# Personalized message
print("\nHello", name + "!")
print("You are a", category + ".")
print("It's great that you enjoy", hobby + "!")