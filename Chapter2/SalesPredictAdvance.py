i = "y"
total = 0
while i !="n":
        s = int(input("input price for your sale items:"))
        total=total+s
        i = input("Do you wish to continue, type n for No")
t = total * 0.7
print("$",total +t)
