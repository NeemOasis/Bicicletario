import tkinter as tk
from tkinter import *

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

def cadastrar_bike():
    cliente = str(cliente_campo.get())
    server.request_insert_bike(aro_campo.get(),
        condicao_campo.get(),
        cliente_campo.get(),
        cor_campo.get())

    limpar_entry()
    mostrar_tela_entrada()


def registrar_movimentacao():
    server.request_insert_movement(bike_campo.get())

    limpar_entry()
    mostrar_tela_inicial()


def mostrar_tela_entrada():
    ## retornar
    limpar_botoes()

    cliente = cliente_campo.grid(row=0, column=0)
    bike = bike_campo.grid(row=1, column=0)


    botao_cliente.grid(row=0, column=1)
    botao_bike.grid(row=1,column=1)
    botao_registrar.grid(row=2, column=1)
    botao_cancelar.grid(row=3, column=1)


def mostrar_tela_cadastro():
    # ... Esconde widgets da tela de login ...
    limpar_botoes()

    # Mostra widgets da tela de cadastro
    botao_cadastrar_cliente.grid(row=8, column=3)
    botao_cancelar_entrada_bike.grid(row=9, column=3)

    label_nome_campo.grid(row=1, column=0)
    label_rg_campo.grid(row=2, column=0)
    label_cpf_campo.grid(row=3, column=0)
    label_data_nascimento_campo.grid(row=4, column=0)
    label_telefone_campo.grid(row=5, column=0)
    label_email_campo.grid(row=6, column=0)
    label_endereco_campo.grid(row=7, column=0)


    nome = nome_campo.grid(row=1, column=1)
    rg = rg_campo.grid(row=2, column=1)
    cpf = cpf_campo.grid(row=3, column=1)
    data_nascimento = data_nascimento_campo.grid(row=4, column=1)
    telefone = telefone_campo.grid(row=5, column=1)
    email = email_campo.grid(row=6, column=1)
    endereco = endereco_campo.grid(row=7, column=1)


def mostrar_tela_bike():
    limpar_botoes()
    botao_cadastrar_bike.grid(row=5, column=3)
    botao_cancelar_entrada_bike.grid(row=6, column=3)

    label_idcliente_campo.grid(row=1, column=0)
    label_aro_campo.grid(row=2, column=0)
    label_cor_campo.grid(row=3, column=0)
    label_condicao_campo.grid(row=4, column=0)


    cliente = cliente_campo.grid(row=1, column=2)
    aro = aro_campo.grid(row=2, column=2)
    cor = cor_campo.grid(row=3, column=2)
    condicao = condicao_campo.grid(row=4, column=2)

    limpar_entry()





def mostrar_tela_retirada():
    limpar_botoes()

    submeter = submeter_retirada_campo.grid()

    botao_submeter_retirada.grid()
    botao_cancelar.grid()

    limpar_entry()


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
    bike_campo.grid_forget()
    submeter_retirada_campo.grid_forget()

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



# Cria a janela principal
janela = tk.Tk()
janela.title("Bicicletário Techbit")
janela.geometry("600x400")
#janela.grid(sticky="nsew")
#janela.rowconfigure(0, weight=1)
#janela.columnconfigure(0, weight=1)
#janela.columnconfigure(1, weight=1)


# Widgets da tela de login (inicialmente visíveis)
botao_entrada = tk.Button(janela, text="Entrada de bike", command=mostrar_tela_entrada)
botao_entrada.grid()

botao_retirada = tk.Button(janela, text="Retirada de bike", command=mostrar_tela_retirada)
botao_retirada.grid()


# Widgets da tela de cadastro (inicialmente ocultos)
botao_cliente = tk.Button(janela, text="Cliente", command=mostrar_tela_cadastro)
botao_bike = tk.Button(janela, text="Bike", command=mostrar_tela_bike)
botao_submeter_retirada = tk.Button(janela, text="Submeter retirada", command=mostrar_tela_inicial)
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
label_aro_campo = tk.Label(janela, text="Aro")
label_cor_campo = tk.Label(janela, text="Cor")
label_condicao_campo = tk.Label(janela, text="Condições")



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
bike_campo = Entry(janela)
cor_campo = Entry(janela)
submeter_retirada_campo = Entry(janela)


janela.mainloop()