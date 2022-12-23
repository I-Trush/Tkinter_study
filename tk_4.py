# grid

import tkinter as tk

win = tk.Tk()
win.title('окно графического приложения')
win.geometry('800x600+500+200')
win.config(bg='#c7c7c7')
#======================================================================================================

# btn_1 = tk.Button(win, text='Hello 1')
# btn_2 = tk.Button(win, text='Hello world 2')
# btn_3 = tk.Button(win, text='Hello 3')
# btn_4 = tk.Button(win, text='Hello 4')
# btn_5 = tk.Button(win, text='Hello 5')
# btn_6 = tk.Button(win, text='Hello 6')
# btn_7 = tk.Button(win, text='Hello 7')
# btn_8 = tk.Button(win, text='Hello 8')
#
#
# btn_1.grid(row=0, column=0, stick='we')     # btn_1.grid метод поместит кнопку в соответствующую ячейку на координатной сетке
# btn_2.grid(row=0, column=1)
# btn_3.grid(row=1, column=0)
# btn_4.grid(row=1, column=1, stick='we')
# btn_5.grid(row=2, column=0)
# btn_6.grid(row=2, column=1)
# btn_7.grid(row=3, column=0, columnspan=2, stick='we')  # columnspan=2 кнопка займет 2 столбца, stick='we' кнопка будет растянута с запада на восток (по горизонтали)
# btn_8.grid(row=0, column=3, rowspan=4, stick='ns')     # rowspan=4 кнопка займет 4 строки, stick='ns' кнопка будет растянута с севера на юг (по вертикали)
#
# win.grid_columnconfigure(0, minsize=200)
# win.grid_columnconfigure(1, minsize=100)
#======================================================================================================

for i in range(7):
    for j in range(5):
        tk.Button(win, text=f'Кнопка {i},{j}').grid(row=i, column=j, stick='NSEW')  #stick='NSEW' полностью растянутая кнопка

win.grid_columnconfigure(0, minsize=200)
win.grid_columnconfigure(1, minsize=100)
win.grid_rowconfigure(0, minsize=100)




win.mainloop()  # вывели окно
