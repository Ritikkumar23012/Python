# Input date in MMDDYYYY format and print the month name, date, year
'''n = input("Enter Date in format MMDDYYYY :--- ")
month = n[0:2]
date = n[2:4]
year = n[4:8]
if month == '01':
    month_name = "January"
elif month == '02':
    month_name = "Feburary"
elif month == '03':
    month_name = "March"
elif month == '04':
    month_name = "April"
elif month == '05':
    month_name = "May"
elif month == '06':
    month_name = "June"
elif month == '07':
    month_name = "July"
elif month == '08':
    month_name = "August"
elif month == '09':
    month_name = "September"
elif month == '10':
    month_name = "October"
elif month == '11':
    month_name = "November"
elif month == '12':
    month_name = "December"
else:
    print("Invalid Month number")    
print("Month is ", month_name)
print("Date is ", date)
print("Year is ", year)'''

n = int(input("Enter Date in format (DDMMYYYY): "))
y = n % 10000
n = n // 10000
m = n % 100
d = n // 100
print(f"Date: {d}, Month: {m}, Year: {y}")
