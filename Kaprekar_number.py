# Check if a number is a kaprekar number or not  -----> Square of a number and split it into two part and than sum == number  
n = int(input("Enter number: "))
square = n*n
temp = n
count = 0
while temp > 0:
    count+=1
    temp = temp//10
divisor = 10 ** count
right = square % divisor
left = square // divisor
sum = left + right 
if sum == n:
    print("Number is Kaprekar number")
else:
    print("Number is not kaprekar number")