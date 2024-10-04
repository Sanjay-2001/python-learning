#letter template

name = input("Enter name : ")

letter = """
Dear <|Name|>,
    You are selected!
<|Date|>
"""

print(letter.replace("<|Name|>","Sanjay").replace("<|Date|>","28 September")) #.replace chaining

