n = int(input())
def open_file(n):
    global input_line
    global file_name
    for i in range(n):
        file_name = input()
        with open(file_name) as input_file:
            input_line = input_file.read()
            print('The input line is :',input_line)
            print()

def f1():
    global unique_word_list
    unique_word_list = []
    for i in input_line.split(' '):
        if i not in unique_word_list:
            unique_word_list.append(i.strip(':;,.'))

    unique_word_list_actual = []
    for i in unique_word_list:
        x=i.lower()
        if x not in unique_word_list_actual:
            unique_word_list_actual.append(x)

    count_unique = len(unique_word_list_actual)
    count_total = len(input_line.split(' '))
    f1_grade = count_unique / count_total
    return f1_grade

def f2():
    unique_word_list_1 = []
    for i in input_line.split(' '):
        i = i.strip(':;,. ')
        if i not in unique_word_list_1:
            unique_word_list_1.append(i)

    d = {}
    for i in input_line.split(' '):
        count = 0
        i = i.strip(':,.; ')
        for j in input_line.split(' '):
            j = j.strip(':;,. ')
            if j == i:
                count += 1
        d[i] = count

    count_total = len(input_line.split(' '))
    count_5_most_used = 0
    count_dict = sorted(d.items(), key=lambda x:x[1],reverse = True)

    for i in range(5):
        count_5_most_used += count_dict[i][1]
    f2_grade = count_5_most_used / count_total
    return f2_grade

def f3():
    sentences_list = []
    sentence_count = 0

    for i in input_line.split('. '):
        sentences_list.append(i)
        sentence_count += 1
    sentence_in_range_count = 0
    for i in range(sentence_count):
        if len(sentences_list[i].split(' ')) > 35 or len(sentences_list[i].split(' ')) < 5:
            sentence_in_range_count += 1

    f3_grade = sentence_in_range_count / sentence_count
    return f3_grade

def f4():
    unique_word_list = []
    word_without_symbols = []
    count_symbols = 0
    list = []

    for i in input_line.split(' '):
        if i not in unique_word_list:
            unique_word_list.append(i)
        for j in i:
            if j in ':;,.':
                count_symbols += 1
            else:
                word_without_symbols.append(i.strip(',.;: '))

    list1=[]
    count = 0
    for i in unique_word_list:
        if i[-2] in ':;,.':
            list1.append(i)
            count += 1
    f4_grade = count / len(input_line.split(' '))

    return f4_grade

def f5():
    unique_word_list = []
    for i in input_line.split(' '):
        if i not in unique_word_list:
            unique_word_list.append(i)
    count_unique = len(unique_word_list)
    count_total = len(input_line.split(' '))

    if count_total > 750:
        return 1
    else:
        return 0

open_file(n)
# print('f1 Grade :',f1())
# print('f2 Grade :',f2())
# print('f3 Grade :',f3())
# print('f4 Grade :',f4())
# print('f5 Grade :',f5())
# print()

net_grade =(round(( 4 + f1()*6 + f2()*6 - f3() - f4() - f5()),2))
print('Net Grade :', net_grade)

f=open("scores","w")

f.write(file_name)
f.write('\n')
f.write('Score : ' + str(net_grade))
f.write('\n')