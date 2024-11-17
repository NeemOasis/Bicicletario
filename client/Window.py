import tkinter as tk
import json
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime
from resources.bike import BikeStatus
from resources.client import Client

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
    server.request_insert_bike(aro_campo.get(),
        condicao_campo.get(),
        cliente_campo.get(),
        BikeStatus.INSERT.value)

    limpar_entry()
    mostrar_tela_entrada()
    messagebox.showinfo("Cadastro", "Bike cadastrado com sucesso!")
    

def registrar_movimentacao():
    info = bike_combo.get()

    bikes = server.request_select_bike(info)
    bike = bikes[0]

    if bike.status_bike == BikeStatus.NOT_VALID.value:
        messagebox.showerror("Movimentação", "Não é possível fazer registro de movimentação, bike foi revogada do sistema")
    elif bike.status_bike == BikeStatus.ENTRY.value:
        messagebox.showerror("Movimentação", "Não é possível fazer registro de movimentação, bike já tem uma entrada registrada")
    else:
        server.request_insert_movement(bike.id_bike)
        server.request_update_bike(bike.condicao, BikeStatus.ENTRY.value, bike.id_bike)

        limpar_entry()
        mostrar_tela_inicial()
        messagebox.showinfo("Movimentação", f"Movimentação registrada com sucesso!")


def client_search_database(event):
    label_bike_info.config(text="")
    label_nome.config(text="")

    info = cliente_combo.get()
    clientes = server.request_select_client(info)

    valores_combobox = [cliente.cpf for cliente in clientes]
    cliente_combo['values'] = valores_combobox

def bike_search_database():
    cpf = cliente_combo.get()
    bikes = server.request_select_bike_by_client(cpf)

    valores_combobox = [bike.id_bike for bike in bikes]
    bike_combo['values'] = valores_combobox

def select_client_combo(event):
    label_bike_info.config(text="")
    info = cliente_combo.get()
    clientes = server.request_select_client(info)
    cliente = clientes[0]

    label_nome.config(text=f"nome do cliente: {cliente.nome}")

    bike_search_database()

def select_bike_combo(event):
    info = bike_combo.get()

    bikes = server.request_select_bike(info)
    bike = bikes[0]

    label_bike_info.config(text=f"aro: {bike.aro}, condicao: {bike.condicao}, status: {bike.status_bike}")

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
    label_condicao_campo.grid(row=3, column=0)


    cliente_campo.grid(row=1, column=2)
    aro_campo.grid(row=2, column=2)
    condicao_campo.grid(row=3, column=2)

    limpar_entry()

def mostrar_tela_retirada():
    limpar_botoes()

    submeter_retirada_campo.grid()
    label_movimentacao_info.grid()

    botao_procurar_movimentacao.grid()
    botao_submeter_retirada.grid()
    botao_cancelar.grid()

    limpar_entry()


def procurar_movimentacao():
    movements = server.request_select_movement_by_id(submeter_retirada_campo.get())
    movement = movements[0]

    bikes = server.request_select_bike(movement.id_bike)
    bike = bikes[0]

    clientes = server.request_select_client(bike.id_cliente)
    cliente = clientes[0]

    label_movimentacao_info.config(text=f"bike id: {bike.id_bike}, bike status: {bike.status_bike}, bike condicao: {bike.condicao}, cliente cpf: {cliente.cpf}, cliente nome: {cliente.nome}")


def submeter_retirada():
    movements = server.request_select_movement_by_id(submeter_retirada_campo.get())
    movement = movements[0]

    bikes = server.request_select_bike(movement.id_bike)
    bike = bikes[0]

    if bike.status_bike == BikeStatus.NOT_VALID.value:
        messagebox.showerror("Submeter Retirada", "Não é possível fazer retira, pois bika consta como removida do sistema")
    elif bike.status_bike == BikeStatus.REMOVAL.value:
        messagebox.showerror("Submeter Retirada", "Não é possível fazer retirada, bike já consta como retirado")
    else:
        server.request_update_movement(submeter_retirada_campo.get())
        server.request_update_bike(bike.condicao, BikeStatus.REMOVAL.value, bike.id_bike)

        movements = server.request_select_movement_by_id(submeter_retirada_campo.get())
        movement = movements[0]

        formato = "%Y-%m-%d %H:%M:%S.%f"
        entrada = datetime.strptime(movement.data_entrada, formato)
        saida = datetime.strptime(movement.data_saida, formato)

        diferenca = saida - entrada
        minutos = diferenca.total_seconds() / 60

        messagebox.showinfo("Resultado final", f"bike retirada: {bike.id_bike}, minutos utilizados: {minutos:.0f}")

        limpar_entry()
        mostrar_tela_inicial()
        messagebox.showinfo("Retirada de Bike", "Retirada registrada com sucesso")
    

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
        nome_campo.insert(0, cliente.nome)
        rg_campo.insert(0, cliente.rg)
        cpf_campo.insert(0, cliente.cpf)
        email_campo.insert(0, cliente.email)
        telefone_campo.insert(0, cliente.telefone)
        endereco_campo.insert(0, cliente.endereco)
        data_nascimento_campo.insert(0, cliente.data_nascimento)

    botao_update_cliente.grid(row=8, column=3)
    botao_cancelar_entrada_bike.grid(row=9, column=3)


