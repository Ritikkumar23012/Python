# Check if a number is a armstrong number or not
n = int(input("Enter number: "))
sum=0
temp = n
while temp > 0:
    rem = temp%10
    sum = sum + (rem*rem*rem)
    temp = temp//10
if n==sum:
    print(f"{n} is Armstrong number")
else:
    print(f"{n} is not Armstrong number")