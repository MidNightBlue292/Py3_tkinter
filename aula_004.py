from tkinter import *
janela = Tk()

# Criar Label
lb = Label(janela, text='Olá mundo!!')
# Localização
lb.place(x=100, y=100)

janela.geometry ('300x300+200+200')
janela.mainloop()
