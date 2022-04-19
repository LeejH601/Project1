import Carlist

if __name__ == '__main__':
    # for text in test_str:
    #     carNum, cost, etc = car_re.search(text).groups()
    #     carwash_records.append((carNum.replace(" ",''), cost, etc))
    # WriteFile()
    c_list = Carlist.carlist()
    c_list.ReadFile('carlist.txt')
    c_list.PrintAll()
    c_list.DeleteAllCarByEtc()
    c_list.PrintAll()
