import socket
import json
import datetime

from resources.client import Client
from resources.bike import Bike
from resources.movement import Movement

# Configurações do cliente
HOST = 'DESKTOP-GC4CVEH'  # Endereço IP do servidor
PORT = 65432        # Porta

def send_to_server(dados):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))

        # Dados a serem enviados
        data = json.dumps(dados).encode()

        s.sendall(data)

def send_server_and_receive(dados):
       with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))

        # Dados a serem enviados
        data = json.dumps(dados).encode()

        s.sendall(data)

        data = s.recv(1024)

        while data:
            #print('Dados recebidos do servidor:', data.decode('utf-8'))
            data = data.decode('utf-8')
            return data

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


def request_select_client(cpf):
        dados = {
                     "action": "select_client_by_cpf",
                     "data": {
                         "cpf": cpf
                     }
                 }

        results = send_server_and_receive(dados)
        results = eval(results)
        clients = []
        for result in results:
            client = Client(nome=result[0], 
                            rg=result[1],
                            cpf=result[2],
                            email=result[3],
                            telefone=result[4],
                            endereco=result[5],
                            data_nascimento=result[6])
            clients.append(client)
        
        return clients


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

def request_select_bike(id):
    dados = {
            "action": "select_bike_by_id",
            "data": {
                  "id": id
            }
      }

    results = send_server_and_receive(dados)
    results = results.replace('Decimal', '')
    results = eval(results)
    bikes = []
    for result in results:
        bike = Bike(id_bike=result[0], 
                        aro=result[1],
                        condicao=result[2],
                        id_cliente=result[3],
                        status_bike=result[4])
        bikes.append(bike)
    
    return bikes

def request_select_bike_by_client(cpf):
    dados = {
                    "action": "select_bikes_by_client",
                    "data": {
                          "cpf": cpf
                    }
              }
    
    results = send_server_and_receive(dados)
    results = results.replace('Decimal', '')
    results = eval(results)
    bikes = []
    for result in results:
        bike = Bike(id_bike=result[0], 
                        aro=result[1],
                        condicao=result[2],
                        id_cliente=result[3],
                        status_bike=result[4])
        bikes.append(bike)
    
    return bikes

def convert_to_datetime(input_data):
    date_format = "%Y-%m-%d %H:%M:%S.%f"

    output_data = []

    for item in input_data:
        # Verifica se o item é do tipo datetime
        if isinstance(item[2], datetime.datetime) and isinstance(item[3], datetime.datetime):
            # Converte o datetime para string no formato desejado
            formatted_date_1 = item[2].strftime(date_format)
            formatted_date_2 = item[3].strftime(date_format)
            # Cria uma nova tupla com a data convertida
            output_data.append((item[0], item[1], formatted_date_1, formatted_date_2))
        elif isinstance(item[2], datetime.datetime):
            # Converte o datetime para string no formato desejado
            formatted_date_1 = item[2].strftime(date_format)
            # Cria uma nova tupla com a data convertida
            output_data.append((item[0], item[1], formatted_date_1, item[3]))
        else:
            output_data.append(item)

    return output_data

def request_select_movement_by_id(id):
    dados = {
                     "action": "select_movement_by_id",
                     "data": {
                        "id_movement": id
                     }
                 }   

    results = send_server_and_receive(dados)
    results = eval(results)
    results = convert_to_datetime(results)
    movements = []
    for result in results:
        movement = Movement(id_movimentacao=result[0], 
                        id_bike=result[1],
                        data_entrada=result[2],
                        data_saida=result[3])
        print(movement)
        movements.append(movement)
    
    return movements     
      