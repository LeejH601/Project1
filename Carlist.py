import os
import re
import exrex
import time
import datetime





class carlist:
    car_re = re.compile(r'''
    ^
    (\d{2,3}    
    [ ]*
    [가-힣]
    [ ]*
    \d{4})
    [ ]*
    (\d{4})
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
    (\d
    000)
    [ ]*
    (.*)
    '''

    final_pattern = re.sub(r'[ ]{2,}|\t|\n', '', pattern)

    def __init__(self):
        self.carwash_records = []
        self.nCars = 0

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
        self.nCars= len(self.carwash_records)
        f.close()


    def WriteFile(self, fileName):
        f = open(fileName, 'w')
        for data in self.carwash_records:
            f.write(str(data[1]) + str(data[2]) + str(data[3])+'\n')
        f.close()


    def InsertCarData(self, text):
        mo = self.car_re.search(text)
        if mo:
            self.nCars += 1
            self.carwash_records.append([self.nCars, mo.group(1), mo.group(2), mo.group(3)])
            return True
        else:
            print('형식이 올바르지 않음.')
        return False


    def PrintAll(self):
        No = 1
        for data in self.carwash_records:
            print(format(f"{data[0]:4}\t{data[1]:>8}\t{data[2]:>5}\t{data[3]}"))
            No += 1


    def ShowOne(self, data):
        print(format(f"{data[0]:4}\t{data[1]:>8}\t{data[2]:>5}\t{data[3]}"))


    def DeleteCarDataByCarNum(self,text):
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



    def DeleteAllCarByCost(self, text):
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


    def DeleteAllCarByEtc(self, text):
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


    def FindCarDataByCarNum(self, text):
        find_list = []
        for data in self.carwash_records:
            if data[1] == text.replace(" ", ''):
                find_list.append(data)
                print(find_list)
                return find_list
        return None


    def FindAllCarByCost(self, text):
        find_list = []
        for data in self.carwash_records:
            if data[2] == text.replace(" ", ''):
                find_list.append(data)
                return find_list
        return None


    def FindAllCarByEtc(self, text):
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
        self.nCars = no-1


class managemnetList(carlist):
    manage_re = re.compile(r'''
        ^
        (\d{2,3}    
        [ ]*
        [가-힣]
        [ ]*
        \d{4})
        [ ]*
        (.*)
        ''', re.VERBOSE)

    def __init__(self):
        super(managemnetList, self).__init__()

    def InsertCarData(self, text):
        mo = self.manage_re.search(text)
        if mo:
            self.nCars += 1
            self.carwash_records.append([self.nCars, mo.group(1), '0000', mo.group(2)])
            return True
        else:
            print('형식이 올바르지 않음.')
        return False


if __name__ == '__main__':
    test_str = [exrex.getone(carlist.final_pattern, 5) for _ in range(10)]

    test_c = carlist()
    for text in test_str:
        test_c.InsertCarData(text)
    test_c.WriteFile('accountlist.txt')