# filling letter template

letter = '''
Dear <|name|>
You are selected!!
<|date|>
'''

name = input("Enter your name: ")

date = input("Enter the date: ")

print(letter.replace("<|name|>", name).replace("<|date|>", date))
