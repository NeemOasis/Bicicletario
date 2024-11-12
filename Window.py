import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import re

import ConexaoTCP as server

def mostrar_tela_inicial():
    # ... Esconde widgets da tela de cadastro ...
    limpar_botoes()

    # Mostra widgets da tela de login
    botao_entrada.grid()
    botao_retirada.grid()
    

def cadastrar_cliente():
    ## cadastrar
    name = str(nome_campo.get())
    server.request_insert_client(name,
                                 cpf_campo.get(),
                                 rg_campo.get(),
                                 email_campo.get(),
                                 telefone_campo.get(),
                                 endereco_campo.get(),
                                 data_nascimento_campo.get())

    limpar_entry()
    mostrar_tela_entrada()
    messagebox.showinfo("Cadastro", "Cliente cadastrado com sucesso!")


def cadastrar_bike():
    cliente = str(cliente_campo.get())
    server.request_insert_bike(aro_campo.get(),
        condicao_campo.get(),
        cliente_campo.get(),
        cor_campo.get())

    limpar_entry()
    mostrar_tela_entrada()
    messagebox.showinfo("Cadastro", "Bike cadastrado com sucesso!")
    

def registrar_movimentacao():
    server.request_insert_movement(bike_campo.get())

    limpar_entry()
    mostrar_tela_inicial()
    messagebox.showinfo("Movimentação", "Movimentação registrada com sucesso!")


def client_search_database(event):
    label_bike_info.config(text="")
    label_nome.config(text="")

    info = cliente_combo.get()
    results = server.request_select_client(info)
    results = eval(results)

    valores_combobox = [result[2] for result in results]
    cliente_combo['values'] = valores_combobox

def bike_search_database():
    cpf = cliente_combo.get()
    results = server.request_select_bike_by_client(cpf)
    results = results.replace('Decimal', '')
    results = eval(results)

    valores_combobox = [result[0] for result in results]
    bike_combo['values'] = valores_combobox

def select_client_combo(event):
    label_bike_info.config(text="")
    info = cliente_combo.get()
    results = server.request_select_client(info)
    results = eval(results)
    cliente = results[0]

    label_nome.config(text=f"nome do cliente: {cliente[0]}")

    bike_search_database()

def select_bike_combo(event):
    info = bike_combo.get()

    results = server.request_select_bike(info)
    results = results.replace('Decimal', '')
    results = eval(results)
    bike = results[0]

    label_bike_info.config(text=f"aro: {bike[1]}, condicao: {bike[2]}, status: {bike[4]}")

def mostrar_tela_entrada():
    ## retornar
    limpar_botoes()

    #cliente = cliente_campo.grid(row=0, column=0)
    cliente_combo.grid(row=0, column=0)
    bike_combo.grid(row=1, column=0)

    label_nome.grid(row=0, column=3)
    label_bike_info.grid(row=1, column=3)

    # busca no banco
    cliente_combo.bind('<KeyRelease>', client_search_database)
    cliente_combo.bind("<<ComboboxSelected>>", select_client_combo)
    bike_combo.bind("<<ComboboxSelected>>", select_bike_combo)


    botao_cliente.grid(row=0, column=1)
    botao_bike.grid(row=1,column=1)
    botao_registrar.grid(row=2, column=1)
    botao_editar_cliente.grid(row=3, column=1)
    botao_editar_bike.grid(row=4, column=1)
    #botao_deletar_user.grid(row=5, column=1)
    botao_cancelar.grid(row=6, column=1)

