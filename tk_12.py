# виджеты, Combobox - Выпадающий список

import tkinter as tk

# Combobox и другие виджеты содержаться в tkinter.ttk
from tkinter import ttk

win = tk.Tk()
win.title('окно графического приложения')
win.geometry('500x600+500+200')
win.config(bg='#c7c7c7')
# ======================================================================================================


weekDays = [1, 2, 3, 4, 5, 6, 7]

combo = ttk.Combobox(win, values=weekDays)
combo.current(0)  # значение из списка, которое будет выводиться в качестве default
combo.pack()



win.mainloop()
