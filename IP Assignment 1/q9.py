import math

p = int(input('Enter initial price'))

def demand_func(a,b,p): return math.e**(a-b*p)
def supply_func(c,d,p): return math.e**(c+d*p)

while demand_func(10,1.05,p)>=supply_func(1,1.06,p):
    p += 0.05*p

print('Demand =',demand_func(10,1.05,p))
print('Supply =',supply_func(1,1.06,p))
print('Price =',p)