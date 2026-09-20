# Check if number is a Neon number  ---->  Square ke Digit ka sum = number itself
n = int(input("Enter number: "))
square = n*n
sum = 0
temp = square
while temp > 0:
    rem = temp % 10
    sum = sum + rem
    temp = temp//10
if sum == n:
    print(f"{n} is Neon number")
else:
    print(f"{n} is not Neon number" )
