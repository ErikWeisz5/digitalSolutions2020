m = int(input('Number of males?'))
f = int(input('Number of females?'))

t = m + f
mp = m / t
fp = f /t

print("%.0f%%" % (100 * mp))

print("%.0f%%" % (100 * fp))