l = list(map(int,input('Enter list  ').split()))

def count_year(l):
    year = 0
    a = 0.025
    s = 0
    for x in l:
        growth = 0
        for y in range(13):
            x += (growth + a)*x
            year = y + 1
            growth -= 0.001
        s += x
        a -= 0.004
    print(int(s*1000000))
    print(year)
count_year(l)