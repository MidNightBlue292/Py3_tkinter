from tkinter import *

janela = Tk()

lb1 = Label(janela, text='HORIZONTAL', bg='white')
lb2 = Label(janela, text='LEFT', bg='white')
lb3 = Label(janela, text='RIGHT', bg='white')

lb1.pack(side=TOP, fill=X)
lb2.pack(side=LEFT, fill=Y)
lb3.pack(side=RIGHT, fill=Y)

janela['bg'] = 'black'
janela.geometry('400x300+200+200')
janela.mainloop()
