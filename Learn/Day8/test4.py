order_dict = dict()

data = input('Enter number of bread & milk separated by ":" ')
temp = data.split(':')
order_dict[temp[0]] = int(temp[1])


key = list(order_dict.keys())[0]  
value = order_dict[key]

print('Bread: {} grams, Milk: {} litres'.format(value * 400, value * 0.5))