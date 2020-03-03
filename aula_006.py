from tkinter import *
from functools import partial


def bt_click1():
    print('bt_click1')
    lb1['text'] = 'Funcionou'


def bt_click2(botao):
    print(botao['text'])
    lb2['text'] = 'Funcionou'


janela = Tk()

# Modo 1
bt1 = Button(janela, width=20, text='Botão1', command=bt_click1)
bt1.place(x=10, y=10)
# Modo 2
bt2 = Button(janela, width=20, text='Botão2')
bt2['command'] = partial(bt_click2, bt2)
bt2.place(x=10, y=50)

lb1 = Label(janela, text='Teste1')
lb1.place(x=200, y=10)
lb2 = Label(janela, text='Teste2')
lb2.place(x=200, y=50)

janela.geometry('300x300+200+200')
janela.mainloop()
