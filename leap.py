import datetime
current = datetime.datetime.now().year
final = int(input("Enter final year: "))
print("Leap Years: ")
for year in range(current, final+1):
    if (year%4==0 and year%100!=0) or (year%400==0):
        print(year)
    