# Enter seconds and convert it to minute and hour
n = int(input("Enter Seconds: "))
hour = n//3600
remaining = n%3600
minute = remaining//60
n = remaining%60
print(f"Hours = {hour} : Minute = {minute} : Second = {n}") 
