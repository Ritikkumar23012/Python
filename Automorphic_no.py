# Check a number is Automorphic or not ----> Square of a number end with a same number
n = int(input("Enter Number: "))
num = n*n
if num % (10**len(str(n))) == n:
    print("Number is Automorphic")
else:
    print("Number is Not Automorphic")