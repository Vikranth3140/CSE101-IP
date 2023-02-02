n = int(input())

one = n%10
ten = n//10

d1 = ['zero','one','two','three','four','five','six','seven','eight','nine']
d2 = ['','','twenty','thirty','forty','fifty','sixty','seventy','eight','ninety']
d3 = ['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
#d4 = {11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen'}

if 0<=n<=9:
    print(d1[one])
elif n>9 and n <20:
    print(d3[one])
elif n>19 and n<100:
    print(d2[ten],d1[one])