def mostrar_tela_editar_bike(bike):
    limpar_botoes()

    label_idbike_campo.grid(row=0, column=0)
    label_idcliente_campo.grid(row=1, column=0)
    label_aro_campo.grid(row=2, column=0)
    label_status_campo.grid(row=3, column=0)
    label_condicao_campo.grid(row=4, column=0)

    idbike_campo.grid(row=0, column=2)
    cliente_campo.grid(row=1, column=2)
    aro_campo.grid(row=2, column=2)
    status_campo.grid(row=3, column=2)
    condicao_campo.grid(row=4, column=2)

    limpar_entry()

    if bike is not None:
        idbike_campo.insert(0, bike.id_bike)
        cliente_campo.insert(0, bike.id_cliente)
        aro_campo.insert(0, bike.aro)
        status_campo.insert(0, bike.status_bike)
        condicao_campo.insert(0, bike.condicao)

    botao_update_bike.grid(row=5, column=3)
    botao_deletar_bike.grid(row=6, column=3)
    botao_cancelar_entrada_bike.grid(row=7, column=3)

def editar_cliente():
    info = cliente_combo.get()
    clientes = server.request_select_client(info)
    cliente = clientes[0]

    mostrar_tela_editar_cliente(cliente)
    
def editar_bike():
    info = bike_combo.get()

    bikes = server.request_select_bike(info)
    bike = bikes[0]

    mostrar_tela_editar_bike(bike)

def update_cliente():
    server.request_update_client(nome_campo.get(),
                                 email_campo.get(),
                                 telefone_campo.get(),
                                 endereco_campo.get(),
                                 cpf_campo.get())

    limpar_entry()
    mostrar_tela_entrada()
    messagebox.showinfo("Atualizado", "Cliente atualizado com sucesso!")


def update_bike():
    server.request_update_bike(condicao_campo.get(),
                                 status_campo.get(),
                                 idbike_campo.get())

    limpar_entry()
    mostrar_tela_entrada()
    messagebox.showinfo("Atualizada", "Bicicleta atualizado com sucesso!")

def deletar_bike():
    server.request_update_bike(condicao_campo.get(),
                                 BikeStatus.NOT_VALID.value,
                                 idbike_campo.get())

    limpar_entry()
    mostrar_tela_entrada()
    messagebox.showinfo("Atualizada", "Bicicleta desvinculada com sucesso")


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
    botao_update_cliente.grid_forget()
    botao_update_bike.grid_forget()
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
    botao_deletar_bike.grid_forget()


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
    status_campo.delete(0, tk.END)
    submeter_retirada_campo.delete(0, tk.END)
    idbike_campo.delete(0, tk.END)

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

# Widgets da tela de cadastro (inicialmente ocultos)
botao_cliente = tk.Button(janela, text="Novo Cliente", command=mostrar_tela_cadastro)
botao_bike = tk.Button(janela, text="Nova Bike", command=mostrar_tela_bike)
botao_editar_cliente = tk.Button(janela, text="Editar Cliente", command=editar_cliente)
botao_editar_bike = tk.Button(janela, text="Editar Bike", command=editar_bike)
botao_update_cliente = tk.Button(janela, text="Atualizar Cadastro do Cliente", command=update_cliente)
botao_update_bike = tk.Button(janela, text="Atualizar Cadastro da Bike", command=update_bike)
botao_submeter_retirada = tk.Button(janela, text="Submeter Retirada", command=submeter_retirada)
botao_cadastrar_cliente = tk.Button(janela, text="Cadastrar Cliente", command=cadastrar_cliente)
botao_cadastrar_bike = tk.Button(janela, text="Cadastrar", command=cadastrar_bike)
botao_cancelar = tk.Button(janela, text="Cancelar", command=mostrar_tela_inicial)
botao_cancelar_entrada_bike = tk.Button(janela, text="Cancelar", command=mostrar_tela_entrada)
botao_registrar = tk.Button(janela, text="Registrar Movimentação", command=registrar_movimentacao)
botao_procurar_movimentacao = tk.Button(janela, text="Procurar movimentação", command=procurar_movimentacao)
botao_deletar_bike = tk.Button(janela, text="Deletar bike", command=deletar_bike)



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
label_status_campo = tk.Label(janela, text="status")
label_condicao_campo = tk.Label(janela, text="Condições")
label_nome = tk.Label(janela, text="")
label_bike_info = tk.Label(janela, text="")
label_movimentacao_info = tk.Label(janela, text="")




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
status_campo = Entry(janela)
submeter_retirada_campo = Entry(janela)

# Campo combobox (retorno)
cliente_combo = ttk.Combobox(janela)
bike_combo = ttk.Combobox(janela)


janela.mainloop()

