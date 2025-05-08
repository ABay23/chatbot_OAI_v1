# 
'''
This is a special comment updated on the IDE

Testing mat:
- You have $50
- You buy an item $15
- Add 3% tax
- Return total printed.
'''

# bank = 50
# item = 15
# tax = 3 / 100

# def purchasing(money: int, price: int, tax: float)-> float:
#     total = (price + (price * tax))
#     money = money - total
#     print(f'Your total after purchasin is {total}, you have {money} in your account.')
    
# purchasing(bank, item, tax)

# '''This is a format string method'''
# name = 'Alejandro'
# lastname = 'Doe'
# sentence = 'Hi {}'
# print(sentence.format(name, lastname))

# '''Pla,ying with sets'''

# my_set = {3, 4, 5, 5, 3, 7, 9}
# my_set.discard(3)

# my_set.update([16, 2])

# my_set.add('one')

# print(my_set)

'''Loops and while loop test on continue'''
i = 0
while i < 6:
    # print(i)
    i += 1
    
    if i == 3:
        continue
    print(i)
    # if i == 4:
        # break
else:
    print('i is now larger or equal to 6')
    
'''Dictionaries'''
my_vehicle = {
    "model": "Ford",
    "make": "Explorer",
    "year": 2018,
    "mileage": 40000
}
for key, value in my_vehicle.items():
    print(f'The key: {key} and the value: {value},')