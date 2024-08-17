import tkinter as tk
from tkinter import messagebox

# Create the main application window
root = tk.Tk()
# Set window title
root.title("Calculadoras de Concreto Armado e Protendido")
# Set window size (width x height)
root.geometry("400x300")

# Functions for menu actions
def laje_trelicada():
    messagebox.showinfo("New lajes", "New lajes created!")

def laje_macica():
    messagebox.showinfo("Open lajes", "lajes opened!")

def laje_mista():
    messagebox.showinfo("Save lajes", "lajes saved!")

def exit_app():
    root.quit()

# Create the menu bar
menu_bar = tk.Menu(root)

# Criação dos menus
#Lajes
lajes_menu = tk.Menu(menu_bar, tearoff=0)
lajes_menu.add_command(label="Laje treliçada", command=laje_trelicada)
lajes_menu.add_command(label="Laje maciça", command=laje_macica)
lajes_menu.add_command(label="Laje mista", command=laje_mista)
menu_bar.add_cascade(label="Lajes", menu=lajes_menu)

#Vigas
vigas_menu = tk.Menu(menu_bar, tearoff=0)

#cria submenu viga ELU
sub_vigas_menu = tk.Menu(vigas_menu, tearoff= 0)

#submenu flexão simples
sub_flexao_menu = tk.Menu(vigas_menu, tearoff=0)
sub_flexao_menu.add_command(label='Dimensionamento: Seção retangular', command= '')
sub_flexao_menu.add_command(label='Dimensionamento: Seção T', command= '')
sub_flexao_menu.add_command(label='Verificação: Seção retangular', command= '')
sub_flexao_menu.add_command(label='Verificação: Seção T', command= '')
#adiciona sub menu vigas ao submenu flexão simples
sub_vigas_menu.add_cascade(label='Flexão simples', menu=sub_flexao_menu)
sub_vigas_menu.add_command(label="Força cortante", command='')
sub_vigas_menu.add_command(label="Torção", command='')

vigas_menu.add_cascade(label= 'Estado Limite Último', menu=sub_vigas_menu)
vigas_menu.add_command(label="Estado limite de serviço", command=laje_macica)
menu_bar.add_cascade(label="Vigas", menu=vigas_menu)

#cria menu pilares
pilares_menu = tk.Menu(menu_bar, tearoff= 0)
pilares_menu.add_command(label='Estado Limite Último')
menu_bar.add_cascade(label='Pilares', menu= pilares_menu)

#cria menu fundações
fundacoes_menu = tk.Menu(menu_bar, tearoff= 0)
#submenu blocos
blocos_menu = tk.Menu(fundacoes_menu, tearoff=0)
blocos_menu.add_command(label='1 Estaca')
blocos_menu.add_command(label='2 Estacas')
blocos_menu.add_command(label='3 Estaca')
blocos_menu.add_command(label='4 Estacas')
blocos_menu.add_command(label='5 Estacas')
fundacoes_menu.add_cascade(label='Blocos', menu= blocos_menu)
fundacoes_menu.add_command(label='Sapatas')
fundacoes_menu.add_command(label='Radier')
#submenu arrimos
arrimos_menu = tk.Menu(fundacoes_menu, tearoff= 0 )
arrimos_menu.add_command(label="Estaqueado")
arrimos_menu.add_command(label='Com sapatas')
fundacoes_menu.add_cascade(label='Muros de arrimo', menu= arrimos_menu)
menu_bar.add_cascade(label='Fundações', menu=fundacoes_menu)

#Cria menu escadas
escadas_menu = tk.Menu(menu_bar, tearoff= 0 )
escadas_menu.add_command(label='Plissadas')
escadas_menu.add_command(label='Retas')
escadas_menu.add_command(label='Helicoidais')
menu_bar.add_cascade(label='Escadas', menu= escadas_menu)

#cria menu outros
outros_menu = tk.Menu(menu_bar, tearoff= 0)
outros_menu.add_command(label='Ancoragem')
menu_bar.add_cascade(label='Outros', menu= outros_menu)


# Configure the root window to display the menu
root.config(menu=menu_bar)

# Start the Tkinter event loop
root.mainloop()
