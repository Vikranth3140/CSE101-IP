file_name = 'addressbook.txt'
import json

def Menu():
    print('1. Insert Entries')
    print('2. Delete Entries')
    print('3. Find Entries using Partial Names')
    print('4. Find Entries using Phone No. and Email No.')
    print('5. Exit')
    addressbook = check_file(file_name)
    merge(addressbook,check_file(file_name))
    while True:
        ch = int(input('Enter choice No. : '))
        if ch == 1:
            insert(addressbook)
        elif ch == 2:
            delete(addressbook)
        elif ch == 3:
            print(partial(addressbook))
        elif ch == 4:
            entries_using_ph_email(addressbook)
        elif ch == 5:
            with open (file_name,'w') as f:
                json.dump(addressbook,f)
            break
        else:
            print('You have entered the wrong choice')

def insert(addressbook):
    user_name = input()
    address = input()
    ph_no = input()
    email_id = input()
    addressbook = multiple_names(addressbook,user_name,address,ph_no,email_id)
    return addressbook

def delete(addressbook):
    x = input("Which Name's Adress you want to delete : ")
    del addressbook[x]
    return addressbook

def partial(addressbook):
    x = input('Enter Name of whom you want to search : ')
    for i in addressbook.keys():
        if x.lower() in i.lower():
            return i,addressbook[i]

def entries_using_ph_email(addressbook):
    ph = input('Enter Phone No. or email ID : ')
    for i,j in addressbook.items():
        if type(j) == dict:
            for k,l in j.items():
                if l == ph:
                    print(i,j)
        else:
            for p in range(len(j)):
                if j[p]['Phone No.'] == ph or j[p]['Email ID'] == ph:
                    print(i,j[p])

def check_file(filename):
    f = open("addressbook.txt",'r')
    try:
        line1 = json.load(f)
    except:
        line1 = {}
    return line1

def merge(addressbook,check_file):
    if check_file == {}:
        return addressbook
    else:
        addressbook.update(check_file)
        return addressbook

def multiple_names(addressbook,user_name,address,ph_no,email_id):
    d = {}
    d['Address'] = address
    d['Phone No.'] = ph_no
    d['Email ID'] = email_id
    l = []
    if addressbook == {}:
        addressbook[user_name] = d
    else:
        for i,j in addressbook.items():
            if user_name == i:
                l.append(j)
                l.append(d)
                addressbook[user_name] = l
            else:
                addressbook[user_name] = d
    return addressbook

Menu()