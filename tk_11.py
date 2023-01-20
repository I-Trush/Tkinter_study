# виджеты, Radiobutton

import tkinter as tk

win = tk.Tk()
win.title('окно графического приложения')
win.geometry('500x600+500+200')
win.config(bg='#c7c7c7')
# ======================================================================================================

# изначально 3 флажка tk.Radiobutton не связаны, их необходимо связать через переменную lelel_var
level_var = tk.IntVar()
race_var = tk.IntVar()
lvl_txt = tk.StringVar()
dict_lvl = {1:'Easy', 2:'Middle', 3:'Hard'}

def select_lvl():
    lvl = level_var.get()
    print(dict_lvl[lvl])
    lvl_txt.set(dict_lvl[lvl])  # tk.переменные через '=' не присваиваются, только через методы класса

tk.Label(win, text='выберите уровень сложности').pack()
# tk.Radiobutton(win, text='Easy', variable=level_var, value=1, command=select_lvl).pack()    # variable -переменная, value - её значение, которое будет установлено при выборе данного пункта
# tk.Radiobutton(win, text='Middle', variable=level_var, value=2, command=select_lvl).pack()
# tk.Radiobutton(win, text='Hard', variable=level_var, value=3, command=select_lvl).pack()

# Valid resource names: activebackground, activeforeground, anchor, background, bd, bg, bitmap, borderwidth, command, cursor,
# disabledforeground, fg, font, foreground, height, highlightbackground, highlightcolor, highlightthickness, image, indicatoron, justify,
# padx, pady, relief, selectcolor, selectimage, state, takefocus, text, textvariable, underline, value, variable, width, wraplength.

for key in sorted(dict_lvl):
    tk.Radiobutton(win, text=dict_lvl[key], variable=level_var, value=key, command=select_lvl).pack()


tk.Label(win, textvariable=lvl_txt).pack()


tk.Label(win, text='выберите рассу').pack()
tk.Radiobutton(win, text='Эльфы', variable=race_var, value=1, command=select_lvl).pack()
tk.Radiobutton(win, text='Люди', variable=race_var, value=2, command=select_lvl).pack()
tk.Radiobutton(win, text='Орки', variable=race_var, value=3, command=select_lvl).pack()


win.mainloop()
