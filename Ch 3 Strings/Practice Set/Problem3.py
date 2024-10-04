#detect double space

text = "hello  ji how are  you"

print(text.find("  "))

#replace with single space

print(text.replace("  "," ")) #strings are immutable which means that you cannot change them by running functions on thm