def mostrar_tela_cadastro():
    # ... Esconde widgets da tela de login ...
    limpar_botoes()

    # Mostra widgets da tela de cadastro
    botao_cadastrar_cliente.grid(row=8, column=3)
    botao_cancelar_entrada_bike.grid(row=9, column=3)

    label_nome_campo.grid(row=1, column=0)
    label_rg_campo.grid(row=2, column=0)
    label_cpf_campo.grid(row=3, column=0)
    #vcmd = (janela.register(on_validate), '%P')
    #data_nascimento_campo.config(validate='key', validatecommand=vcmd)
    label_data_nascimento_campo.grid(row=4, column=0)
    label_telefone_campo.grid(row=5, column=0)
    label_email_campo.grid(row=6, column=0)
    label_endereco_campo.grid(row=7, column=0)


    nome_campo.grid(row=1, column=1)
    rg_campo.grid(row=2, column=1)
    cpf_campo.grid(row=3, column=1)
    data_nascimento_campo.grid(row=4, column=1)
    telefone_campo.grid(row=5, column=1)
    email_campo.grid(row=6, column=1)
    endereco_campo.grid(row=7, column=1)


def mostrar_tela_bike():
    limpar_botoes()
    botao_cadastrar_bike.grid(row=5, column=3)
    botao_cancelar_entrada_bike.grid(row=6, column=3)

    label_idcliente_campo.grid(row=1, column=0)
    label_aro_campo.grid(row=2, column=0)
    label_cor_campo.grid(row=3, column=0)
    label_condicao_campo.grid(row=4, column=0)


    cliente_campo.grid(row=1, column=2)
    aro_campo.grid(row=2, column=2)
    cor_campo.grid(row=3, column=2)
    condicao_campo.grid(row=4, column=2)

    limpar_entry()

def mostrar_tela_retirada():
    limpar_botoes()

    submeter = submeter_retirada_campo.grid()

    botao_submeter_retirada.grid()
    botao_cancelar.grid()

    limpar_entry()
    

def mostrar_tela_editar_cliente(cliente):
    limpar_botoes()

    label_nome_campo.grid(row=1, column=0)
    label_rg_campo.grid(row=2, column=0)
    label_cpf_campo.grid(row=3, column=0)
    label_data_nascimento_campo.grid(row=4, column=0)
    label_telefone_campo.grid(row=5, column=0)
    label_email_campo.grid(row=6, column=0)
    label_endereco_campo.grid(row=7, column=0)

    nome_campo.grid(row=1, column=1)
    rg_campo.grid(row=2, column=1)
    cpf_campo.grid(row=3, column=1)
    data_nascimento_campo.grid(row=4, column=1)
    telefone_campo.grid(row=5, column=1)
    email_campo.grid(row=6, column=1)
    endereco_campo.grid(row=7, column=1)

    limpar_entry()

    print(cliente)

    if cliente is not None:
        nome_campo.insert(0, cliente[0])
        rg_campo.insert(0, cliente[1])
        cpf_campo.insert(0, cliente[2])
        email_campo.insert(0, cliente[3])
        telefone_campo.insert(0, cliente[4])
        endereco_campo.insert(0, cliente[5])
        data_nascimento_campo.insert(0, cliente[6])

    botao_update_cliente.grid(row=5, column=3)
    botao_cancelar_entrada_bike.grid(row=6, column=3)


def mostrar_tela_editar_bike(bike):
    limpar_botoes()

    label_idbike_campo.grid(row=0, column=0)
    label_idcliente_campo.grid(row=1, column=0)
    label_aro_campo.grid(row=2, column=0)
    label_cor_campo.grid(row=3, column=0)
    label_condicao_campo.grid(row=4, column=0)

    idbike_campo.grid(row=0, column=0)
    cliente_campo.grid(row=1, column=2)
    aro_campo.grid(row=2, column=2)
    cor_campo.grid(row=3, column=2)
    condicao_campo.grid(row=4, column=2)

    limpar_entry()

    if bike is not None:
        idbike_campo.insert(0, bike[0])
        cliente_campo.insert(0, bike[1])
        aro_campo.insert(0, bike[2])
        cor_campo.insert(0, bike[3])
        condicao_campo.insert(0, bike[4])

    botao_update_bike.grid(row=5, column=3)
    botao_cancelar_entrada_bike.grid(row=6, column=3)

def editar_cliente():
    info = cliente_combo.get()
    results = server.request_select_client(info)
    results = eval(results)
    cliente = results[0]

    mostrar_tela_editar_cliente(cliente)
    
