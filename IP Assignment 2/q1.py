menu = {'Samosa':15,'Idli':30,'Maggie':50,'Dosa':70,'Tea':10,'Coffee':20,'Sandwich':35,'ColdDrink':25}
c = []
b = []

def Menu(l):
    
    flag = True
    print('1.    Samosa    : 15 ')
    print('2.    Idli      : 30 ')
    print('3.    Maggie    : 50 ')
    print('4.    Dosa      : 70 ')
    print('5.    Tea       : 10 ')
    print('6.    Coffee    : 20 ')
    print('7.    Sandwich  : 35 ')
    print('8.    ColdDrink : 25 ')

    while flag:

        a = list(map(int,input('Enter Item Number & Quantity: ').split()))

        if len(a) != 2:
            break
        else:
            l.append(a[0])

        if a[0] == 1:
            add(1,a)
        elif a[0] == 2:
            add(2,a)
        elif a[0] == 3:
            add(3,a)
        elif a[0] == 4:
            add(4,a)
        elif a[0] == 5:
            add(5,a)
        elif a[0] == 6:
            add(6,a)
        elif a[0] == 7:
            add(7,a)
        elif a[0] == 8:
            add(8,a)

def add(x,l):
    if x == 1:
        c.append(int(menu['Samosa']*l[1]))
        b.append(int(l[1]))
    elif x == 2: 
        c.append(int(menu['Idli']*l[1]))
        b.append(int(l[1]))
    elif x == 3:
        c.append(int(menu['Maggie']*l[1]))
        b.append(int(l[1]))
    elif x == 4:
        c.append(int(menu['Dosa']*l[1]))
        b.append(int(l[1]))
    elif x == 5:
        c.append(int(menu['Tea']*l[1]))
        b.append(int(l[1]))
    elif x == 6:
        c.append(int(menu['Coffee']*l[0]))
        b.append(int(l[1]))
    elif x == 7:
        c.append(int(menu['Sandwich']*l[1]))
        b.append(int(l[1]))
    elif x == 8:
        c.append(int(menu['ColdDrink']*l[1]))
        b.append(int(l[1]))

l = []
Menu(l)

for i in range(len(l)):
    l[i] -= 1

for i in range(len(c)):
    a = c[i]//b[i]
    x = 0
    for j in menu:
        if x == l[i]:
            print(j +', '+ str(b[i]) +', Rs '+str(c[i]))
        x += 1
print('TOTAL,'+ str(sum(b)) + ',Rs ' + str(sum(c)))
