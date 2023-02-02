import math

a = int(input('Enter starting time'))
b = int(input('Enter ending time'))
flag = True
x = a
t = 0
v = 0
while flag:
    v += (2000*math.log(140000/(140000 - 2100*x))) - (9.8*x)
    x += 0.25
    t += 1

    if x>b:
        flag = False
avg = v/t
d = avg*(b-a)
print('The distance covered by the rocket =',d)