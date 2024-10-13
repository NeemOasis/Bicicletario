import tkinter as tk
from tkinter import *

def mostrar_tela_inicial():
    # ... Esconde widgets da tela de cadastro ...
    limpar_botoes()

    # Mostra widgets da tela de login
    botao_entrada.grid()
    botao_retirada.grid()

def mostrar_tela_entrada():
    limpar_botoes()

    botao_cliente.grid()
    botao_bike.grid()


def mostrar_tela_cadastro():
    # ... Esconde widgets da tela de login ...
    limpar_botoes()

    # Mostra widgets da tela de cadastro
    botao_cadastrar.grid(row=0, column=3)

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
    botao_cadastrar_bike.grid()

    cliente = cliente_campo.grid()
    aro = aro_campo.grid()
    condicao = condicao_campo.grid()
    status = status_campo.grid()



def mostrar_tela_retirada():
    limpar_botoes()

    botao_submeter_retirada.grid()

def limpar_botoes():
    botao_entrada.grid_forget()
    botao_retirada.grid_forget()
    botao_submeter_retirada.grid_forget()
    botao_cliente.grid_forget()
    botao_cadastrar.grid_forget()
    botao_bike.grid_forget()
    botao_cadastrar_bike.grid_forget()
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
    status_campo.grid_forget()
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
    label_status_campo.grid_forget()


# Cria a janela principal
janela = tk.Tk()
janela.title("Bicicletário Techbit")
janela.geometry("600x400")


# Widgets da tela de login (inicialmente visíveis)
botao_entrada = tk.Button(janela, text="Entrada de bike", command=mostrar_tela_entrada)
botao_entrada.grid()

botao_retirada = tk.Button(janela, text="Retirada de bike", command=mostrar_tela_retirada)
botao_retirada.grid()


# Widgets da tela de cadastro (inicialmente ocultos)
botao_cliente = tk.Button(janela, text="Cliente", command=mostrar_tela_cadastro)
botao_bike = tk.Button(janela, text="Bike", command=mostrar_tela_bike)
botao_submeter_retirada = tk.Button(janela, text="Submeter retirada", command=mostrar_tela_inicial)
botao_cadastrar = tk.Button(janela, text="Cadastrar", command=mostrar_tela_inicial)
botao_cadastrar_bike = tk.Button(janela, text="Cadastrar", command=mostrar_tela_inicial)


# Label nomeia os campos de entrada "Entry"
label_nome_campo = tk.Label(janela, text="Nome:")
label_rg_campo = tk.Label(janela, text="RG:")
label_cpf_campo = tk.Label(janela, text="CPF:")
label_data_nascimento_campo = tk.Label(janela, text="Data de nascimento:")
label_telefone_campo = tk.Label(janela, text="Telefone:")
label_email_campo = tk.Label(janela, text="Email:")
label_endereco_campo = tk.Label(janela, text="Endereço:")
label_cliente_campo = tk.Label(janela, text="Cliente")
label_aro_campo = tk.Label(janela, text="Aro")
label_condicao_campo = tk.Label(janela, text="Condições")
label_status_campo = tk.Label(janela, text="Status")


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
status_campo = Entry(janela)

janela.mainloop()