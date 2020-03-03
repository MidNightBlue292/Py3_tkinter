from tkinter import *


def bt_click():
    print(en.get())
    lb['text'] = en.get()


janela = Tk()

# Criar entrada de dados
en = Entry(janela)
en.place(x=100, y=100)

# Criar Botão
bt = Button(janela, width=20, text='OK', command=bt_click)
# Localização
bt.place(x=100, y=150)

lb = Label(janela, text='Teste1')
lb.place(x=100, y=200)

janela.geometry('300x300+200+200')
janela.mainloop()
