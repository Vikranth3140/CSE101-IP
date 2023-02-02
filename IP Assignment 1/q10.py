def polynomial(x):
    a = x**3 - 10.5*x**2 + 34.5*x - 35
    return a

def differentiate(x):
    b = 3*x**2 - 21*x + 34.5
    return b

x0 = int(input('Enter the value of x0'))
c = polynomial(x0) / differentiate(x0)


while abs(c)>0.00000000000001:
    c = polynomial(x0) / differentiate(x0)
    x0 -= c
print('The root of the polynomial =',x0)