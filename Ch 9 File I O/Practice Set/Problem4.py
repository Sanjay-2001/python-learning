import re

word = "Donkey"

with open("text.txt") as f:
    content = f.read()

# contentNew = content.replace(word, "######")
contentNew = re.sub(word, "######", content, flags=re.IGNORECASE)

with open("text.txt", "w") as f:
    f.write(contentNew)
