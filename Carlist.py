import os
import re
import exrex
import time
import datetime




# test_str = [exrex.getone(final_pattern, 5) for _ in range(1000)]

class carlist:
    carwash_records = []

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

    def __init__(self):
        pass


    def ReadFile(self, fileName):
        f = open(fileName, 'r')
        No = 1
        while True:
            data = f.readline()
            if data:
                carNum, cost, etc = self.car_re.search(data).groups()
                self.carwash_records.append([No, carNum.replace(" ",''), cost, etc])
                No += 1
            else:
                break


    def WriteFile(self, fileName):
        f = open(fileName, 'w')
        for data in self.carwash_records:
            f.write(str(data[0] + data[1] + data[2])+'\n')
        f.close()


    def InsertCarData(self):
        text = input()
        mo = self.car_re.search(text)
        if mo:
            self.carwash_records.append(list(mo.groups()))
        else:
            print('형식이 올바르지 않음.')



    def PrintAll(self):
        No = 1
        for data in self.carwash_records:
            print(format(f"{data[0]:4}\t{data[1]:>8}\t{data[2]:>5}\t{data[3]}"))
            No += 1


    def ShowOne(self, data):
        print(format(f"{data[0]:4}\t{data[1]:>8}\t{data[2]:>5}\t{data[3]}"))


    def DeleteCarDataByCarNum(self):
        text = input()
        find_list = []
        for data in self.carwash_records:
            if data[1] == text.replace(" ", ''):
                find_list.append(data)
        if not find_list:
            return False
        for d in find_list:
            self.carwash_records.remove(d)
        self.RenameNums()
        return True



    def DeleteAllCarByCost(self):
        text = input()
        find_list = []
        for data in self.carwash_records:
            if data[2] == text.replace(" ", ''):
                find_list.append(data)
        if not find_list:
            return False
        for d in find_list:
            self.carwash_records.remove(d)
        self.RenameNums()
        return True


    def DeleteAllCarByEtc(self):
        text = input()
        find_list = []
        for data in self.carwash_records:
            if data[3] == text.replace(" ", ''):
                find_list.append(data)
        if not find_list:
            return False
        for d in find_list:
            self.carwash_records.remove(d)
        self.RenameNums()
        return True


    def FindCarDataByCarNum(self):
        text = input()
        find_list = []
        for data in self.carwash_records:
            if data[1] == text.replace(" ", ''):
                find_list.append(data)
                return find_list
        return None


    def FindAllCarByCost(self):
        text = input()
        find_list = []
        for data in self.carwash_records:
            if data[2] == text.replace(" ", ''):
                find_list.append(data)
                return find_list
        return None


    def FindAllCarByEtc(self):
        text = input()
        find_list = []
        for data in self.carwash_records:
            if data[3] == text.replace(" ", ''):
                find_list.append(data)
                return find_list
        return None


    def ReviseCost(self):
        pass


    def ReviseCarNum(self):
        pass


    def ReviseCarEtc(self):
        pass


    def RenameNums(self):
        no = 1
        for data in self.carwash_records:
            data[0] = no
            no += 1