f = open("/home/vik/Desktop/IP Assignment 2/pages.txt",'r')
urls_list = []
init_importance_list = []
url_text_list = []
for line in f:
    url_initimportance,url_text = line.split(': ')
    urls,init_importance = url_initimportance.split(', ')
    urls_list.append(urls)
    init_importance_list.append(init_importance)
    url_text_list.append(url_text)

url_in_text = []
for i in url_text_list:
    words_in_text = i.split(' ')

other_url = []
for i in url_text_list:
    temp_l = []
    for j in urls_list:
        if j in i:
            temp_l.append(j)
    other_url.append(temp_l)

d = {}
another_dict = {}
for i in range(len(urls_list)):
    d[urls_list[i]] = {
        'Init importance': float(init_importance_list[i]),
        'Importance': 0.0,
        'Urls': other_url[i]
    }

for i,j in d.items():
    calc = j['Init importance']/len(j['Urls'])
    for x in j['Urls']:
        d[x]['Importance'] += calc
sorted_dict = sorted(d.items(), key=lambda x:x[1]['Importance'], reverse=True)

for i in sorted_dict:
    print(i[0]+': '+str(i[1]['Importance']))