message = input("Enter your message: ")

spam_words = ["win", "free", "offer", "money"]

is_spam = False

for word in spam_words:
    if word in message.lower():
        is_spam = True
        break

if is_spam:
    print("This message is Spam")
else:
    print("This message is Not Spam")