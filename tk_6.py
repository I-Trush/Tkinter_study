# Калькулятор

import tkinter as tk

win = tk.Tk()
win.title('калькулятор')
win.geometry('800x600+500+200')
win['bg'] = '#c7c7c7'       # можно и так задать цвет
#======================================================================================================

calc = tk.Entry(win, font=('Arial', 25, 'bold'), justify=tk.RIGHT)  # justify=tk.RIGHT прижали цифры к правому краю
calc.grid(row=0, column=0, columnspan=4 ,sticky='NEWS')


def add_digit(arg):
    calc.insert(tk.END, arg)    # добавляем новую цифру в конец


tk.Button(text=1, bd=5, font=('Arial', 20, 'bold'), command=lambda : add_digit(1)).grid(row=1, column=0, sticky='NSEW',padx=5, pady=5)
tk.Button(text=2, bd=5, font=('Arial', 20, 'bold'), command=lambda : add_digit(2)).grid(row=1, column=1, sticky='NSEW',padx=5, pady=5)
tk.Button(text=3, bd=5, font=('Arial', 20, 'bold'), command=lambda : add_digit(3)).grid(row=1, column=2, sticky='NSEW',padx=5, pady=5)
tk.Button(text=4, bd=5, font=('Arial', 20, 'bold'), command=lambda : add_digit(4)).grid(row=2, column=0, sticky='NSEW',padx=5, pady=5)
tk.Button(text=5, bd=5, font=('Arial', 20, 'bold'), command=lambda : add_digit(5)).grid(row=2, column=1, sticky='NSEW',padx=5, pady=5)
tk.Button(text=6, bd=5, font=('Arial', 20, 'bold'), command=lambda : add_digit(6)).grid(row=2, column=2, sticky='NSEW',padx=5, pady=5)
tk.Button(text=7, bd=5, font=('Arial', 20, 'bold'), command=lambda : add_digit(7)).grid(row=3, column=0, sticky='NSEW',padx=5, pady=5)
tk.Button(text=8, bd=5, font=('Arial', 20, 'bold'), command=lambda : add_digit(8)).grid(row=3, column=1, sticky='NSEW',padx=5, pady=5)
tk.Button(text=9, bd=5, font=('Arial', 20, 'bold'), command=lambda : add_digit(9)).grid(row=3, column=2, sticky='NSEW',padx=5, pady=5)
tk.Button(text=0, bd=5, font=('Arial', 20, 'bold'), command=lambda : add_digit(0)).grid(row=4, column=0, sticky='NSEW',padx=5, pady=5, columnspan=2)

tk.Button(text='+', font=('Arial', 20, 'bold'), bd=5).grid(row=1, column=3, sticky='NSEW', padx=5, pady=5)
tk.Button(text='-', font=('Arial', 20, 'bold'), bd=5).grid(row=2, column=3, sticky='NSEW', padx=5, pady=5)
tk.Button(text='*', font=('Arial', 20, 'bold'), bd=5).grid(row=3, column=3, sticky='NSEW', padx=5, pady=5)
tk.Button(text='/', font=('Arial', 20, 'bold'), bd=5).grid(row=4, column=3, sticky='NSEW', padx=5, pady=5)
tk.Button(text='=', font=('Arial', 20, 'bold'), bd=5).grid(row=4, column=2, sticky='NSEW', padx=5, pady=5)


for i in range(5):
    win.grid_columnconfigure(i, minsize=50)
    win.grid_rowconfigure(i, minsize=50)


win.mainloop()  # вывели окно
