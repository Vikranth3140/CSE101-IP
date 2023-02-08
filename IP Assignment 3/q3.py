import random

n = int(input())
def open_file(n):
    global input_line
    global file_name
    f=open("scores.txt","w")
    for i in range(n):
        file_name = input('Enter the filename : ')
        with open(file_name) as input_file:
            input_file = input_file.read()
            input_line = ''
            for i in input_file:
                if i == '\n':
                    input_line += ' '
                else:
                    input_line += i
            # print('The input line is :',input_line)
            # print()
            net_grade =(round(( 4 + f1()*6 + (f2()[0])*6 - f3() - f4() - f5()),2))
            print('Net Grade :', net_grade)      
            f.write(file_name)
            f.write('\n')
            f.write('Score : ' + str(net_grade))
            f.write('\n')
            f.write('The 5 most words being printed is : ' + str((f2()[1])))
            f.write('\n')
            f.write('Random 5 words are : ' + str(random_5()))
            f.write('\n')

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

    most_5 = []
    for i in range(5):
        count_5_most_used += count_dict[i][1]
        most_5.append(count_dict[i][0])
        most_5.reverse()
    f2_grade = count_5_most_used / count_total
    return f2_grade,most_5

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
        if ':;,. ' in i:
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

def random_5():
    random_word1 = random.choice(unique_word_list)
    random_word2 = random.choice(unique_word_list)
    random_word3 = random.choice(unique_word_list)
    random_word4 = random.choice(unique_word_list)
    random_word5 = random.choice(unique_word_list)
    return random_word1,random_word2,random_word3,random_word4,random_word5
open_file(n)