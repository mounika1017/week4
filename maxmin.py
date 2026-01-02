a=int(input("enter a"))
b=int(input("enter b"))
c=int(input("enter c"))
if(a>=b) and (a>=c):
    print("max:",a)
elif b>=a and b>=c:
    print("max:",b)
else:
    print("max:",c)
if(a<=b) and (a<=c):
    print("min:",a)
elif b<=a and b<=c:
    print("min:",b)
else:
    print("min:",c)
    