#Вариант 14. Конвейер сборки состоит из 10 технологических мест. На 4 из них требуется силовая подготовка (мужчины).
#Конвейер должен работать в 2 смены. Сформировать все возможные варианты рабочего расписания, если в цехе работает 20 рабочих: 12 женщин и 8 мужчин.

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import time

shift = 'M' * 4 + 'W' * 6


def shift_o_matic(iterable, r=None):
    # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
    # permutations(range(3)) --> 012 021 102 120 201 210
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    if r > n:
        return
    indices = list(range(n))
    cycles = list(range(n, n - r, -1))
    yield tuple(pool[i] for i in indices[:r])
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i + 1:] + indices[i:i + 1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(pool[i] for i in indices[:r])
                break
        else:
            return


print('Пожалуйста, подождите 5-10 секунд.')

schedule = list(set(shift_o_matic(shift)))

shift_separator = []
new_shifts = []
old_shifts = []

for i in range(len(schedule)):
    shift_separator.append(str(schedule[i]).replace('(', '').replace(')', '').replace("'", "").replace(',', '').replace(' ', ''))
for i in shift_separator:
    if 'MM' not in i:
        new_shifts.append(i)
for i in range(len(schedule)):
    old_shifts.append(str(schedule[i]).replace('(', '').replace(')', '').replace("'", "").replace(',', '').replace(' ', ''))


shift_maker_window = tk.Tk()

shift_maker_window.geometry('350x300')
shift_maker_window.resizable(False, False)

shift_maker_window.title('Сменодел')

label_function_name1 = tk.Label(shift_maker_window, text='Введите 1 для выведения всех смен', font='Arial 12')
label_function_name1.place(x=20, y=30)

label_function_name2 = tk.Label(shift_maker_window, text='Введите 2 для выведения смен после указа', font='Arial 12')
label_function_name2.place(x=20, y=60)

text_box = ttk.Entry(shift_maker_window, font='Arial 12')
text_box.place(x=21, y=90)


def checker():
    return True


def inserter(controller):
    if controller == '1' and checker() is True:
        shift_maker_window.destroy()
        newWindow = tk.Tk()
        newWindow.title('Запрошенные смены')
        newWindow.geometry('240x320')
        solution_list = str(old_shifts)
        languages_var = tk.StringVar(value=solution_list)
        listbox = tk.Listbox(newWindow, listvariable=languages_var, font='Arial 12')
        listbox.pack(side='left', fill='both', expand=1)
        scrollbar = tk.Scrollbar(newWindow, orient="vertical", command=listbox.yview)
        scrollbar.pack(side='right', fill='y')

    elif controller == '2' and checker() is True:
        shift_maker_window.destroy()
        newWindow = tk.Tk()
        newWindow.title('Запрошенные смены')
        newWindow.geometry('240x320')
        solution_list = str(new_shifts)
        languages_var = tk.StringVar(value=solution_list)
        listbox = tk.Listbox(newWindow, listvariable=languages_var, font='Arial 12')
        listbox.pack(side='left', fill='both', expand=1)
        scrollbar = tk.Scrollbar(newWindow, orient="vertical", command=listbox.yview)
        scrollbar.pack(side='right', fill='y')

    else:
        tk.messagebox.showwarning(title='Ошибка!', message='Введите корректное значение!')


shift_creator = tk.Button(shift_maker_window, text='Вывести смены', font='Arial 16', command=lambda:(checker(), inserter(text_box.get())), bg='brown', fg='white', height=6)
shift_creator.place(x=87, y=125)

shift_maker_window.mainloop()

