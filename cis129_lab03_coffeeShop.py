#james feddick cis129 module 3 lab

#establishing prices and title
print('My Coffee and Muffin Shop')
Coffees_price = int(5.00)
Muffins_price = int(4.00)
Espresso_price = int(7.00)
Cookie_price = int(4.00)

#gaining input for ammount of coffees and muffins
Coffees = int(input('Number of coffees bought?'))
print(Coffees)
Muffins = int(input('Number of muffins bought?'))
print(Muffins)
Espresso = int(input('Number of Espressos?'))
print(Espresso)
Cookies = int(input('Number of Cookies'))
print(Cookies)

#caculating subtotals
Coffee_total = Coffees_price * Coffees
Muffin_total = Muffins_price * Muffins
Espresso_total = Espresso_price * Espresso
Cookie_total = Cookie_price * Cookies

#tax
taxrate = 0.06
subtotal = Coffee_total + Muffin_total + Espresso_total + Cookie_total
tax = subtotal * taxrate

#total
total = subtotal + tax

#output
print('My Coffee and Muffin Shop Receipt')
print(f'{Coffees} Coffees at ${Coffees_price} each: ${Coffee_total}')
print(f'{Muffins} Muffins at ${Muffins_price} each: ${Muffin_total}')
print(f'{Espresso} Espressos at ${Espresso_price} each: ${Espresso_total}')
print(f'{Cookies} Cookies at ${Cookie_price} each: ${Cookie_total}')
print(f'6% tax: {tax:.2f}')
print('---------------------')
print(f'Total: ${total:.2f}')

