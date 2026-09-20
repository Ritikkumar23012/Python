# Find the nth fibonacci number
n = int(input("Enter Number: "))
x=1
y=0
for i in range(1,n+1):
    s = x + y
    print(s,"\t", end=" ")
    x=y
    y=s
print("\nNth fibonacci number is ",s)