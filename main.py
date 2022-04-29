import datetime
import tkinter.messagebox
import os
import Carlist
from tkinter import *
from tkinter.ttk import *
from tkinter.scrolledtext import ScrolledText
from functools import partial
from tkinter import filedialog


def stop(event=None):
    main_window.quit()


def reset_list(container, c_list):
    c_list.delete(0, END)
    for no, carNum, cost, etc in container.carwash_records:
        if not cost == '0000':
            c_list.insert(END, f'{no} {carNum} {cost} {etc}')
        else:
            c_list.insert(END, f'{no} {carNum} {etc}')


def addData(container, entry_box, c_list, b_list, a_cont):
    text = entry_box.get()
    mo = container.car_re.search(text)
    if b_list.FindCarDataByCarNum( mo.group(1)):
        if not tkinter.messagebox.askokcancel("attention","블랙 리스트에 등록된 차량입니다. 등록하시겠습니까?"):
            return
    if container.InsertCarData(text):
        if a_cont.FindCarDataByCarNum(container.carwash_records[container.nCars-1][1] ):
            container.carwash_records[container.nCars - 1][2] = str(int(0.7 * int(container.carwash_records[container.nCars - 1][2])))
        c_list.delete(0,END)
        for no, carNum, cost, etc in container.carwash_records:
            c_list.insert(END, f'{no} {carNum} {cost} {etc}')
    entry_box.delete(0, END)


def addData_managements(container, entry_box, c_list):
    text = entry_box.get()
    if container.InsertCarData(text):
        c_list.delete(0,END)
        for no, carNum, cost, etc in container.carwash_records:
            c_list.insert(END, f'{no} {carNum} {etc}')
    entry_box.delete(0, END)


def deleteData(container, entry_box, c_list):
    child_window = Tk()
    child_window.geometry('+0+0')
    child_window.resizable(False, False)

    def quit_child(event=None):
        child_window.quit()
        child_window.destroy()

    child_window.bind('<Escape>', quit_child)

    target_entry = Entry(child_window)
    target_entry.pack()

    def deleteItem(case):
        text = target_entry.get()
        if case == 0:
            result = container.DeleteCarDataByCarNum(text)
        elif case == 1:
            result = container.DeleteAllCarByCost(text)
        elif case == 2:
            result = container.DeleteAllCarByEtc(text)
        if result:
            c_list.delete(0, END)
            for no, carNum, cost, etc in container.carwash_records:
                if not cost == '0000':
                    c_list.insert(END, f'{no} {carNum} {cost} {etc}')
                else:
                    c_list.insert(END, f'{no} {carNum} {etc}')
            quit_child()
            return result
        return None

    Button(child_window, text='번호로 삭제', command=partial(deleteItem, 0)).pack(side=LEFT, expand=True, fill=BOTH, padx=5,
                                                                           pady=2)
    if not type(container) == Carlist.managemnetList:
        Button(child_window, text='비용으로 일괄 삭제', command=partial(deleteItem, 1)).pack(side=LEFT, expand=True, fill=BOTH, padx=5,
                                                                          pady=2)
    Button(child_window, text='기타 일괄 삭제', command=partial(deleteItem, 2)).pack(side=LEFT, expand=True, fill=BOTH, padx=5,
                                                                       pady=2)

    child_window.mainloop()


