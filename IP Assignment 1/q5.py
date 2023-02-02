def fact(n):
    product = 1
    for i in range(1,n+1):
        product *= i
    return product

def angle_converter(a):
    r = a*pi/180
    return r

def sin(x):
    f = 0
    for i in range(10):
        f += (((-1)**i) * (x**((2*i)+1))) / fact((2*i)+1)
    return f

def cos(x):
    g = 0
    for i in range(10):
        g += (((-1)**i) * x**((2*i))) / fact((2*i))
    return g

def height(a,d):
    b = angle_converter(a)
    x = sin(b)/cos(b)
    h = d*x
    return h

def distance(a,d):
    b = angle_converter(a)
    dist = d / cos(b)
    return dist

a = float(input('Enter angle'))
d = int(input('Enter distance'))
pi = 3.14

if a == 90:
    print('The line of sight and the height will be parallel and their values cannot be calculated')
elif a == 0:
    print('The line of sight and the distance will be parallel and the values cannot be calculated')
else:
    print('The height of the pole =',height(a,d))
    print('The distance of the pole from the person =',distance(a,d))