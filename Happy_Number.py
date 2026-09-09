# Check if a number is a happy number --> Digit ke square ka sum equal to 1
n = int(input("Enter number: "))
temp = n
while temp != 1 and temp != 4:
    sum = 0
    while temp > 0:
        rem = temp%10
        sum = sum + (rem*rem)
        temp = temp//10
    temp = sum
if temp == 1:
    print(f"{n} is a happy number")
else:
    print(f"{n} is not a happy number")
