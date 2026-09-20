# Convert a number to binary representation
n = int(input("Enter decimal number: "))
BinNum = 0
temp = n
pow = 0
while temp > 0:
    rem = temp%2
    BinNum = BinNum + (rem * (10**pow))
    temp = temp//2
    pow += 1
print(f"Binary of {n} is {BinNum}")
