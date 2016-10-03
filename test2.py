import math
distance = 760
totalmen = 77
men = 3
speed = 2

#time = ((distance + (totalmen * 5 // men + (totalmen * 5 % men))) // (speed * 15) + distance % (speed * 15)) * 6

#convert speed to fpm and float
#Calculate travel time + extra for length of the army
speed = speed * 15 * 10.0
time = distance / speed + ((math.ceil(totalmen // men) + totalmen % men) * 5) / speed

print totalmen / men
print math.ceil(totalmen / men)
print "The passage took [%s minutes, %s seconds] or [%s rounds] to cross." % (int(time * 60 // 60), int(time * 60 % 60), int(math.ceil(time * 6)))


