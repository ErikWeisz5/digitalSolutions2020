recl1 =int(input('enter first rectangle length:'))
recw1 =int(input('enter first rectangle width:'))
recw2 =int(input('enter second rectangle length:'))
recl2 =int(input('enter second rectangle width:'))
u1 = input('input your units:')
r1 = recl1 * recw1
r2 = recl2 * recw2

if r1 > r2:
    print('rectangle one is larger')
    print(r1, u1)

elif r1 < r2:
    print('rectangle two is larger')
    print(r2, u1)

