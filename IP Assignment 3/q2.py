def opening_file():
    with open("sorted_copy.txt") as file:
        read_file = file.read().splitlines()
        return read_file

read_file = opening_file()

start_list = []
for i in read_file:
    var = i.split(', ')
    start_list.append(var)

temp_list = start_list[1::]
print(temp_list)

names_list = []