def printn(num):
    if (num == 0):
        return
    print("*", end = " ")

    printn(num - 1)

def pattern_1(n, i):
    if (n == 0):
        return
    printn(i)
    print("\n", end = "")

    pattern_1(n - 1, i + 1)

def print_space(space):
    if (space == 0):
        return
    print(" ", end=" ")

    print_space(space - 1)

def print_asterisk(asterisk):
    if (asterisk == 0):
        return  

    print("*", end =" ")

    print_asterisk(asterisk - 1)

def pattern(n, num):
    if (n == 0):
        return

    print_space(n - 1)
    print_asterisk(num - n + 1)
    print()
    pattern(n - 1, num)

if __name__ == '__main__':
    n = int(input('Enter n'))
    pattern_1(n, 1)
    pattern(n, n)