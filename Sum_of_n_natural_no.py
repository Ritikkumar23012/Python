# Calculate the sum of first n natural number
n = int(input("Enter number: "))
sum = 0
for i in range(1,n+1):
    sum = sum + i
print(f"Sum of {n}th Natural number is {sum}")
