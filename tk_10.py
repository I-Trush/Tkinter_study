# виджеты, Checkbox

import tkinter as tk

win = tk.Tk()
win.title('окно графического приложения')
win.geometry('500x600+500+200')
win.config(bg='#c7c7c7')
# ======================================================================================================


str_var = tk.StringVar()
str_var.set('выкл')  # можно установить флажек в позицию по умолчанию, через значение переменной

int_var = tk.IntVar()


def select_all():
    for check in [check_1, check_2, check_3]:
        check.select()


def unselect_all():
    for check in [check_1, check_2, check_3]:
        check.deselect()


def switch_all():
    for check in [check_1, check_2, check_3]:
        check.toggle()


def show_value():
    print('флажек установлен в позицию:', str_var.get())
    print('флажек установлен в позицию:', int_var.get())



check_1 = tk.Checkbutton(win, text='сообщение 1', variable=str_var, # variable=str_var запись позиции флажка в переменной
                         offvalue = 'выкл', onvalue='вкл')  # флажек, offvalue = 'выкл', onvalue='вкл' значения переменной
check_2 = tk.Checkbutton(win, text='сообщение 2', variable=int_var,
                         offvalue = 0, onvalue=11)
check_3 = tk.Checkbutton(win, text='сообщение 3', indicatoron=0)  # флажок отображается в виде кнопки, которую можно зажать и отжать

# Valid resource names: activebackground, activeforeground, anchor, background, bd, bg, bitmap, borderwidth, command, cursor,
# disabledforeground, fg, font, foreground, height, highlightbackground, highlightcolor, highlightthickness, image,
# indicatoron, justify, offvalue, onvalue, padx, pady, relief, selectcolor, selectimage, state, takefocus, text, textvariable,
# underline, variable, width, wraplength.


check_1.grid(row=0, column=1)
check_2.grid(row=1, column=1)
check_3.grid(row=2, column=1)

tk.Button(win, text='select_all', command=select_all).grid(row=0, column=0)
tk.Button(win, text='unselect_all', command=unselect_all).grid(row=1, column=0)
tk.Button(win, text='switch', command=switch_all).grid(row=2, column=0)
tk.Button(win, text='show_value', command=show_value).grid(row=3, column=0)

win.mainloop()
