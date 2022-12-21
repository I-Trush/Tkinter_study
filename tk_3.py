# виджеты, Button

import tkinter as tk

win = tk.Tk()
win.title('окно графического приложения')
win.geometry('500x600+500+200')
win.config(bg='#c7c7c7')
#======================================================================================================

def say_hello():  # нужна ф-ия не принимающая никаких аргументов
    print('hello')

btn_1 = tk.Button(win, text='Hello',
                  command=say_hello, # если указать скобки, то 'hello' в консоль будет напичатано сразу при запуске модуля, а не при нажатии кнопки
                  )
#======================================================================================================


def add_label():
    label = tk.Label(win, text='new Label')
    label.pack()  # добавили объект в окно// для работы 2 кнопки

btn_2 = tk.Button(win, text='Add Label',
                  command=add_label
                  )
#======================================================================================================

btn_3 = tk.Button(win, text='Add Label lambda',
                  command=lambda: tk.Label(win, text='new').pack(),
                  )
#======================================================================================================


count = [0]
def counter():  # ф-ия счетчик
    count[0] += 1
    btn_4['text'] = f'счетчик = {count[0]}'  # атрибуты кнопки записаны в словарь (под капотом)


btn_4 = tk.Button(win, text='счетчик = 0',  # кннопка счётчик
                  command=counter,  # кннопка счётчик
                  bg='red',
                  activebackground='blue',  # фон кнопки при зажатии
                  state=tk.NORMAL  # можно отключить кнуопку по умолчанию tk.NORMAL //  tk.DISABLED - отключить кнопку
                  )

# WIDGET-SPECIFIC OPTIONS:
# command, compound, default, height, overrelief, state, width

# STANDARD OPTIONS:
# activebackground, activeforeground, anchor, background, bitmap, borderwidth, cursor, disabledforeground, font, foreground, highlightbackground, highlightcolor,
# highlightthickness, image, justify, padx, pady, relief, repeatdelay, repeatinterval, takefocus, text, textvariable, underline, wraplength
#======================================================================================================

btn_1.pack()  # добавили объект в окно
btn_2.pack()
btn_3.pack()
btn_4.pack()

win.mainloop()  # вывели окно
