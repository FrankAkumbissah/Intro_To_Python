import math
import time

#radians = celcius * pi/180
temp = float(input("what is the temperature (in degree celcius)?\n"))
first = math.pi / 180
radian = temp * first
print("The temperature in radian is:", radian,"\n")

#surface area = 4 pi r^2
rad = float(input("what is the radius of the sphere? \n"))
sa = 4 * math.pi * (math.pow(rad, 2))
print("The surface area of the sphere is:", sa,"\n")

#volume = (4/3)*pi*r^3
volume = (4/3) * math.pi * (math.pow(rad, 3))
print("The volume of the shpere is:", volume, "\n")


initial = time.localtime() # get struct_time
current_time = time.strftime("%H:%M:%S", initial)
print("The current time is", current_time, "\n")

