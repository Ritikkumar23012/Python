# Determine if a number is an Evil number. ---->  Binary Representation contain Even number of 1's.
n = int(input("Enter number: "))
temp = n
count = 0
while temp>0:
    r = temp%2
    if r == 1:
        count+=1
    temp=temp//2
if count%2==0:
    print(f"{n} is an Evil number")
else:
    print(f"{n} is Odious number")      # Odious Number ------> Binary Reoresentation contain Odd number of 1's.
