# Калькулятор

import tkinter as tk

win = tk.Tk()
win.title('калькулятор')
win.geometry('800x600+500+200')
win['bg'] = '#c7c7c7'  # можно и так задать цвет
# ======================================================================================================

calc = tk.Entry(win, font=('Arial', 25, 'bold'), justify=tk.RIGHT)  # justify=tk.RIGHT прижали цифры к правому краю
# background, bd, bg, borderwidth, cursor, exportselection, fg, font, foreground, highlightbackground, highlightcolor,
# highlightthickness, insertbackground, insertborderwidth, insertofftime, insertontime, insertwidth, invalidcommand,
# invcmd, justify, relief, selectbackground, selectborderwidth, selectforeground, show, state, takefocus, textvariable,
# validate, validatecommand, vcmd, width, xscrollcommand.
calc.insert(0, 0)
calc.grid(row=0, column=0, columnspan=4, sticky='NEWS')


# ======================================================================================================
def validator(Param):
    """Validates the input.
    Args:
        P (int): the value the text would have after the change.
    Returns:
        bool: True if the input is digit-only or empty, and False otherwise.
    """
    return Param.isdigit() or Param == "" or Param in '/*-+' or Param =='\r'


calc.configure(
    validate="key",
    validatecommand=(win.register(validator))   # при этом нолик в начале строки не стирается, и это приводит к ошибке
)
# ======================================================================================================


def press_key(event):
    print(repr(event.char))
    if event.char.isdigit():
        add_digit(event.char)
    elif event.char in '/*-+':
        add_operand(event.char)
    elif event.char == '\r':
        calculate()
    else:
        pass


win.bind('<Key>', press_key)    # func press_key вызывается если одно из событий происходит \\ <Key> имя события чувствительно к регистру \\ передает параметр event в ф-ию
# Control, Mod2, M2, Shift, Mod3, M3, Lock, Mod4, M4, Button1, B1, Mod5, M5 Button2, B2, Meta, M, Button3,
# B3, Alt, Button4, B4, Double, Button5, B5 Triple, Mod1, M1. TYPE is one of Activate, Enter, Map,
# ButtonPress, Button, Expose, Motion, ButtonRelease FocusIn, MouseWheel, Circulate, FocusOut, Property,
# Colormap, Gravity Reparent, Configure, KeyPress, Key, Unmap, Deactivate, KeyRelease Visibility, Destroy, Leave and DETAIL


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


def calculate():
    value = calc.get()  # создается копия
    if value[-1] in '+-*/':
        operation = value[-1]
        value = value[:-1] + operation + value[:-1]
    calc.delete(0, tk.END)
    calc.insert(0, eval(value))


def add_operand(operand):
    value = calc.get()
    if value[-1] in '+-*/':
        value = value[:-1]
    elif '/' in value or '*' in value or '-' in value or '+' in value:
        calculate()
        value = calc.get()
    calc.delete(0, tk.END)
    calc.insert(0, value + operand)  # т.к. ф-ия в tk.Button записана с круклыми скобками она вызывает все знаки и в конце знак (=)
    # так происходит из-за tk.Button(text=arg, font=('Arial', 20, 'bold'), bd=5, command=add_operand(arg))
    # т.е. вызов через lambda предохраняет от авто активации


def make_operation_button(arg):
    return tk.Button(text=arg, font=('Arial', 20, 'bold'), bd=5, command=lambda: add_operand(arg))


def make_calc_button(arg):
    return tk.Button(text=arg, font=('Arial', 20, 'bold'), bd=5, command=calculate)


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

make_calc_button('=').grid(row=4, column=2, sticky='NSEW', padx=5, pady=5)
tk.Button(text='C', font=('Arial', 20, 'bold'), bd=5, command=add_cansel).grid(row=4, column=1, sticky='NSEW', padx=5, pady=5)

for i in range(5):
    win.grid_columnconfigure(i, minsize=50)
    win.grid_rowconfigure(i, minsize=50)

win.mainloop()  # вывели окно
