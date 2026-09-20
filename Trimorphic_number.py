# Check if number is Trimorphic number ----> Cube of a number ends with the same number
n = int(input("Enter number: "))
cube = n*n*n
if cube % (10 ** len(str(n))) == n:
    print("Trimorphic Number")
else:
    print("Not Trimorphic number")
