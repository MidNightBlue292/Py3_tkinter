from tkinter import *


def bt_click():
    print('bt_click')
    lb['text'] = 'Funcionou' # Muda o nome do Label text


janela = Tk()

# Criar Botão
bt = Button(janela, width=20, text='OK', command=bt_click) # Sem () em bt_click
# Localização
bt.place(x=100, y=100)

# Criar Label
lb = Label(janela, text='Teste')
# Localização
lb.place(x=100, y=150)

janela.geometry ('300x300+200+200')
janela.mainloop()
