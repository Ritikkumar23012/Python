# Check if a number is palindrome or not
n = int(input("Enter number: "))
rev=0
temp = n
while temp>0:
    rem = temp%10
    rev = rev * 10 + rem
    temp = temp//10
if n==rev:
    print(f"{n} is Palindrome Number")
else:
    print(f"{n} is not palindrome number")