import string

text = input("Enter text: ").lower()

for c in string.punctuation:
    text = text.replace(c, "")

words = text.split()

stopwords = ["is", "the", "and"]
keywords = [w for w in words if w not in stopwords]

print("Keywords:", keywords)