def FindData(container, c_list):
    child_window = Tk()
    child_window.geometry('+0+0')
    child_window.resizable(False, False)

    def quit_child(event=None):
        child_window.quit()
        child_window.destroy()

    child_window.bind('<Escape>', quit_child)

    target_entry = Entry(child_window)
    target_entry.pack()

    def finditme(case):
        text = target_entry.get()
        if case == 0:
            result = container.FindCarDataByCarNum(text)
        elif case == 1:
            result = container.FindAllCarByCost(text)
        elif case == 2:
            result = container.FindAllCarByEtc(text)
        if result:
            c_list.delete(0, END)
            for no, carNum, cost, etc in result:
                if not cost == '0000':
                    c_list.insert(END, f'{no} {carNum} {cost} {etc}')
                else:
                    c_list.insert(END, f'{no} {carNum} {etc}')
            quit_child()
            return result
        return None

    Button(child_window, text='번호로 검색', command=partial(finditme, 0)).pack(side=LEFT, expand=True, fill=BOTH, padx=5, pady=2)
    if not type(container) == Carlist.managemnetList:
        Button(child_window, text='비용으로 검색', command=partial(finditme, 1)).pack(side=LEFT, expand=True, fill=BOTH, padx=5, pady=2)
    Button(child_window, text='기타', command=partial(finditme, 2)).pack(side=LEFT, expand=True, fill=BOTH, padx=5, pady=2)

    child_window.mainloop()


def managementList(managementList, window_name):
    child_window = Tk()
    child_window.title(window_name)
    child_window.geometry('300x500+0+0')
    child_window.resizable(False, False)

    def quit_child(event=None):
        managementList.WriteFile()
        child_window.quit()
        child_window.destroy()

    child_window.bind('<Escape>', quit_child)
    child_window.protocol("WM_DELETE_WINDOW", quit_child)

    b_entry_frame = LabelFrame(child_window)
    b_entry_frame.pack(padx=5)

    b_entry_label = Label(b_entry_frame, text='input')
    b_entry_label.pack(padx=5)

    b_data_entry = Entry(b_entry_frame, width=70)
    b_data_entry.pack(padx=5, pady=5)

    b_cars_list = Listbox(child_window, height=20)
    for no, carNum, cost, etc in managementList.carwash_records:
        b_cars_list.insert(END, f'{no} {carNum} {etc}')
    b_cars_list.pack(fill=BOTH, padx=5, pady=5)

    b_label_frame = LabelFrame(child_window)
    b_label_frame.pack( padx=5)

    Button(b_label_frame, text='추가', command=partial(addData_managements, managementList, b_data_entry, b_cars_list)).pack(\
        side=LEFT, expand=True, fill=BOTH, padx=5, pady=2)
    Button(b_label_frame, text='검색', command=partial(FindData, managementList, b_cars_list)).pack(side=LEFT, expand=True, \
                                                                                    fill=BOTH,padx=5, pady=2)
    Button(b_label_frame, text='삭제', command=partial(deleteData, managementList, data_entry, b_cars_list)).pack(\
        side=LEFT,expand=True,fill=BOTH,padx=5,pady=2)

    Button(child_window, text='초기화', command=partial(reset_list, managementList, b_cars_list)).pack(side=BOTTOM, expand=True,\
                                                                                       fill=BOTH, padx=5, pady=2)

    child_window.mainloop()


def open_file(container, c_list, r_filename):
    file_name = filedialog.askopenfilename(title='Select text files',
                                           filetypes=(("text files (.txt)", "*.txt"), ("all files", "*.*")))
    container.ReadFile(file_name)
    container.filename = file_name
    fn = file_name.split('/')
    list_text.set('carList - ' + fn[len(fn)-1][:-4])
    reset_list(container, c_list)


def save_file(container, filename):
    container.WriteFile(filename)


