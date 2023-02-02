M = int(input())
x1 = 0

for i in range(200):
    t1 = 200 - 4*x1
    t2 = 120 - 2*x1 
    if t1 == t2:
        print('The number of tables to be manufactured =',x1)
        print('The number of chairs to be manufactured =',t2)
        break
    x1+=1

if M>x1:
    print("Total profit will be : ",(90*M)+(25*M))
else:
    print("Total profit will be : ",(90*M)+(25*M)+((x1-M)*100)+((t2-M)*30))