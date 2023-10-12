# Leap year
"""
year %4==0&
year %100!==0/
year %400==0

"""


def isleapyear(year):
  if(year %4 == 0 and year % 100 !=0) or year %400 == 0:
    return True
  else:
    return False


year = 2012

if isleapyear(year):
  print("{} is  a leap year.".format(year))
else:
  print("{} is not a leap year.".format(year))
    