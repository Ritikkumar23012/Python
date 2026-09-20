# Check if a number is a pronic number -----> Product of two consecutive integer
n = int(input("Enter number: "))
i=0
while i * (i + 1) <= n:
    if i*(i+1) == n:
        print(n," is a Pronic Number ")
        break
    i+=1
else:
    print(f"{n} is not pronic number")
