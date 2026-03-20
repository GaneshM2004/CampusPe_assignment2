#enter birth date
print("Enter your birth details:")
birthday = int(input("What day were you born? (1-31): "))
birthmonth = int(input("What month? (1-12): "))
birthyear = int(input("What year?: "))

#current date
curday = 23
curmonth = 2
curyear = 2026

# age in years
ageyears = curyear - birthyear
if (curmonth < birthmonth) or (curmonth == birthmonth and curday < birthday):
    ageyears = ageyears - 1
#age in months
agemonths = (ageyears * 12) + (curmonth - birthmonth)
if curday < birthday:
    agemonths = agemonths - 1

#age in days
totaldays = int(ageyears * 365.25) + ((curmonth - birthmonth) * 30) + (curday - birthday)
#age in hours and minutes
agehours = totaldays * 24
ageminutes = agehours * 60

#years left to reach 100
years100 = 100 - ageyears

print(ageyears, "years old")
print(agemonths, "months old")
print(totaldays, "days old")
print(agehours, "hours old")
print(ageminutes, "minutes old")
print(years100, "years left to reach 100")
