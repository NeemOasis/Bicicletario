import socket
import json

import SQLConnection as sql

# Criação do socket
HOST = 'DESKTOP-GC4CVEH'  # Endereço IP do servidor
PORT = 65432       # Porta


def read_json(data):
    action = data["action"]

    if action == "insert_client":
        name = data["data"]["name"] or None
        cpf = data["data"]["cpf"] or None
        rg = data["data"]["rg"] or None
        email = data["data"]["email"] or None
        telephone = data["data"]["tel"] or None
        address = data["data"]["street"] or None
        date = data["data"]["date"] or None

        sql.insert_client(name, rg, cpf, email, telephone, address, date)

        return None

    elif action == "update_client":
        cpf = data["data"]["cpf"] or None
        name = data["data"]["name"] or None
        email = data["data"]["email"] or None
        telephone = data["data"]["tel"] or None
        address = data["data"]["street"] or None

        sql.update_client(cpf, name, email, telephone, address)

        return None

    elif action == "select_client_by_cpf":
        cpf = data["data"]["cpf"] or None

        return sql.select_client(f"cpf LIKE '{cpf}%'")

    elif action == "insert_bike":
        rim = data["data"]["rim"] or None
        condition = data["data"]["condition"] or None
        id_client = data["data"]["id_client"] or None
        status = data["data"]["status"] or None

        sql.insert_bike(rim, condition, id_client, status)

        return None

    elif action == "update_bike":
        id_bike = data["data"]["id_bike"] or None
        condition = data["data"]["condition"] or None
        status = data["data"]["status"] or None

        sql.update_bike(id_bike, condition, status)

        return None

    elif action == "select_bike_by_id":
        id = data["data"]["id"] or None

        return sql.select_bike(f"id_bike = '{id}'")
    
    elif action == "select_bikes_by_client":
        cpf = data["data"]["cpf"] or None

        return sql.select_bike(f"id_cliente = '{cpf}'")

    elif action == "insert_movement":
        id_bike = data["data"]["id_bike"] or None

        sql.insert_movement(id_bike, True)

        return None

    elif action == "update_movement":
        id_movement = data["data"]["id_movement"] or None

        sql.update_movement(id_movement)

        return None

    elif action == "select_movement_by_id":
        id = data["data"]["id_movement"] or None

        return sql.select_movement(f"id_movimentacao = '{id}'")
    
    elif action == "select_movements_by_bike":
        id = data["data"]["id_bike"] or None

        return sql.select_movement(f"id_bike = '{id}'")


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print('Esperando conexões...')
    while True:
        conn, addr = s.accept()
        with conn:
            print('Conectado por', addr)
            while True:
                data = conn.recv(1024)
                if data:
                    print('dados recebidos')
                    dados_recebidos = json.loads(data.decode())
                    print(dados_recebidos)
                    result = read_json(dados_recebidos)

                    if result is not None: 
                        conn.send(str(result).encode('utf-8'))
                    
                    break