if __name__ == '__main__':
    if not 'config.txt' in os.listdir():
        open('config.txt', 'w').close()
    conf_f = open('config.txt', 'r')

    openfilename = ''
    file_info = []

    if not 'washdatas' in os.listdir():
        os.mkdir('washdatas')
    for root, subfolder, filenames in os.walk('/washdatas'):
        for fn in filenames:
            file_info.append((root, subfolder, fn))

    while not openfilename:
        data = conf_f.readline()
        if not data:
            currentTime = datetime.datetime.now()
            openfilename = 'washdatas/wash_' + currentTime.strftime('%Y%m%d') +'.txt'
            f = open(openfilename, 'w')
            f.close()
            conf_f.close()
            conf_f = open('config.txt', 'w')
            conf_f.write(openfilename)
            break
        openfilename = data
    conf_f.close()

    wash_list = Carlist.carlist()
    wash_list.ReadFile(openfilename)

    black_list = Carlist.managemnetList()
    if not 'blacklist.txt' in os.listdir():
        open('blacklist.txt', 'w').close()
    black_list.ReadFile('blacklist.txt')

    account_list = Carlist.managemnetList()
    if not 'accountlist.txt' in os.listdir():
        open('accountlist.txt', 'w').close()
    account_list.ReadFile('accountlist.txt')

    text_car_List = ''

    for no, carNum, cost, etc in wash_list.carwash_records:
        text_car_List += f'{no} {carNum} {cost} {etc}\n'

    main_window = Tk()
    main_window.title('CarList')
    main_window.geometry('+0+0')
    main_window.resizable(False, False)
    main_window.bind('<Escape>', stop)

    first_label_frame = LabelFrame()
    first_label_frame.pack(padx=5, pady=5)

    entry_label = Label(first_label_frame, text='input')
    entry_label.pack(padx=5)

    data_entry = Entry(first_label_frame,width=70)
    # data_entry.bind('<Return>', )
    data_entry.pack(padx=5, pady=5)

    second_label_frame = LabelFrame()
    second_label_frame.pack(fill=BOTH, padx=5, pady=5)

    list_text = StringVar()

    fn = openfilename.split('/')
    list_text.set('carList - ' + fn[len(fn)-1][:-4])

    list_label = Label(second_label_frame, textvariable=list_text)
    list_label.pack(padx=5)

    cars_list = Listbox(second_label_frame, height=20)
    for no, carNum, cost, etc in wash_list.carwash_records:
        cars_list.insert(END, f'{no} {carNum} {cost} {etc}')
    cars_list.pack(fill=BOTH, padx=5, pady=5)

    third_label_frame = LabelFrame()
    third_label_frame.pack(fill=BOTH, padx=5, pady=5)

    Button(third_label_frame, text='추가', command=partial(addData, wash_list, data_entry, cars_list, black_list, account_list)).pack(side=LEFT, expand=True, fill=BOTH, padx=5, pady=2)
    Button(third_label_frame, text='검색', command=partial(FindData, wash_list, cars_list)).pack(side=LEFT, expand=True, fill=BOTH, padx=5, pady=2)
    Button(third_label_frame, text='삭제', command=partial(deleteData, wash_list, data_entry, cars_list)).pack(side=LEFT, expand=True, fill=BOTH, padx=5, pady=2)
    Button(third_label_frame, text='초기화', command=partial(reset_list, wash_list, cars_list)).pack(side=LEFT, expand=True, fill=BOTH, padx=5, pady=2)

    fourth_label_frame = LabelFrame()
    fourth_label_frame.pack(fill=BOTH, padx=5, pady=2)

    Button(fourth_label_frame, text='블랙리스트', command=partial(managementList, black_list, 'blackList')).pack(side=LEFT,expand=True,fill=BOTH,padx=5,pady=2)
    Button(fourth_label_frame, text='거래처', command=partial(managementList, account_list, 'accountList')).pack(side=LEFT,expand=True,fill=BOTH,padx=5,pady=2)

    menu = Menu()
    menu_file = Menu(menu, tearoff=False)
    menu_file.add_command(label='Open', command=partial(open_file, wash_list, cars_list,  openfilename), accelerator='Ctrl+o')
    menu_file.add_command(label='Save File', command=partial(save_file, wash_list, None), accelerator='Ctrl+s')
    menu_file.add_separator()
    menu_file.add_command(label='Quit', accelerator='Ctrl+q')

    menu.add_cascade(label='File', menu=menu_file)

    main_window.config(menu=menu)

    main_window.mainloop()
