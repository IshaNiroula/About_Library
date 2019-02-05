# Using operating system and changing the file name #

import os

a = os.path.join ("C:\\Users\\Lenovo\\PycharmProjects\\Class-8", "file4.py")
b = os.path.join ("C:\\Users\\Lenovo\\PycharmProjects\\Class-8", "file1.py")

os.rename(b,a)

# Date and Time #

import datetime as dt
today = dt.date.today()
print("Year: ", today.year)
print("Month: ", today.month)
print("Day: ", today.day)

# functions from math library #

import math

x=int(input("Enter the value of angle: "))
# degree #
print("The value of angle in degree is: ",math.degrees(x))
#radian#
print("The value of angle in radian is: ",math.radians(x))


# find some of the library #

from PIL import Image
myImage = Image.open("theflower.jpg")
myImage.show()
