n = int(input())
z = n

def upper(n):
    if n == 0:
        pass
    else:
        if n != z:
            print(n*'* ' + (4*(z-n))*' ' + (n)*'* ')
        else:
            print(n*'* ' + (4*(z-n)-4)*' ' + (n)*'* ')
        n = n-1
        upper(n)

def lower(n):
    if n == 0:
        pass
    else:
        if z != n:
            if z - n != 1:
                print((z-n)*'* ' + (4*(n))*' ' + (z-n)*'* ')
        n = n-1
        lower(n)

upper(n)
lower(n)
print(n*'* ' + (4*(z-n))*' ' + n*'* ')