# -*- coding: utf-8 -*-\
import datetime

t1 = datetime.datetime.utcnow()

f = open('Test/30K.csv', 'r')

list4 =[]
lines = f.readlines()
for line in lines:
    list1 = ['User_Name', 'User_ID']
    list2 = line.strip().split('|')
    dict1 = dict(zip(list1,list2))
    list4.append(dict1)


t2 = datetime.datetime.utcnow()
print(t2 - t1)
