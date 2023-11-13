#Вариант 14. Конвейер сборки состоит из 10 технологических мест. На 4 из них требуется силовая подготовка (мужчины).
#Конвейер должен работать в 2 смены. Сформировать все возможные варианты рабочего расписания, если в цехе работает 20 рабочих: 12 женщин и 8 мужчин.

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

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

schedule = list(set(shift_o_matic(shift)))

shift_separator = []
new_shifts = []

for i in range(len(schedule)):
    shift_separator.append(str(schedule[i]).replace('(', '').replace(')', '').replace("'", "").replace(',', '').replace(' ', ''))
for i in shift_separator:
    if not 'MM' in i:
        new_shifts.append(i)


shift_maker_window = tk.Tk()

shift_maker_window.geometry('350x350')
shift_maker_window.resizable(False, False)

shift_maker_window.title('Сменодел')
label_function_name = tk.Label(shift_maker_window, text='Все возможные смены', font='Arial 16')
label_function_name.place(x=55, y=50)


def inserter(controller):
    if controller:
        newWindow = tk.Toplevel(shift_maker_window)
        newWindow.title('Все возможные смены')
        newWindow.geometry('240x320')
        solution_list = str(new_shifts)
        languages_var = tk.StringVar(value=solution_list)
        listbox = tk.Listbox(newWindow, listvariable=languages_var, font= 'Arial 12')
        listbox.pack(side='left', fill='both', expand=1)
        scrollbar = tk.Scrollbar(newWindow, orient="vertical", command=listbox.yview)
        scrollbar.pack(side='right', fill='y')


def checker():
    return True


shift_creator = tk.Button(shift_maker_window, text='Вывести смены', font='Arial 16', command=lambda:(checker(), inserter(checker)), bg='brown', fg='white', height=6)
shift_creator.place(x=87, y=125)


shift_maker_window.mainloop()

