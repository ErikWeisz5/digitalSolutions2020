m = float(input('input your mass:'))

w = m*9.8
print(w,"Newtones")

if w > 500:
    print('Too Heavy')
elif w < 100:
    print('Too light')


