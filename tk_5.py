# Entry виджет для ввода текста

import tkinter as tk

win = tk.Tk()
win.title('окно графического приложения')
win.geometry('800x600+500+200')
win.config(bg='#c7c7c7')
# ======================================================================================================

tk.Label(win, text='Какое-то имя').grid(row=0, column=1, sticky='NSEW')

name = tk.Entry(win)  # создали окошко для ввода текста
name.grid(row=0, column=2, sticky='NSEW')

# Valid resource names: background, bd, bg, borderwidth, cursor, exportselection, fg, font, foreground, highlightbackground,
# highlightcolor, highlightthickness, insertbackground, insertborderwidth, insertofftime, insertontime, insertwidth,
# invalidcommand, invcmd, justify, relief, selectbackground, selectborderwidth, selectforeground, show, state, takefocus,
# textvariable, validate, validatecommand, vcmd, width, xscrollcommand.
# ======================================================================================================


def get_entry():
    """ Ф-ия берет текст введенный в окошко Entry и записывает его в переменную value """
    value = name.get()
    if value:
        print(value)
    else:
        print('empty entry')


tk.Button(win, text='взять инфу из Entry', command=get_entry).grid(row=0, column=3, sticky='NSEW')
# ======================================================================================================


def delete_entry():
    # name.delete(first=0)    # удаляет с 1й позиции по 1 символу
    # name.delete(first=0, last=100)  # удаляет с 1й позиции по 100й символы
    # name.delete(0, 5)     # доступна передача параметров по позиции удаляет с 1й позиции по 5й символы
    # name.delete(0, 'end')     # доступна передача параметров по позиции удаляет с 1й позиции и до конца
    name.delete(0, tk.END)  # доступна передача параметров по позиции удаляет с 1й позиции и до конца


tk.Button(win, text='очистить', command=delete_entry).grid(row=0, column=4, sticky='NSEW')
# ======================================================================================================

# name.insert(0, 'hello') позволяет вставить текст в окошко, первый обязательный позиционный параметр (как и у delete)
# каждый раз вставка будет на 0ю позицию (hellohellohello при многократном нажатии)
# чтоб не было наслоений следует сперва удалить текст, а потом вставить
tk.Button(win, text='вставить текст', command=lambda : name.insert(0, 'hello')).grid(row=0, column=5, sticky='NSEW')

# ======================================================================================================

tk.Label(win, text='Пароль').grid(row=1, column=0, sticky='NSEW')
password = tk.Entry(win, show='*')
password.grid(row=1, column=1, sticky='NSEW')

def submit():
    print(name.get())
    print(password.get())
    delete_entry()

tk.Button(win, text='Submit', command=submit).grid(row=1, column=2, sticky='NSEW')


win.grid_columnconfigure(0, minsize=100)
win.grid_columnconfigure(1, minsize=100)
# win.grid_rowconfigure(0, minsize=100)


win.mainloop()  # вывели окно
