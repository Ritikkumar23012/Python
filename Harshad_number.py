# Determine if a number is a Harshad number. It is also called Niven Number ----> Number which is Divisible by the sum of its digits
n = int(input("Enter number: "))
temp = n
sum = 0
while temp>0:
    rem = temp%10
    sum = sum + rem
    temp = temp//10
if n % sum==0:
    print(f"{n} is a Harshad Number")
else:
    print(f"{n} is not Harshad number")
