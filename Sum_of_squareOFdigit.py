# Calculate the sum of the square of the digits of a number
n = int(input("Enter number: "))
temp = n
sum = 0
while temp > 0:
    rem = temp % 10
    sum = sum + rem*rem
    temp = temp//10
print(f"Sum of Square of digit of {n} is {sum}")
