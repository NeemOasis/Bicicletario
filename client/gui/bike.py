from tkinter import *
import tkinter as tk 
from typing import Optional
from pydantic import BaseModel

class Bike(BaseModel):
    id_bike: Optional[int] = None
    id_client: str
    rim: str
    conditions: str
    status: str

def create_labels(window):
    labels = {
        "id_bike": tk.Label(window, text="ID Bike"),
        "id_client": tk.Label(window, text="ID Cliente"),
        "rim": tk.Label(window, text="Aro"),
        "conditions": tk.Label(window, text="Condições"),
        "status": tk.Label(window, text="Status")
    }

    return labels

def show_bike_info(labels, bike: Bike):
    labels["id_bike"].grid(row=0, column=4)
    labels["id_client"].grid(row=1, column=4)
    labels["rim"].grid(row=2, column=4)
    labels["conditions"].grid(row=3, column=4)
    labels["status"].grid(row=4, column=4)

    labels["id_bike"].config(Text=bike.id_bike)
    labels["id_client"].config(text=bike.id_client)
    labels["rim"].config(text=bike.rim)
    labels["conditions"].config(text=bike.conditions)
    labels["status"].config(text=bike.status)

def create_entries(window):
    entries = {
        "id_client": tk.Entry(window),
        "rim": tk.Entry(window),
        "conditions": tk.Entry(window),
        "status": tk.Entry(window),
    }

    return entries

def show_bike_form(labels, entries, buttons=None, bike: Bike=None):
    labels["id_client"].grid(row=1, column=1)
    labels["rim"].grid(row=2, column=1)
    labels["conditions"].grid(row=3, column=1)
    labels["status"].grid(row=4, column=1)


window = tk.Tk()
window.geometry("600x400")

b = Bike(id_client="123", rim="123", conditions="123", status="entrada")

bike = create_labels(window)
entry = create_entries(window)
show_bike_info(labels=bike, bike=b)
show_bike_form(labels=bike, entries=entry)


window.mainloop()

