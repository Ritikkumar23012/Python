# Convert a binary number to decimal
n = int(input("Enter Binary Number: "))
temp = n
DecNum = 0
pow = 0
while temp > 0:
    rem = temp%10
    DecNum = DecNum + (rem * (2**pow))
    temp = temp//10
    pow+=1
print(f"Decimal of {n} is {DecNum}")