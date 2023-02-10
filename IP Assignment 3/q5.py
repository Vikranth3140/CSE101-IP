import time

def opening_file(file):
    with open(file) as file:
        read_file = file.read().splitlines()
    return read_file
read_file = opening_file('q4_5.txt')

wts = [("labs", 30),("midsem", 15),("assignments", 30),("endsem", 25)]
main_list = []
for i in read_file:
    i = i.split(', ')
    main_list.append(i)
d = {}
for i in main_list:
    for j in i:
        d[i[0]] = i[1::]

def percentage(d,wts):
    percentage_list = []
    for i,j in d.items():
        temp_list = []
        for k in range(len(j)):
            temp_list.append((int(j[k]) * wts[k][1]) / 100)
        percentage_list.append(temp_list)
    return percentage_list
percentage_list = percentage(d,wts)

total_list = []
for k,i in zip(percentage_list,d.keys()):
    temp_count = 0
    for j in range(len(k)):
        d[i] = k
        temp_count += k[j]
    total_list.append(temp_count)

count_A = 0
count_B = 0
count_C = 0
count_D = 0
count_F = 0
def grade(sum):
    global count_A
    global count_B
    global count_C
    global count_D
    global count_F
    grd = ''
    if sum > 80:
        grd = 'A'
        count_A += 1
    elif 80 >= sum > 65:
        grd = 'B'
        count_B += 1
    elif 65 >= sum > 50:
        grd = 'C'
        count_C += 1
    elif 50 >= sum > 40:
        grd = 'D'
        count_D += 1
    else:
        grd = 'F'
        count_F += 1
    return grd

grade_list1 = []
for i in total_list:
    grd = grade(i)
    grade_list1.append(grd)

dict_percentage = {}
for i,j in zip(d.keys(),total_list):
    dict_percentage[i] = j

dict_grade = {}
for i,k in zip(d.keys(),grade_list1):
    dict_grade[i] = k

grade_list = ['A','B','C','D','F']
len_grade = []
len_grade.append(count_A)
len_grade.append(count_B)
len_grade.append(count_C)
len_grade.append(count_D)
len_grade.append(count_F)
dict_count = {}
for i,j in zip(grade_list,len_grade):
    dict_count[i] = j

policy = [80, 65, 50, 40]
list_less_2 = []
for i in range(len(policy)):
    temp_list = []
    for j in dict_percentage.values():
        if abs(policy[i] - j) <= 2:
            temp_list.append(j)
    list_less_2.append(temp_list)
    temp_list.sort(reverse=True)
    if temp_list == []:
        pass
    else:
        diff = []
        for l in range(1,len(temp_list)):
            diff.append(temp_list[l-1]-temp_list[l])
        if diff == []:
            pass
        else:
            policy[i] = round((temp_list[diff.index(max(diff))] + temp_list[diff.index(max(diff))+1]),2)/2
for i in range(len(list_less_2)):
    list_less_2[i] = sorted(list_less_2[i],reverse = True)

def student_details():
    print('Course Name :',course_name)
    print('Credits :',credits)
    print('Weights :',wts)
    print('Cutoffs for different grades :',policy)
    print('Grading Summary :',dict_count)

def show_grd():
    f=open("Student's Grade Summary","w")
    for i,j in zip(dict_percentage.items(),dict_grade.values()):
        f.write(i[0] + ", " + str(i[1]) + ", " + str(j))
        f.write('\n')

def search_stud(roll_no):
    bool1 = True
    for k in d.keys():
        if int(k) == int(roll_no):
            print('The Marks :',d[k])
    for i,j in zip(dict_grade.items(),dict_percentage.items()):
        if int(i[0]) == roll_no and int(j[0]) == roll_no:
            print('The Grade :',i[1])
            print('The Percentage :',j[1])
            bool1 = True
            break
        else:
            bool1 = False
    if bool1 == False:
        print('Student with that Roll No not found')

def main():
    global course_name
    global credits
    count1 = 0
    count2 = 0
    course_name = input('Enter Course Name : ')
    credits = int(input('Enter Credits : '))
    print("1. Generate summary of the course")
    print("2. Show the grades of all students")
    print("3. Search student's record")
    while True:
        ch = input('Enter your choice : ')
        if ch == '1':
            student_details()
        elif ch == '2':
            start = time.time()
            show_grd()
            end = time.time()
            print(end-start)
            count1 += 1
        elif ch == '3':
            roll_no = int(input("Enter Roll No. : "))
            start = time.time()
            search_stud(roll_no)
            end = time.time()
            print(end - start)
            count2 += 1
        elif ch == '':
            print('Thank You!!!')
            break
        else:
            print('Enter another choice')

    print('N1:'count1)
    print('N2:'count2)
main()