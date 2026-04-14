pos = ["good", "great", "amazing"]
neg = ["bad", "worst", "boring"]

review = input("Enter review: ").lower()

score = 0

for w in pos:
    if w in review:
        score += 1

for w in neg:
    if w in review:
        score -= 1

if score > 0:
    print("Positive")
elif score < 0:
    print("Negative")
else:
    print("Neutral")