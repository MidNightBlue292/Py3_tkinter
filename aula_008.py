from tkinter import *


def bt_click():
    if (en1.get().isnumeric() and en2.get().isnumeric()):
        lb['text'] = int(en1.get()) + int(en2.get())
    else:
        lb['text'] = 'Valores inválidos'


janela = Tk()

en1 = Entry(janela)
en1.place(x=10, y=10)
en2 = Entry(janela)
en2.place(x=10, y=50)

bt = Button(janela, width=20, text='SOMA', command=bt_click)
bt.place(x=10, y=100)

lb = Label(janela, text='Soma 2 números')
lb.place(x=10, y=150)

janela.geometry('300x300+200+200')
janela.mainloop()
