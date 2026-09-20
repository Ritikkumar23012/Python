# # Determine if two number are co-prime -----> HCf of two number is 1
n = int(input("Enter 1st number: "))
n1 = int(input("Enter 2nd number: "))
i=1
GCD = 1
while i<=n and i<=n1:
    if n%i==0 and n1%i==0:
        GCD = i
    i+=1
if GCD == 1:
    print(f"{n} and {n1} is co-prime number")
else:
    print(f"{n} and {n1} is not co-prime number")
