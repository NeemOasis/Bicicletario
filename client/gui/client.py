from tkinter import *
import tkinter as tk 
from typing import Optional
from pydantic import BaseModel

class Client(BaseModel):
    name: str
    rg: str
    cpf: str
    email: str
    tel: str
    address: str
    birth_date: str
    id: Optional[int] = None


def create_labels(window):
    labels = {
        "name": tk.Label(window, text="Nome"),
        "rg": tk.Label(window, text="RG"),
        "cpf": tk.Label(window, text="CPF"),
        "birth_date": tk.Label(window, text="Data de nascimento"),
        "tel": tk.Label(window, text="Telefone"),
        "email": tk.Label(window, text="Email"),
        "address": tk.Label(window, text="Endereço"),
        "id": tk.Label(window, text="ID Cliente"),
        "info_name": tk.Label(window, text=""),
        "info_rg": tk.Label(window, text=""),
        "info_cpf": tk.Label(window, text=""),
        "info_birth_date": tk.Label(window, text=""),
        "info_tel": tk.Label(window, text=""),
        "info_email": tk.Label(window, text=""),
        "info_address": tk.Label(window, text=""),
        "info_id": tk.Label(window, text="")
    }

    return labels


def create_entries(window):
    entries = {
        "name": tk.Entry(window),
        "rg": tk.Entry(window),
        "cpf": tk.Entry(window),
        "birth_date": tk.Entry(window),
        "tel": tk.Entry(window),
        "email": tk.Entry(window),
        "address": tk.Entry(window),
        "id": tk.Entry(window)
    }

    return entries


def clean_widgets(labels=None, entries=None, buttons=None):
    if labels:
        for label in labels.values():
            label.grid_forget()
    
    if entries:
        for entry in entries.values():
            entry.grid_forget()

    if buttons:
        for button in buttons:
            button.grid_forget()


def show_client_form(labels, entries, buttons=None, client: Client=None):
    labels["name"].grid(row=0, column=0)
    labels["rg"].grid(row=1, column=0)
    labels["cpf"].grid(row=2, column=0)
    labels["email"].grid(row=3, column=0)
    labels["tel"].grid(row=4, column=0)
    labels["birth_date"].grid(row=5, column=0)
    labels["address"].grid(row=6, column=0)

    entries["name"].grid(row=0, column=1)
    entries["rg"].grid(row=1, column=1)
    entries["cpf"].grid(row=2, column=1)
    entries["email"].grid(row=3, column=1)
    entries["tel"].grid(row=4, column=1)
    entries["birth_date"].grid(row=5, column=1)
    entries["address"].grid(row=6, column=1)

    if buttons:
        for i, button in enumerate(buttons):
            button.grid(row=8+i, column=0, columnspan=2)

    if client:
        entries["name"].insert(0, client.name)
        entries["rg"].insert(0, client.rg)
        entries["cpf"].insert(0, client.cpf)
        entries["email"].insert(0, client.email)
        entries["tel"].insert(0, client.tel)
        entries["birth_date"].insert(0, client.birth_date)
        entries["address"].insert(0, client.address)


def show_client_info(labels, client: Client):
    labels["info_id"].grid(row=0, column=3)
    labels["info_name"].grid(row=1, column=3)
    labels["info_rg"].grid(row=2, column=3)
    labels["info_cpf"].grid(row=3, column=3)
    labels["info_email"].grid(row=4, column=3)
    labels["info_tel"].grid(row=5, column=3)
    labels["info_birth_date"].grid(row=6, column=3)
    labels["info_address"].grid(row=7, column=3)

    labels["info_id"].config(text=client.id)
    labels["info_name"].config(text=client.name)
    labels["info_rg"].config(text=client.rg)
    labels["info_cpf"].config(text=client.cpf)
    labels["info_email"].config(text=client.email)
    labels["info_tel"].config(text=client.tel)
    labels["info_birth_date"].config(text=client.birth_date)
    labels["info_address"].config(text=client.address)


window = tk.Tk()
window.geometry("600x400")

labels_client = create_labels(window)
entries_client = create_entries(window)

c = Client(name="Walber", rg="50", cpf="50", email="email", tel="telefone", address="address", birth_date="data")


show_client_form(labels=labels_client, entries=entries_client, client=c)
show_client_info(labels=labels_client, client=c)


window.mainloop()