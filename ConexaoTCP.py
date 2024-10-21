import socket
import json

# Configurações do cliente
HOST = '192.168.0.106'  # Endereço IP do servidor
PORT = 65432        # Porta

def send_to_server(dados):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))

        # Dados a serem enviados
        data = json.dumps(dados).encode()

        s.sendall(data)

def request_insert_client(name, cpf, rg, email, tel, street, date):
    dados = {
                "action": "insert_client",
                "data": {
                    "name": name,
                    "cpf": cpf,
                    "rg": rg,
                    "email": email,
                    "tel": tel,
                    "street": street,
                    "date": date
                }
            }

    send_to_server(dados)

def request_insert_bike(rim, condition, id_client, status):
        dados = {
                     "action": "insert_bike",
                     "data": {
                         "rim": rim,
                         "condition": condition,
                         "id_client": id_client,
                         "status": status
                     }
                 }

        send_to_server(dados)

def request_insert_movement(id_bike):
        dados = {
                     "action": "insert_movement",
                     "data": {
                         "id_bike": id_bike
                     }
                 }

        send_to_server(dados)

def request_update_client(name, email, tel, street, cpf):
        dados = {
                     "action": "update_client",
                     "data": {
                         "name": name,
                         "email": email,
                         "tel": tel,
                         "street": street,
                         "cpf": cpf
                     }
                 }

        send_to_server(dados)

def request_update_bike(condition, status, id_bike):
        dados = {
                     "action": "update_bike",
                     "data": {
                         "condition": condition,
                         "status": status,
                         "id_bike": id_bike
                     }
                 }

        send_to_server(dados)

def request_update_movement(id_movement):
        dados = {
                     "action": "update_movement",
                     "data": {
                         "id_movement": id_movement
                     }
                 }

        send_to_server(dados)