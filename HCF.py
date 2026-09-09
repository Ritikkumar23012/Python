# Calculate the greatest common divisor of two number
n = int(input("Enter 1st number: "))
n1 = int(input("Enter 2nd number"))
i=1
gcd=1
while i<=n and i<=n1:
    if n%i==0 and n1%i==0:
        gcd = i
    i+=1
print("Greatest Common Divisor is ", gcd)
