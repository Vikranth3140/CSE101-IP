with open('q4_5.txt') as file:
    read_file = file.read().splitlines()

wts = [("labs", 30),("midsem", 15),("assignments", 30),("endsem", 25)]

count_A = 0
count_B = 0
count_C = 0
count_D = 0
count_F = 0
policy = [80,65,50,40]

class Course:
    def __init__(self,grd,policy):
        self.d = {}
        self.total_list = []
        self.grd = grd
        self.dict_percentage = {}
        self.percentage_list = []
        self.dict_grade = {}
        self.dict_count = {}
        self.policy = policy

    def start_file(self):
        wts = [("labs", 30),("midsem", 15),("assignments", 30),("endsem", 25)]
        main_list = []
        for i in read_file:
            i = i.split(', ')
            main_list.append(i)
        for i in main_list:
            for j in i:
                self.d[i[0]] = i[1::]
        return main_list,self.d

    def percentage(self):
        for i,j in self.d.items():
            temp_list = []
            for k in range(len(j)):
                temp_list.append((int(j[k]) * wts[k][1]) / 100)
            self.percentage_list.append(temp_list)
        return self.percentage_list

    def tot_list(self):
        for k,i in zip(self.percentage_list,self.d.keys()):
            temp_count = 0
            for j in range(len(k)):
                self.d[i] = k
                temp_count += k[j]
            self.total_list.append(temp_count)

    def grade(self,sum):
        self.grd = ''
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
        return self.grd

    def dict(self):
        grade_list1 = []
        for i in self.total_list:
            grd = self.grade(i)
            grade_list1.append(grd)
        for i,j in zip(self.d.keys(),self.total_list):
            self.dict_percentage[i] = j
        for i,k in zip(self.d.keys(),grade_list1):
            self.dict_grade[i] = k
        return self.dict_percentage,self.dict_grade

    def grd_updation(self):
        grade_list = ['A','B','C','D','F']
        len_grade = []
        len_grade.append(count_A)
        len_grade.append(count_B)
        len_grade.append(count_C)
        len_grade.append(count_D)
        len_grade.append(count_F)
        for i,j in zip(grade_list,len_grade):
            self.dict_count[i] = j
        return self.dict_count

    def cutoff(self):
        list_less_2 = []
        for i in range(len(self.policy)):
            temp_list = []
            for j in self.dict_percentage.values():
                if abs(self.policy[i] - j) <= 2:
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
                    self.policy[i] = round((temp_list[diff.index(max(diff))] + temp_list[diff.index(max(diff))+1]),2)/2
        for i in range(len(list_less_2)):
            list_less_2[i] = sorted(list_less_2[i],reverse = True)

class Student:
    def __init__(self,dict_count,policy,dict_percentage,dict_grade,d):
        self.dict_count = dict_count
        self.policy = policy
        self.dict_percentage = dict_percentage
        self.dict_grade = dict_grade
        self.d = d

    def student_details(self):
        print('Course Name :',course_name)
        print('Credits :',credits)
        print('Weights :',wts)
        print('Cutoffs for different grades :',self.policy)
        print('Grading Summary :',self.dict_count)

    def show_grd(self):
        f=open("Student's Grade Summary","w")
        for i,j in zip(self.dict_percentage.keys(),self.dict_grade.values()):
            f.write(i[0] + ", " + str(i[1]) + ", " + str(j))
            f.write('\n')

    def search_stud(self,roll_no):
        bool1 = True
        for k in self.d.keys():
            if int(k) == int(roll_no):
                print('The Marks :',self.d[k])
        for i,j in zip(self.dict_grade.items(),self.dict_percentage.items()):
            if int(i[0]) == roll_no and int(j[0]) == roll_no:
                print('The Grade :',i[1])
                print('The Percentage :',j[1])
                bool1 = True
                break
            else:
                bool1 = False
        if bool1 == False:
            print('Student with that Roll No not found')

grd = ['A','B','C','D','F']
course_name = input('Enter Course Name : ')
credits = int(input('Enter Credits : '))
course_class = Course(grd,policy)
main_list,dictionary = course_class.start_file()
percentage,grade = course_class.dict()
count = course_class.grd_updation()
def main():
    b = Student('IP',"4",count,policy,percentage,grade,main_list)
    print("1. Generate summary of the course")
    print("2. Show the grades of all students")
    print("3. Search student's record")
    while True:
        ch = input('Enter your choice : ')
        if ch == '1':
            Student(course_name,credits,wts,policy,count).student_details()
        elif ch == '2':
            Student(percentage,grade).show_grd()
        elif ch == '3':
            roll_no = int(input("Enter Roll No. : "))
            Student(main_list,percentage,grade).search_stud(roll_no)
        elif ch == '':
            print('Thank You!!!')
            break
        else:
            print('Enter another choice')
main()