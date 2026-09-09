# Find the least common multiple of two number
n = int(input("Enter 1st number: "))
n1 = int(input("Enter 2nd number"))
i=1
while True:
    if i%n==0 and i%n1==0:
        LCM = i
        break
    i+=1
print(f"LCM of {n} and {n1} is {LCM}")