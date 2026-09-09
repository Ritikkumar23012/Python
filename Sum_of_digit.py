# Calculate the sum of digit of a number
n = int(input("Enter number: "))
sum=0
i=1
while n>0:
    rem = n%10
    sum = sum + i
    n = n//10
    i+=1
print("Sum of a digit is ", sum)
