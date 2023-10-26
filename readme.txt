root = tk.Tk()
root.title("Cadastro de Clientes")

label_codigo = ttk.Label(root, text="Código:")
entry_codigo = ttk.Entry(root)

label_cpf = ttk.Label(root, text="CPF:")
entry_cpf = ttk.Entry(root)

label_nome = ttk.Label(root, text="Nome:")
entry_nome = ttk.Entry(root)

label_endereço = ttk.Label(root, text="Digite o Endereço do Cliente:")
entry_endereço = ttk.Entry(root)


label_nCasa = ttk.Label(root, text="Nº da casa:")
entry_nCasa = ttk.Entry(root)

label_cep = ttk.Label(root, text="CEP:")
entry_cep = ttk.Entry(root)

label_telefone = ttk.Label(root, text="Telefone:")
entry_telefone = ttk.Entry(root)

label_descricao = ttk.Label(root, text="Descrição:")
entry_descricao = ttk.Combobox(root)

btn_cadastrar = ttk.Button(root, text="Cadastrar", command=Cadastrar_clientes)

label_busca = ttk.Label(root, text="Buscar por Endereço:")
entry_busca = ttk.Entry(root)

btn_buscar = ttk.Button(root, text="Buscar", command=buscar)



label_codigo.pack()
entry_codigo.pack()

label_cpf.pack()
entry_cpf.pack()

label_nome.pack()
entry_nome.pack()

label_endereço.pack()
entry_endereço.pack()

label_nCasa.pack()
entry_nCasa.pack()

label_cep.pack()
entry_cep.pack()

label_telefone.pack()
entry_telefone.pack()

label_descricao.pack()
entry_descricao.pack()

btn_cadastrar.pack()
label_busca.pack()
entry_busca.pack()
btn_buscar.pack()

root.mainloop()
