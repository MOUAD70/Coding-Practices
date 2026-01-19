import math

def century(year):
    return year / 100 if year % 100 == 0 else math.ceil(year / 100)

print(century(1969))