def editar_bike():
    info = bike_combo.get()

    results = server.request_select_bike(info)
    results = results.replace('Decimal', '')
    results = eval(results)
    bike = results[0]

    mostrar_tela_editar_bike(bike)

def update_cliente():
    server.request_update_client(condicao_campo.get(),
                                 cor_campo.get(),
                                 idbike_campo.get())

    limpar_entry()
    mostrar_tela_entrada()
    messagebox.showinfo("Atualizado", "Cliente atualizado com sucesso!")


def update_bike():
    server.request_update_bike(nome_campo.get(),
                                 email_campo.get(),
                                 telefone_campo.get(),
                                 endereco_campo.get(),
                                 cpf_campo.get())

    limpar_entry()
    mostrar_tela_entrada()
    messagebox.showinfo("Atualizada", "Bicicleta atualizado com sucesso!")


def delete_client():
    pass


def delete_bike():
    pass


def validar_data(data):
    padrao = re.compile(r"^\d{2}/\d{2}/\d{4}$")
    return padrao.match(data) is not None

def on_validate(P):
    if validar_data(P):
        return True
    elif P == "":
        return True
    else:
        return False

def limpar_botoes():
    botao_entrada.grid_forget()
    botao_retirada.grid_forget()
    botao_submeter_retirada.grid_forget()
    botao_cliente.grid_forget()
    botao_cadastrar_cliente.grid_forget()
    botao_bike.grid_forget()
    botao_cadastrar_bike.grid_forget()
    botao_cancelar.grid_forget()
    botao_cancelar_entrada_bike.grid_forget()
    botao_registrar.grid_forget()
    #botao_deletar_user.grid_forget()
    #botao_deletar_bike.grid_forget()
    botao_deletar_cliente.grid_forget()
    botao_deletar_bike.grid_forget()
    nome_campo.grid_forget()
    rg_campo.grid_forget()
    cpf_campo.grid_forget()
    data_nascimento_campo.grid_forget()
    telefone_campo.grid_forget()
    email_campo.grid_forget()
    endereco_campo.grid_forget()
    aro_campo.grid_forget()
    cliente_campo.grid_forget()
    condicao_campo.grid_forget()
    idcliente_campo.grid_forget()
    cor_campo.grid_forget()
    label_nome_campo.grid_forget()
    label_rg_campo.grid_forget()
    label_cpf_campo.grid_forget()
    label_data_nascimento_campo.grid_forget()
    label_telefone_campo.grid_forget()
    label_email_campo.grid_forget()
    label_endereco_campo.grid_forget()
    label_aro_campo.grid_forget()
    label_cliente_campo.grid_forget()
    label_condicao_campo.grid_forget()
    label_cor_campo.grid_forget()
    label_idcliente_campo.grid_forget()
    label_nome.grid_forget()
    bike_campo.grid_forget()
    submeter_retirada_campo.grid_forget()
    cliente_combo.grid_forget()
    bike_combo.grid_forget()
    label_bike_info.grid_forget()
    botao_editar_bike.grid_forget()
    botao_editar_cliente.grid_forget()
    idbike_campo.grid_forget()

def limpar_entry():
    nome_campo.delete(0, tk.END)
    rg_campo.delete(0, tk.END)
    cpf_campo.delete(0, tk.END)
    data_nascimento_campo.delete(0, tk.END)
    telefone_campo.delete(0, tk.END)
    email_campo.delete(0, tk.END)
    endereco_campo.delete(0, tk.END)
    cliente_campo.delete(0, tk.END)
    aro_campo.delete(0, tk.END)
    condicao_campo.delete(0, tk.END)
    idcliente_campo.delete(0, tk.END)
    bike_campo.delete(0, tk.END)
    cor_campo.delete(0, tk.END)
    submeter_retirada_campo.delete(0, tk.END)

