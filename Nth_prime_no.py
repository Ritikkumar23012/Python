# Find the Nth Prime number
n = int(input("Enter Number: "))
count = 0
num = 2
while count < n:
    prime = 1 
    for i in range(2,num):
        if num%i==0:
            prime=0
            break
    if prime:
        print(num, end=" ")
        count+=1
        if count == n:
            print("\nLast Prime number is ",num)
    num+=1