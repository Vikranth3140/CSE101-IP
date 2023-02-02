def func():
    n = int(input('Enter the value of n'))
    for i in range(n+1):
        print('*'*i + ' '*(n-i)*2 +'*'*i)

func()