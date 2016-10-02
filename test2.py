import math
distance = 760
totalmen = 50
men = 2
speed = 2

#time = ((distance + (totalmen * 5 // men + (totalmen * 5 % men))) // (speed * 15) + distance % (speed * 15)) * 6

#convert speed to fpm and float
speed = speed * 15 * 10.0


time = distance / speed #+ (totalmen // men * 5) / speed

print speed
print time
print math.ceil(time)