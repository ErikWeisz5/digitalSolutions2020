month =int(input('input your month:'))

if  1 <= month <= 3:
    print('first quarter')
elif  4 <= month <= 6:
    print('second quarter')
elif 7 <= month <= 9:
    print('third quarter')
elif 10 <= month <= 12:
    print('fourth quarter')
else:
    print('ERROR 404 MONTH NOT FOUND ')