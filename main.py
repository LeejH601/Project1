import Carlist
from tkinter import *
from tkinter.ttk import *
from tkinter.scrolledtext import ScrolledText
from functools import partial


def stop(event=None):
    main_window.quit()


def addData(container, entry_box, c_list):
    text = entry_box.get()
    if container.InsertCarData(text):
        c_list.delete(0,END)
        for no, carNum, cost, etc in container.carwash_records:
            c_list.insert(END, f'{no} {carNum} {cost} {etc}')
    entry_box.delete(0, END)


def FindData(container):
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
            cars_list.delete(0, END)
            for no, carNum, cost, etc in result:
                cars_list.insert(END, f'{no} {carNum} {cost} {etc}')
            quit_child()
            return result
        return None

    Button(child_window, text='번호로 검색', command=partial(finditme, 0)).pack(side=LEFT, expand=True, fill=BOTH, padx=5, pady=2)
    Button(child_window, text='비용으로 검색', command=partial(finditme, 1)).pack(side=LEFT, expand=True, fill=BOTH, padx=5, pady=2)
    Button(child_window, text='기타', command=partial(finditme, 2)).pack(side=LEFT, expand=True, fill=BOTH, padx=5, pady=2)

    child_window.mainloop()


if __name__ == '__main__':
    # for text in test_str:
    #     carNum, cost, etc = car_re.search(text).groups()
    #     carwash_records.append((carNum.replace(" ",''), cost, etc))
    # WriteFile()
    wash_list = Carlist.carlist()
    wash_list.ReadFile('carlist.txt')

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

    list_label = Label(second_label_frame, text='carList')
    list_label.pack(padx=5)

    cars_list = Listbox(second_label_frame, height=20)
    for no, carNum, cost, etc in wash_list.carwash_records:
        cars_list.insert(END, f'{no} {carNum} {cost} {etc}')
    cars_list.pack(fill=BOTH, padx=5, pady=5)

    third_label_frame = LabelFrame()
    third_label_frame.pack(fill=BOTH, padx=5, pady=5)

    Button(third_label_frame, text='추가', command=partial(addData, wash_list, data_entry, cars_list)).pack(side=LEFT, expand=True, fill=BOTH, padx=5, pady=2)
    Button(third_label_frame, text='검색', command=partial(FindData, wash_list)).pack(side=LEFT, expand=True, fill=BOTH, padx=5, pady=2)
    Button(third_label_frame, text='삭제', ).pack(side=LEFT, expand=True, fill=BOTH, padx=5, pady=2)

    main_window.mainloop()
