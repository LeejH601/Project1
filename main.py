import os
import re
import exrex


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
    while True:
        data = f.readline()
        if data:
            carNum, cost, etc = car_re.search(data).groups()
            carwash_records.append((carNum.replace(" ",''), cost, etc))
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



def SearchCarData():
    text = input()
    find_list = []
    for data in carwash_records:
        if data[0] == text.replace(" ", ''):
            find_list.append(data)
    print(data)


def DeleteCarDataByCarNum():
    pass


def DeleteAllCarByCost():
    pass


def DeleteAllCarByEtc():
    pass


def FindCarDataByCarNum():
    pass


def FindAllCarByCost():
    pass


def FindAllCarByEtc():
    pass


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
    for data in carwash_records:
        print(data)
