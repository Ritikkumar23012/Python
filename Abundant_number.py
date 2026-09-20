# Check if a number is abundant number or not ----> Sum of proper number is greater than the number
n = int(input("Enter number: "))
sum = 0
for i in range(1,n):
    if n%i==0:
        sum = sum + i
if sum == n:    # sum == n (perpect number)               
    print(f"{n} is perfect number")
elif sum > n:
    print(f"{n} is Abundant number")
else:
    print(f"{n} is not Abundant number")