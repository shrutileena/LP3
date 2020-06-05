import datetime

yr = int(input("Enter year: "))
mon = int(input("Enter month: "))
day = int(input("Enter day: "))

x = datetime.datetime(yr,mon,day)

print(int(x.strftime("%W"))+1)
