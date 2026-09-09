# Find reverse of a digit of a number
n = int(input("Enter number: "))
rev = 0
temp = n
while temp > 0:
    rem = temp%10
    rev = rev * 10 + rem
    temp = temp//10
print(f"Reverse of {n} is {rev}")