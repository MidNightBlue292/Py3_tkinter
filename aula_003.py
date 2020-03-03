import tkinter as tk
janela = tk.Tk()

# Muda o título da janela
janela.title('Janela principal')

# Altera a cor de fundo da janela
# Modo 1
janela['background'] = 'green'
# Modo 2
janela['bg'] = 'green'

# Redimensionar e posição da janela LxA+E+T em pixel
# Largura x Altura + distância Esquerda + distância Topo
janela.geometry ('300x300+100+100')

janela.mainloop()
