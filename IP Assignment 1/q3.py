x = 0
y = 0
distance = 0

compdist = 0
flag = True

while flag :
    d = int(input())

    if d <=0:
        flag = False
        compdist += d
    elif d <= 25:
        
        y += d
        compdist += d
    elif d <=50 and d >=26:
        
        y -= d
        compdist += d
    elif d <=75 and d >=51:
        
        x += d
        compdist += d
    else:
        
        x -= d
        compdist += d

print('x coordinate = ',x)
print('y coordinate = ',y)
print('Displacement =',((x**2 + y**2)**0.5))
print('Distance travelled =',compdist)