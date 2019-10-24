price = input('enter the price you will pay for this item:')
price = float(price)
if price >= 100 :
    tax = 0.07
    print(price + (price * tax))
else:
    tax = 0
    print(price + (price * tax))

country = input('Where do you live?')
if country == 'canada' or country == 'usa' :
    print ('welcome to business!')

elif country == 'europe':
    print ('fuck you')

else :
    print ('Go and fuck yourself!')

# GPA example
