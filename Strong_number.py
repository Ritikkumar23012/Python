#Check if a number is strong number or not ---> sum of factorial of a digit = number itself
n = int(input("Enter number:"))
temp = n
sum = 0
while temp > 0:
    r = temp % 10
    fact = 1
    for i in range(1,r+1):
        fact = fact*i
    
    sum = sum + fact
    temp = temp // 10
if sum == n:
    print("Number is Strong number")
else:
    print("Number is not Strong number")