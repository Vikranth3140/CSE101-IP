def opening_file():
    with open("sorted_copy.txt") as file:
        read_file = file.read().splitlines()
        return read_file

#opening file
read_file = opening_file()

#taking the text from file and modifiying it
start_list = []
for i in read_file:
    var = i.split(', ')
    start_list.append(var)
temp_list = start_list[1::]

#finding name list
names_list = []
for i in temp_list:
    names_list.append(i[0])

#counting number of repititions
names_list_without_repitition = []
name_count = 0
count_dict = {}

sorted_names_list = names_list.copy()
sorted_names_list.sort()

for i in sorted_names_list:
    if i in names_list_without_repitition:
        name_count += 1
    else:
        names_list_without_repitition.append(i)
        name_count = 1

    count_dict[i] = name_count

#making gate no ,crossing ,start and end time into list
crossing_list = []
gate_no_list = []
start_time_list = []
end_time_list = []
for i in temp_list:
    crossing_list.append(i[1])
    gate_no_list.append(i[2])
    
    if i[1] == 'ENTER':
        start_time_list.append(i[3])
        end_time_list.append(' ')
    else:
        start_time_list.append(' ')
        end_time_list.append(i[3])
print()
print(crossing_list)
print(gate_no_list)
print(start_time_list)
print(end_time_list)
print()

Campus_Record = {}

#count_dict = {'Bharat Goyal': 1, 'Bhavya Jain': 1, 'Khushdev Pandit': 4, 'Rohan Dhar': 1, 'Sahil Goyal': 1, 'Thanmayee Matha': 1}

temp_list1 = []
for i,j in count_dict.items():
    temp_dict = {}
    for k in range(len(names_list) - 1):
        temp_dict['Crossing'] = crossing_list[k]
        temp_dict['Gate'] = gate_no_list[k]
        if crossing_list[k]== 'ENTER':
            temp_dict['Time'] = start_time_list[k]
        elif crossing_list[k] == 'EXIT':
            temp_dict['Time'] = end_time_list[k]

        temp_list1.append(temp_dict)

        print(k)
    print(temp_dict)
print(temp_list1)
print()
print(names_list)


#appending values into the main dictionary
for i,j in count_dict.items():
    for k in range(j):
        Campus_Record[i] = temp_list1

print(Campus_Record)



def student_details(stud_name):
    a = b

def timing(start_tim,end_tim):
    a = b

def gate_func(gate_no):
    a = b

def main():
    print("1. Showing student details :")
    print("2. Showing the students who entered / exited the campus in between start & end time :")
    print("3. Showing the students who used the gate :")

    ch = int(input('Enter your choice : '))

    if ch == 1:
        student_name = input("Enter Student's name: ")
        student_details(student_name)
    elif ch == 2:
        start_tim = input("Enter Start time : ")
        end_tim = input("Enter End time : ")

        timing(start_tim,end_tim)
    elif ch == 3:
        gate_no = int(input("3. Enter Gate Number :"))
        gate_func(gate_no)

def student_details(stud_name,time):
    tim_list = []
    bool = True
    while bool:
        for i,j in dict.items():
            if i == stud_name:
                if bool == True:
                    for k in j:
                        if bool == True:
                            if k['Time'] <= time:
                                tim_list.append(k)
                            else:
                                print('The student is not in the campus')
                                bool = False