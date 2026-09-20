# Find the sum of Proper divisor of a number
n = int(input("Enter number: "))
i=1 
sum=0
while i < n:
    if n%i==0:
        sum = sum + i
    i+=1
print(f"Sum of Proper divisor of {n} is {sum}")