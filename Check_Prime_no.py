# Check Prime Determine if a number is prime or not
n = int(input("Enter number: "))
prime = 1
if n <=1:
    print(f"{n} is not prime number")
else:
    for i in range(2,n):
        if n%i==0:
            prime=0
            break
    if(prime):
        print(f"{n} is prime number")
    else:
        print(f"{n} is not prime number")
