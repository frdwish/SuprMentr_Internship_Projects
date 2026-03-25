import string

stopwords = ["is", "the", "and", "in", "to", "of"]

text = input("Enter a sentence: ")

# Lowercase
text = text.lower()

# Remove punctuation
for char in string.punctuation:
    text = text.replace(char, "")

# Remove stopwords
words = text.split()
cleaned = [word for word in words if word not in stopwords]

print("Cleaned text:", " ".join(cleaned))