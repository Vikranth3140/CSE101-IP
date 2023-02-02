f = open("Question3.txt",'r')
line1 = f.read().splitlines()

line2 = []
for i in line1:
    k = i.strip()
    line2.append(k)
line3 = []
main = []
students = []
for i in range(len(line2)):
    if line2[i] == '':
        pass
    else:
        line3.append(line2[i])
line4 = []
for i in line3:
    if i[-1]==':':
        students.append(i)
    if i[-1]==':':
        pass
    else:
        i = i.split(',')
        line4.append(i)

l = 0
student_signed = {}
for i in range(0,len(line4),len(students)-1):
    temp_dict = {}
    for j in range(len(students)-1):
        temp_dict[line4[i+j][0]] = int(line4[i+j][1])
    student_signed[students[l]] = temp_dict
    l += 1
signs = []
for v in student_signed.values():
    count = 0
    for keys,values in v.items():
        count += values
    signs.append(count)

for i,j in zip(students,signs):
    if max(signs) == j:
        print("Maximum signs are of",i[:-1])
for i,j in zip(students,signs):
    if min(signs) == j:
        print("Minimum signs are of",i[:-1])