import math

time = 150


print "With {0} soldiers moving abreast, the passage took [{1} minutes, {2} seconds] or [{3} rounds] to cross.".format(15, time * 60 // 60, time * 60 % 60, math.ceil(time * 6))