year =int(input("Enter a year for leap year check:"))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("{} is leap year".format(year))
else:
    print("{} is not leap year".format(year))
