cx = int(input('Enter cx : '))
cy = int(input('Enter cy : '))

def coordinates():
    l = []
    flag = True
    while flag:
        x = list(map(int,input('Enter x and y : ').split()))
        if len(x) == 2:
            x.append(1)
            x1 = tuple(x)
            l.append(x1)
        else:
            flag = False
    y = len(l)
    return l,y

def matrix_mult(cx,cy):
    m2 = [[cx,0,0],[0,cy,0],[0,0,1]]
    k = [[0 for x in range(len(m2[0]))] for y in range(len(l1))]
    for i in range(len(l1)):
        for j in range(len(m2[0])):
            for p in range(len(m2)):
                k[i][j] += l1[i][p] * m2[p][j]
    return k

l1,y=coordinates()
b = matrix_mult(cx,cy)

for i in range(len(b)):
    print(b[i][0] ,end = ' ')
    print(b[i][1] ,end = '\n')