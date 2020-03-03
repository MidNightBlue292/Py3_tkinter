from tkinter import *

janela = Tk()

lb1 = Label(janela, text='LINHA1', bg='white')
lb2 = Label(janela, text='LINHA1', bg='yellow')
lb3 = Label(janela, text='LINHA1', bg='blue')

lb1.pack(side=TOP, fill=BOTH, expand=1)
lb2.pack(side=TOP, fill=BOTH, expand=1)
lb3.pack(side=TOP, fill=BOTH, expand=1)

janela.geometry('400x300+200+200')
janela.mainloop()
