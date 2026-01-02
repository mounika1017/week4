n=int(input("enter n value"))
even=0
odd=0
for i in range(2,n+1,2):
        print(i,end=" ")
        even=even+1
print("\n no of even numbers =",even)
for i in range(1,n+1,2):
        print(i,end=" ")
        odd=odd+1
print("\n no of odd numbers =",odd)

