from math import pi

r = float(input("Enter radius of orbit(million km): "))
v = float(input("Enter orbital speed(km/s): "))

r = r*1000000
year = 2 * pi * r/v

year = year / (60*60*24) 
print(round(year))
