import  customtkinter as s
from tkinter import *
from tkinter import messagebox
from db import *

App = s.CTk()
"""def buscar():
    endereco = entry_busca.get()
    endereco_encontrado = Buscar_ClienteEnd(endereco)
    print("Endereço encontrado", endereco_encontrado)"""

def cadastro():
    janela1 = s.CTkToplevel(Cadastrar_clientes,fg_color= "Light-Blue")

btn_novatela = s.CTkButton(master=App,text="Cadastro",command=App).place(x=300,y=100)

App.title("Gerenciados de Clientes")
App._set_appearance_mode("system")
App.mainloop()