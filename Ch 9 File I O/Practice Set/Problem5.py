import re
words = ["Donkey", "Monkey", "Bad", "Stupid"]

with open("text.txt", "r") as f:
    content = f.read()

for word in words:
    content = re.sub(word, "$"*len(word), content, flags=re.IGNORECASE)

with open("text.txt", "w") as f:
    f.write(content)
