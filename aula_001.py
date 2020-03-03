# Importar a biblioteca completa
from tkinter import *
# Criar primeira janela
janela = Tk()
# Conteúdo usando Label com gerenciador de layout pack
Label(janela, text='Minha primeira janela!').pack()
# Mantêm a janela em loop infinito até ser fechada
janela.mainloop()
