import os
import re
import exrex
import time
import datetime


car_re = re.compile(r'''
^
(\d{2,3}    
[ ]*
[가-힣]
[ ]*
\d{4})
[ ]*
(\d{4,5})
[ ]*
(.*)
''', re.VERBOSE)

pattern = r'''
^
(\d{2,3}    
[ ]*
[가-힣]
[ ]*
\d{4})
[ ]*
(\d{4,5})
[ ]*
(.*)
'''

final_pattern = re.sub(r'[ ]{2,}|\t|\n', '', pattern)

# test_str = [exrex.getone(final_pattern, 5) for _ in range(1000)]

carwash_records = []


def ReadFile(fileName):
    f = open(fileName, 'r')
    No = 1
    while True:
        data = f.readline()
        if data:
            carNum, cost, etc = car_re.search(data).groups()
            carwash_records.append((No, carNum.replace(" ",''), cost, etc))
            No += 1
        else:
            break


def WriteFile(fileName):
    f = open(fileName, 'w')
    for data in carwash_records:
        f.write(str(data[0] + data[1] + data[2])+'\n')
    f.close()


def InsertCarData():
    text = input()
    mo = car_re.search(text)
    if mo:
        carwash_records.append(mo.groups())
    else:
        print('형식이 올바르지 않음.')



def PrintAll():
    No = 1
    for data in carwash_records:
        print(format(f"{data[0]:4}\t{data[1]:>8}\t{data[2]:>5}\t{data[3]}"))
        No += 1


def ShowOne(data):
    print(format(f"{No:4}\t{data[0]:>8}\t{data[1]:>5}\t{data[2]}"))


def DeleteCarDataByCarNum():
    global carwash_records
    text = input()
    find_list = []
    for data in carwash_records:
        if data[1] == text.replace(" ", ''):
            find_list.append(data)
            print(find_list)
    if not find_list:
        return False
    for d in find_list:
        carwash_records.remove(d)
    return True



def DeleteAllCarByCost():
    pass


def DeleteAllCarByEtc():
    pass


def FindCarDataByCarNum():
    text = input()
    find_list = []
    for data in carwash_records:
        if data[1] == text.replace(" ", ''):
            find_list.append(data)
            print(find_list)
            return True
    return False


def FindAllCarByCost():
    text = input()
    find_list = []
    for data in carwash_records:
        if data[2] == text.replace(" ", ''):
            find_list.append(data)
            print(find_list)
            return True
    return False


def FindAllCarByEtc():
    text = input()
    find_list = []
    for data in carwash_records:
        if data[3] == text.replace(" ", ''):
            find_list.append(data)
            print(find_list)
            return True
    return False


def ReviseCost():
    pass


def ReviseCarNum():
    pass


def ReviseCarEtc():
    pass



if __name__ == '__main__':
    # for text in test_str:
    #     carNum, cost, etc = car_re.search(text).groups()
    #     carwash_records.append((carNum.replace(" ",''), cost, etc))
    # WriteFile()
    ReadFile('carlist.txt')
    PrintAll()
    DeleteCarDataByCarNum()
    PrintAll()