def centralizar_janela(janela):
    janela.update_idletasks()
    largura_janela = janela.winfo_width()
    altura_janela = janela.winfo_height()
    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()
    pos_x = (largura_tela // 2) - (largura_janela // 2)
    pos_y = (altura_tela // 2) - (altura_janela // 2)
    janela.geometry(f'{largura_janela}x{altura_janela}+{pos_x}+{pos_y}')

# Cria a janela principal
janela = tk.Tk()
janela.title("Bicicletário Techbit")
janela.geometry("600x400")
centralizar_janela(janela)


# Widgets da tela de login (inicialmente visíveis)
botao_entrada = tk.Button(janela, text="Entrada de bike", command=mostrar_tela_entrada)
botao_entrada.grid()

botao_retirada = tk.Button(janela, text="Retirada de bike", command=mostrar_tela_retirada)
botao_retirada.grid()

#botao_deletar_user = tk.Button(janela, text="Deletar usuário", command=deletar_user)
#botao_deletar_bike = tk.Button(janela, text="Deletar bike", command=mostrar_tela_inicial)


# Widgets da tela de cadastro (inicialmente ocultos)
botao_cliente = tk.Button(janela, text="Novo Cliente", command=mostrar_tela_cadastro)
botao_bike = tk.Button(janela, text="Nova Bike", command=mostrar_tela_bike)
botao_editar_cliente = tk.Button(janela, text="Editar Cliente", command=editar_cliente)
botao_editar_bike = tk.Button(janela, text="Editar Bike", command=editar_bike)
botao_update_cliente = tk.Button(janela, text="Atualizar Cadastro do Cliente", command=update_cliente)
botao_update_bike = tk.Button(janela, text="Atualizar Cadastro da Bike", command=update_bike)
botao_deletar_cliente = tk.Button(janela, text="Deletar Cliente Selecionado", command=delete_client)
botao_deletar_bike = tk.Button(janela, text="Deletar Bike Selecionada", command=delete_bike)
botao_submeter_retirada = tk.Button(janela, text="Submeter Retirada", command=mostrar_tela_inicial)
botao_cadastrar_cliente = tk.Button(janela, text="Cadastrar Cliente", command=cadastrar_cliente)
botao_cadastrar_bike = tk.Button(janela, text="Cadastrar", command=cadastrar_bike)
botao_cancelar = tk.Button(janela, text="Cancelar", command=mostrar_tela_inicial)
botao_cancelar_entrada_bike = tk.Button(janela, text="Cancelar", command=mostrar_tela_entrada)
botao_registrar = tk.Button(janela, text="Registrar", command=registrar_movimentacao)


# Label nomeia os campos de entrada "Entry"
label_nome_campo = tk.Label(janela, text="Nome:")
label_rg_campo = tk.Label(janela, text="RG:")
label_cpf_campo = tk.Label(janela, text="CPF:")
label_data_nascimento_campo = tk.Label(janela, text="Data de nascimento:")
label_telefone_campo = tk.Label(janela, text="Telefone:")
label_email_campo = tk.Label(janela, text="Email:")
label_endereco_campo = tk.Label(janela, text="Endereço:")
label_cliente_campo = tk.Label(janela, text="Cliente")
label_idcliente_campo = tk.Label(janela, text="ID Cliente")
label_idbike_campo = tk.Label(janela, text="ID Bike")
label_aro_campo = tk.Label(janela, text="Aro")
label_cor_campo = tk.Label(janela, text="Cor")
label_condicao_campo = tk.Label(janela, text="Condições")
label_nome = tk.Label(janela, text="")
label_bike_info = tk.Label(janela, text="")



# Campos de entrada (inputs)
nome_campo = Entry(janela)
rg_campo = Entry(janela)
cpf_campo = Entry(janela)
data_nascimento_campo = Entry(janela)
telefone_campo = Entry(janela)
email_campo = Entry(janela)
endereco_campo = Entry(janela)
cliente_campo = Entry(janela)
aro_campo = Entry(janela)
condicao_campo = Entry(janela)
idcliente_campo = Entry(janela)
idbike_campo = Entry(janela)
bike_campo = Entry(janela)
cor_campo = Entry(janela)
submeter_retirada_campo = Entry(janela)

# Campo combobox (retorno)
cliente_combo = ttk.Combobox(janela)
bike_combo = ttk.Combobox(janela)


janela.mainloop()