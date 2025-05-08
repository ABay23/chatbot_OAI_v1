# 
'''
This is a special comment updated on the IDE

Testing mat:
- You have $50
- You buy an item $15
- Add 3% tax
- Return total printed.
'''

bank = 50
item = 15
tax = 3 / 100

def purchasing(money: int, price: int, tax: float)-> float:
    total = (price + (price * tax))
    money = money - total
    print(f'Your total after purchasin is {total}, you have {money} in your account.')
    
purchasing(bank, item, tax)

'''This is a format string method'''
name = 'Alejandro'
sentence = 'Hi {}'
print(sentence.format(name))