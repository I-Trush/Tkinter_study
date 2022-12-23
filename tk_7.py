# Калькулятор

import tkinter as tk

win = tk.Tk()
win.title('калькулятор')
win.geometry('800x600+500+200')
win['bg'] = '#c7c7c7'  # можно и так задать цвет
# ======================================================================================================

calc = tk.Entry(win, font=('Arial', 25, 'bold'), justify=tk.RIGHT)  # justify=tk.RIGHT прижали цифры к правому краю
calc.insert(0, 0)
calc.grid(row=0, column=0, columnspan=4, sticky='NEWS')


def add_digit(arg):
    value = calc.get()
    if value == '0':
        calc.delete(0, 1)
    calc.insert(tk.END, arg)  # добавляем новую цифру в конец


def make_digit_button(arg):
    return tk.Button(text=arg, bd=5, font=('Arial', 20, 'bold'), command=lambda: add_digit(arg))


def add_cansel():
    calc.delete(0, tk.END)
    calc.insert(0, 0)


def add_operand(operand):
    value = calc.get()
    if value[-1] in '+-*/':
        value = value[:-1]
    calc.delete(0, tk.END)
    calc.insert(0, value + operand)  # т.к. ф-ия в tk.Button записана с круклыми скобками она вызывает все знаки и в конце знак (=)
    # так происходит из-за tk.Button(text=arg, font=('Arial', 20, 'bold'), bd=5, command=add_operand(arg))
    # т.е. вызов через lambda предохраняет от авто активации


def make_operation_button(arg):
    return tk.Button(text=arg, font=('Arial', 20, 'bold'), bd=5, command=lambda: add_operand(arg))


make_digit_button(1).grid(row=1, column=0, sticky='NSEW', padx=5, pady=5)
make_digit_button(2).grid(row=1, column=1, sticky='NSEW', padx=5, pady=5)
make_digit_button(3).grid(row=1, column=2, sticky='NSEW', padx=5, pady=5)
make_digit_button(4).grid(row=2, column=0, sticky='NSEW', padx=5, pady=5)
make_digit_button(5).grid(row=2, column=1, sticky='NSEW', padx=5, pady=5)
make_digit_button(6).grid(row=2, column=2, sticky='NSEW', padx=5, pady=5)
make_digit_button(7).grid(row=3, column=0, sticky='NSEW', padx=5, pady=5)
make_digit_button(8).grid(row=3, column=1, sticky='NSEW', padx=5, pady=5)
make_digit_button(9).grid(row=3, column=2, sticky='NSEW', padx=5, pady=5)
make_digit_button(0).grid(row=4, column=0, sticky='NSEW', padx=5, pady=5)

make_operation_button('+').grid(row=1, column=3, sticky='NSEW', padx=5, pady=5)
make_operation_button('-').grid(row=2, column=3, sticky='NSEW', padx=5, pady=5)
make_operation_button('*').grid(row=3, column=3, sticky='NSEW', padx=5, pady=5)
make_operation_button('/').grid(row=4, column=3, sticky='NSEW', padx=5, pady=5)

make_operation_button('=').grid(row=4, column=2, sticky='NSEW', padx=5, pady=5)
tk.Button(text='C', font=('Arial', 20, 'bold'), bd=5, command=add_cansel).grid(row=4, column=1, sticky='NSEW', padx=5, pady=5)

for i in range(5):
    win.grid_columnconfigure(i, minsize=50)
    win.grid_rowconfigure(i, minsize=50)

win.mainloop()  # вывели окно
