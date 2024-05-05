import  customtkinter as ctk
from tkinter import *
from tkinter import messagebox

from db import *



ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.layout_config()
        self.appearence()
        self.todo_sistema()

    def layout_config(self):
        self.title("Gerenciador de clientes")
        self.geometry("1366x768")

    def appearence(self):
        self.lb_apm = ctk.CTkLabel(self, text="Tema", bg_color="transparent", text_color=["#000","#fff"]).place(x=10,y=630)

        self.opt_apm = ctk.CTkOptionMenu(self, values=["System","Light","Dark"],command=self.change_apm).place(x=10,y=660)

    def change_apm(self, new_appearence_mode):
        ctk.set_appearance_mode(new_appearence_mode)

    

    def todo_sistema(self):
        frame = ctk.CTkFrame(self, width=1920, height=70, corner_radius=0, bg_color="RoyalBlue", fg_color="RoyalBlue")
        frame.place(x=0,y=10)
        title = ctk.CTkLabel(frame, text="Efraim".upper(), font=("Century Gothic bold",30),text_color= "#fff").place(x=600,y=18)
        span = ctk.CTkLabel(self, text="Por favor, preencha todos os campos!", font=("Century Gothic bold",24),text_color= ["#000","#fff"]).place(x=10, y=90)
        
        
        #BackEnd

        #funções dos botoes
        def submit():
            codigo = cod_value.get()
            cpf = cpf_value.get()
            nome = nome_value.get()
            endereco = end_value.get()
            numero = num_value.get()
            bairro = bairro_value.get()
            cep = cep_value.get()
            telefone = tell_value.get()
            descricao = descrição_entry.get(0.0,END)
            

            if (codigo =="" or nome =="" or endereco =="" or numero == ""or bairro =="" or cep =="" or telefone ==""):
                messagebox.showerror("Erro","Preencha todos os campos!")
            else:
                Cadastrar_clientes(codigo,cpf,nome,endereco,numero,bairro,cep,telefone,descricao)
                messagebox.showinfo("System","Dados salvos com sucesso!")

            clear();
    #---------------------------------------------------------------------------------------------------------------
        def BuscarEndereco():
            EnderecoCliente = end_value.get()
            NCasaCliente = num_value.get()

            if check_value(EnderecoCliente,NCasaCliente):
                cliente_encontrado = Buscar_ClienteEnd(EnderecoCliente,NCasaCliente)
                if cliente_encontrado:
                    open_second_screen(cliente_encontrado)
                else:
                    messagebox.showerror("Erro","Cliente não encontrado")
            else:
                messagebox.showerror("Erro","Cliente não encontrado")

        #configTela2
        def open_second_screen(cliente):
            second_screen = ctk.CTkToplevel(App)
            second_screen.grab_set()
            second_screen.geometry("783x600")
            frame2 = ctk.CTkFrame(second_screen,width=783,height=70, corner_radius=0, bg_color="RoyalBlue", fg_color="RoyalBlue")
            frame2.pack()
            frame2.place(x=0,y=10)
            
            #extraindo valores do cliente encontrado
            IdCliente, CodCliente, CpfCliente, NomeCliente, EnderecoCliente, NCasaCliente, BairroCliente, CepCliente , TellCliente , Descricao = cliente

            #FRONT-END
            #LABELS

            lb_codigo_2 = ctk.CTkLabel(second_screen,text="COD", font=("Century Gothic bold",16),text_color= ["#000","#fff"])
            lb_codigo_2.pack()
            lb_codigo_2.place(x=10,y=90)

            lb_cpf_2 = ctk.CTkLabel(second_screen,text="CPF:", font=("Century Gothic bold",16),text_color= ["#000","#fff"])
            lb_cpf_2.pack()
            lb_cpf_2.place(x=60,y=90)

            lb_nome_2 = ctk.CTkLabel(second_screen,text="Nome:", font=("Century Gothic bold",16),text_color= ["#000","#fff"])
            lb_nome_2.pack()
            lb_nome_2.place(x=200,y=90)

            lb_endereco_2 = ctk.CTkLabel(second_screen,text="Endereço:", font=("Century Gothic bold",16),text_color= ["#000","#fff"])
            lb_endereco_2.pack()
            lb_endereco_2.place(x=10,y=170)

            lb_numero_2 = ctk.CTkLabel(second_screen,text="Nº",font=("Century Gothic bold",16),text_color=["#000","#fff"])
            lb_numero_2.pack()
            lb_numero_2.place(x=410,y=170)


            lb_bairro_2 = ctk.CTkLabel(second_screen,text="Bairro:", font=("Century Gothic bold",16),text_color= ["#000","#fff"])
            lb_bairro_2.pack()
            lb_bairro_2.place(x=620,y=170)

            lb_cep_2 = ctk.CTkLabel(second_screen,text="CEP:", font=("Century Gothic bold",16),text_color= ["#000","#fff"])
            lb_cep_2.pack()
            lb_cep_2.place(x=470,y=170)

            lb_telefone_2 = ctk.CTkLabel(second_screen,text="Telefone:", font=("Century Gothic bold",16),text_color= ["#000","#fff"])
            lb_telefone_2.pack()
            lb_telefone_2.place(x=530,y=90)

            lb_descricao_2 = ctk.CTkLabel(second_screen,text="Descrição:", font=("Century Gothic bold",16),text_color= ["#000","#fff"])
            lb_descricao_2.pack()
            lb_descricao_2.place(x=10,y=270)



            #entrys
            entry_tela2_cod = ctk.CTkEntry(second_screen,font=("Century Gothic",16),width=45)
            entry_tela2_cod.pack()
            entry_tela2_cod.insert(0,CodCliente)
            entry_tela2_cod.place(x=10,y=120)
            entry_tela2_cod.configure(state="readonly")

            
            entry_tela2_cpf = ctk.CTkEntry(second_screen,font=("Century Gothic",16),width=130)
            entry_tela2_cpf.pack()
            entry_tela2_cpf.insert(0,CpfCliente)
            entry_tela2_cpf.place(x=60,y=120)
            entry_tela2_cpf.configure(state="readonly")


            entry_tela2_nome = ctk.CTkEntry(second_screen,font=("Century Gothic",16),width=320)
            entry_tela2_nome.pack()
            entry_tela2_nome.insert(0,NomeCliente)
            entry_tela2_nome.place(x=200,y=120)
            entry_tela2_nome.configure(state="readonly")

            entry_tela2_endereco = ctk.CTkEntry(second_screen,font=("Century Gothic",16),width=390)
            entry_tela2_endereco.pack()
            entry_tela2_endereco.insert(0,EnderecoCliente)
            entry_tela2_endereco.place(x=10,y=200)
            entry_tela2_endereco.configure(state="readonly")

            entry_tela2_numero = ctk.CTkEntry(second_screen,font=("Century Gothic",16),width=50)
            entry_tela2_numero.pack()
            entry_tela2_numero.insert(0,NCasaCliente)
            entry_tela2_numero.place(x=410,y=200)
            entry_tela2_numero.configure(state="readonly")


            entry_tela2_bairro = ctk.CTkEntry(second_screen,font=("Century Gothic",16),width=130)
            entry_tela2_bairro.pack()
            entry_tela2_bairro.insert(0,BairroCliente)
            entry_tela2_bairro.place(x=620,y=200)
            entry_tela2_bairro.configure(state="readonly")

            entry_tela2_cep = ctk.CTkEntry(second_screen,font=("Century Gothic",16),width=140)
            entry_tela2_cep.pack()
            entry_tela2_cep.insert(0,CepCliente)
            entry_tela2_cep.place(x=470,y=200)
            entry_tela2_cep.configure(state="readonly")

            entry_tela2_telefone = ctk.CTkEntry(second_screen,font=("Century Gothic",16),width=140)
            entry_tela2_telefone.pack()
            entry_tela2_telefone.insert(0,TellCliente)
            entry_tela2_telefone.place(x=530,y=120)


            entry_tela2_descricao =ctk.CTkTextbox(second_screen,width=500,height=150,font=("Century Gothic",16),fg_color="transparent",border_color="#aaa",border_width=2)
            """entry_tela2_descricao = ctk.CTkTextbox(second_screen,font=("Century Gothic",16),width=500,height=150)"""
            entry_tela2_descricao.pack()
            entry_tela2_descricao.insert("2.0",Descricao)
            entry_tela2_descricao.place(x=10,y=300)

            def alterar():
                novo_telefone = entry_tela2_telefone.get()
                nova_descricao = entry_tela2_descricao.get("1.0","end-1c")
                
                EnderecoCliente = end_value.get()
                NCasaCliente = num_value.get()

                Alterar_dados_cliente(novo_telefone,nova_descricao,EnderecoCliente,NCasaCliente)
                messagebox.showinfo("System","Dados do cliente alterados com sucesso!")


            btn_delete = ctk.CTkButton(second_screen,text="Deletar".upper(),command=delete,fg_color="Red",hover_color="Maroon",height=50,font=("Century Gothic",16))
            btn_delete.pack()
            btn_delete.place(x=10,y=500)

            btn_alterar = ctk.CTkButton(second_screen,text="Alterar dados".upper(),command=alterar,fg_color="RoyalBlue",hover_color="Navy",height=50,font=("Century Gothic",16))
            btn_alterar.pack()
            btn_alterar.place(x=200,y=500)
            
    #---------------------------------------------------------------------------------------------------------------
        def delete():
            EnderecoCliente = end_value.get()
            NCasaCliente = num_value.get()

            if (EnderecoCliente ==""):
                messagebox.showerror("Erro","Código não encontrado!")
            else:
                Excluir_cliente(EnderecoCliente,NCasaCliente)
                messagebox.showinfo("System","Cliente Excluído com sucesso!".upper())

        def clear():
            cod_value.set("")
            cpf_value.set("")
            nome_value.set("")
            end_value.set("")
            num_value.set("")
            bairro_value.set("")
            cep_value.set("")
            tell_value.set("")
            descrição_entry.delete(0.0,END)

        




        #Texts Variables
        cod_value = StringVar()
        cpf_value = StringVar()
        nome_value = StringVar()
        end_value = StringVar()
        num_value = StringVar()
        bairro_value = StringVar()
        cep_value = StringVar()
        tell_value = StringVar()
    
        #FrontEnd---------------------------------------------------------------------------------------------------
        
        #Entrys
        codigo_entry =ctk.CTkEntry(self,width=50,textvariable=cod_value,font=("Century Gothic",16),fg_color="transparent")

        cpf_entry =ctk.CTkEntry(self,width=130,textvariable=cpf_value,font=("Century Gothic",16),fg_color="transparent")

        nome_entry =ctk.CTkEntry(self,width=300,textvariable=nome_value,font=("Century Gothic",16),fg_color="transparent")

        endereço_entry =ctk.CTkEntry(self,width=450,textvariable=end_value,font=("Century Gothic",16),fg_color="transparent")

        numero_entry =ctk.CTkEntry(self,width=50,textvariable=num_value,font=("Century Gothic",16),fg_color="transparent")

        Bairro_entry =ctk.CTkEntry(self,width=170,textvariable=bairro_value,font=("Century Gothic",16),fg_color="transparent")

        cep_entry =ctk.CTkEntry(self,width=140,textvariable=cep_value,font=("Century Gothic",16),fg_color="transparent")

        telefone_entry =ctk.CTkEntry(self,width=140,textvariable=tell_value,font=("Century Gothic",16),fg_color="transparent")

        descrição_entry =ctk.CTkTextbox(self,width=500,height=150,font=("Arial",18),fg_color="transparent",border_color="#aaa",border_width=2)

        
        #Labels
        lb_codigo = ctk.CTkLabel(self, text="Código", font=("Century Gothic bold",16),text_color= ["#000","#fff"])

        lb_cpf = ctk.CTkLabel(self, text="Digite o CPF", font=("Century Gothic bold",16),text_color= ["#000","#fff"])

        lb_nome = ctk.CTkLabel(self, text="Digite o Nome", font=("Century Gothic bold",16),text_color= ["#000","#fff"])

        lb_endereço = ctk.CTkLabel(self, text="Digite o Endereço", font=("Century Gothic bold",16),text_color= ["#000","#fff"])

        lb_numero = ctk.CTkLabel(self, text="Nº", font=("Century Gothic bold",16),text_color= ["#000","#fff"])

        lb_Bairro = ctk.CTkLabel(self, text="Informe o Bairro", font=("Century Gothic bold",16),text_color= ["#000","#fff"])

        lb_cep = ctk.CTkLabel(self, text="Digite o CEP", font=("Century Gothic bold",16),text_color= ["#000","#fff"])

        lb_telefone = ctk.CTkLabel(self, text="Digite o Telefone", font=("Century Gothic bold",16),text_color= ["#000","#fff"])

        lb_descrição = ctk.CTkLabel(self, text="Descrição", font=("Century Gothic bold",16),text_color= ["#000","#fff"])

        #Buttons
        btn_submit = ctk.CTkButton(self,text="Cadastrar Cliente".upper(),command=submit,fg_color="RoyalBlue",hover_color="Navy",height=50,font=("Century Gothic",16))
        btn_clear = ctk.CTkButton(self,text="Limpar Campos".upper(),command=clear,fg_color="#555",hover_color="#333",height=50,font=("Century Gothic",16))
        btn_search = ctk.CTkButton(self,text="buscar".upper(),command=BuscarEndereco,fg_color="RoyalBlue",hover_color="Navy",height=50,font=("Century Gothic",16))
        btn_CostumerRow = ctk.CTkButton(self,text="Lista de Clientes".upper(),fg_color="RoyalBlue",hover_color="Navy",height=50,font=("Century Gothic",16))
        btn_delete = ctk.CTkButton(self,text="Deletar".upper(),fg_color="Red",hover_color="Maroon",height=50,font=("Century Gothic",16))
        



        #---Posicionamento---
        lb_codigo.place(x=50,y=150)
        codigo_entry.place(x=50,y=180)

        lb_cpf.place(x=120,y=150)
        cpf_entry.place(x=120,y=180)

        lb_nome.place(x=260,y=150)
        nome_entry.place(x=260,y=180)

        lb_endereço.place(x=572,y=150)
        endereço_entry.place(x=572,y=180)

        lb_numero.place(x=1040,y=150)
        numero_entry.place(x=1040,y=180)

        lb_Bairro.place(x=50,y=230)
        Bairro_entry.place(x=50,y=260)

        lb_cep.place(x=230,y=230)
        cep_entry.place(x=230,y=260)

        lb_telefone.place(x=380,y=230)
        telefone_entry.place(x=380, y=260)

        lb_descrição.place(x=50,y=300)
        descrição_entry.place(x=50,y=330)

        

        btn_submit.place(x=50,y=520)
        btn_search.place(x=245,y=520)
        #btn_delete.place(x=413,y=520)
        btn_CostumerRow.place(x=395,y=520)
        btn_clear.place(x=570,y=520)


if __name__ == "__main__":
    App = App()
    App.mainloop()
