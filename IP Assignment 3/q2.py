def opening_file():
    with open("sorted_data.txt") as file:
        read_file = file.read().splitlines()
    return read_file
read_file = opening_file()

start_list = []
for i in read_file:
    var = i.split(', ')
    start_list.append(var)
temp_list = start_list[1::]

names_list = []
for i in temp_list:
    names_list.append(i[0])

names = []
for i in names_list:
    if i not in names:
        names.append(i)

dict={}
for i in names:
    dict[i]={}

for i in temp_list:
    temp_dict = {}
    temp_list= []
    for j,k in dict.items():
        temp_dict["Crossing"]=i[1]
        temp_dict["Gate"]=i[2]
        temp_dict["Time"]=i[3]
        if j==i[0]:
            temp_list.extend(k)
            temp_list.append(temp_dict)
            dict[i[0]]=temp_list

def student_details(stud_name,time):
    f=open("student_details.txt","w")
    try:
        tim_list = []
        for i,j in dict.items():
            if i == stud_name:
                for k in j:
                    if k['Time'] <= time:
                        tim_list.append(k)
        for i,j in tim_list[-1].items():
            c = 0
            if j == 'ENTER':
                c = 1
                break
            elif j == 'EXIT':
                c = 0
                break
        if c == 0:
            print('He is not inside the campus')
        else:
            print('He is in the campus')
    except:
        if k['Time'] >= time:
            print('The student has not entered or exited the campus')
    for i,j in dict.items():
        if i == stud_name:
            f.write(str(j) + '\n')
            f.write('\n')
    f.close()

def timing(start_tim,end_tim):
    f=open("student_details.txt","w")
    for i,j in dict.items():
        for k in j:
            if start_tim <= k['Time'] and k['Time']<= end_tim:
                f.write(i + str(k) + '\n')
    f.close()

def gate_func(gate_no):
    in_count = 0
    out_count = 0
    for i,j in dict.items():
        for k in j:
            if k['Gate'] == gate_no:
                if k['Crossing'] == 'ENTER':
                    in_count += 1
                elif k['Crossing'] == 'EXIT':
                    out_count += 1
    print('The number of students who have entered the campus :',in_count)
    print('The number of students who have exited the campus :',out_count)

def main():
    print("1. Showing student details :")
    print("2. Showing the students who entered / exited the campus in between start & end time :")
    print("3. Showing the students who used the gate :")
    print('4. Exit')
    while True:
        ch = int(input('Enter your choice : '))
        if ch == 1:
            student_name = input("Enter Student's name : ")
            current_time = input("Enter Current time : ")
            student_details(student_name,current_time)
        elif ch == 2:
            start_tim = input("Enter Start time : ")
            end_tim = input("Enter End time : ")
            timing(start_tim,end_tim)
        elif ch == 3:
            gate_no = input("3. Enter Gate Number :")
            gate_func(gate_no)
        elif ch == 4:
            break
        else:
            print('Invalid input')
main()