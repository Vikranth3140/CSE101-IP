cost = int(input('Enter cost of laptop you want to buy'))
allowance = int(input('Enter the allowance'))
sf = float(input('Enter the saving fraction'))
r = float(input('Enter the interest rate'))
save = 0
flag = True
month = 1

while flag:
    save = save + save*(r/100)
    save = save + allowance*sf
    month = month + 1
    if cost < save:
        flag = False

print(save - cost)
print(month - 1)