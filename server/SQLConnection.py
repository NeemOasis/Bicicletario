import pyodbc

sqlserver_conncetion = (
    "Driver={SQL Server};"
    r"Server=DESKTOP-GC4CVEH\SQLEXPRESS;"
    "Database=PythonSQL;"
)

## CLIENTES ##

def insert_client(name, rg, cpf, email, telephone, address, birth_date):
    try:
        connection = pyodbc.connect(sqlserver_conncetion)
        cursor = connection.cursor()

        cursor.execute("INSERT INTO dbo.Cliente (nome, rg, cpf, email, telefone, endereco, data_nascimento) VALUES (?, ?, ?, ?, ?, ?, ?)",
                       (name, rg, cpf, email, telephone, address, birth_date))
        connection.commit()

        cursor.close()
        connection.close()

        print("Dados inseridos com sucesso!")

    except pyodbc.Error as ex:
        print("Erro ao inserir dados:", ex)


def select_client(where=None):
    try:
        connection = pyodbc.connect(sqlserver_conncetion)
        cursor = connection.cursor()

        query = "SELECT * FROM dbo.Cliente"
        if where is not None:
            query += f" WHERE {where}"

        cursor.execute(query)
        rows = cursor.fetchall()

        cursor.close()
        connection.close()

        return rows

    except pyodbc.Error as ex:
        print("Erro ao recuperar dados:", ex)
        return None


def update_client(cpf, name=None, email=None, telephone=None, address=None):
    try:
        connection = pyodbc.connect(sqlserver_conncetion)
        cursor = connection.cursor()

        old_values = select_client(f"cpf = '{cpf}'")
        if old_values != []:
            old_values = old_values[0]
        else:
            print("Erro ao atualizar dados: não existe nenhum registro com o cpf informado")
            return

        if name is None:
            name = old_values.nome

        if email is None:
            email = old_values.email

        if telephone is None:
            telephone = old_values.telefone

        if address is None:
            address = old_values.endereco

        cursor.execute("UPDATE dbo.Cliente SET nome = ?, email = ?, telefone = ?, endereco = ? WHERE cpf = ?",
                       (name, email, telephone, address, cpf))

        connection.commit()

        cursor.close()
        connection.close()

        print("Dados atualizados com sucesso!")

    except pyodbc.Error as ex:
        print("Erro ao atualizar dados:", ex)

## BIKES ##

def insert_bike(rim, condition, id_client, status):
    try:
        connection = pyodbc.connect(sqlserver_conncetion)
        cursor = connection.cursor()

        cursor.execute(
            "INSERT INTO dbo.Bike (aro, condicao, id_cliente, status_bike) VALUES (CAST(? AS DECIMAL(10,2)), ?, ?, ?)",
            (rim, condition, id_client, status))
        connection.commit()

        cursor.close()
        connection.close()

        print("Dados inseridos com sucesso!")

    except pyodbc.Error as ex:
        print("Erro ao inserir dados:", ex)


def select_bike(where=None):
    try:
        connection = pyodbc.connect(sqlserver_conncetion)
        cursor = connection.cursor()

        query = "SELECT * FROM dbo.Bike"
        if where is not None:
            query += f" WHERE {where}"

        cursor.execute(query)
        rows = cursor.fetchall()

        cursor.close()
        connection.close()

        return rows

    except pyodbc.Error as ex:
        print("Erro ao recuperar dados:", ex)
        return None

def update_bike(id_bike, condition=None, status=None):
    try:
        connection = pyodbc.connect(sqlserver_conncetion)
        cursor = connection.cursor()

        old_values = select_bike(f"id_bike = '{id_bike}'")
        if old_values != []:
            old_values = old_values[0]
        else:
            print("Erro ao atualizar dados: não existe nenhum registro com o cpf informado")
            return

        if condition is None:
            condition = old_values.condicao

        if status is None:
            status = old_values.status_bike

        cursor.execute("UPDATE dbo.Bike SET condicao = ?, status_bike = ? WHERE id_bike = ?",
                       (condition, status, id_bike))

        connection.commit()

        cursor.close()
        connection.close()

        print("Dados atualizados com sucesso!")

    except pyodbc.Error as ex:
        print("Erro ao atualizar dados:", ex)


## MOVEMENT ##


def insert_movement(id_bike, entry_date=False):
    try:
        connection = pyodbc.connect(sqlserver_conncetion)
        cursor = connection.cursor()

        if entry_date is True:
            cursor.execute(
                "INSERT INTO dbo.Movimentacao (id_bike, data_entrada) VALUES (?, GETDATE())",
                (id_bike))
            connection.commit()
        else:
            print("Erro ao inserir dados: a data de entrada precisa ser autorizada para criar registro da movimentação")

        cursor.close()
        connection.close()

        print("Dados inseridos com sucesso!")

    except pyodbc.Error as ex:
        print("Erro ao inserir dados:", ex)

def select_movement(where=None):
    try:
        connection = pyodbc.connect(sqlserver_conncetion)
        cursor = connection.cursor()

        query = "SELECT * FROM dbo.Movimentacao"
        if where is not None:
            query += f" WHERE {where}"

        cursor.execute(query)
        rows = cursor.fetchall()

        cursor.close()
        connection.close()

        return rows

    except pyodbc.Error as ex:
        print("Erro ao recuperar dados:", ex)
        return None


def update_movement(id_movement):
    try:
        connection = pyodbc.connect(sqlserver_conncetion)
        cursor = connection.cursor()

        cursor.execute("UPDATE dbo.Movimentacao SET data_saida = GETDATE() WHERE id_movimentacao = ?",
                       id_movement)
        connection.commit()

        cursor.close()
        connection.close()

        print("Dados atualizados com sucesso!")

    except pyodbc.Error as ex:
        print("Erro ao atualizar dados:", ex)


# def deletar_user():
#     try:
#         connection = pyodbc.connect(sqlserver_conncetion)     
#         cursor = connection.cursor()

#         sql_delete = "DELETE FROM dbo.Cliente WHERE CPF = ?"
    
#         cursor.execute(sql_delete, (cpf,))
#         connection.commit()


#         cursor.close()
#         connection.close()

#         print("Registro deletado com sucesso!")
#     except pyodbc.Error as ex:
#         print("Erro", f"Erro ao deletar registro:", ex)



#insert_client("Walber", "397308218", "222333666", "walberzinhogatinho@yahoo.com.br", "1198902456",
              ##"Rua Alexandre de Morais, 69", "1997-06-07")

#insert_bike('26.99', 'nova', '46238014890', 'entrada' )

#insert_movement(2, True)

#update_client(cpf='46238014890', email='email@gmail.com')

#lista = select_client("cpf = '46238014890'")

#for item in lista:
#    print(item)

#update_client(cpf='46238014890', email='email@gmail.com')

#update_movement(1)

#lista = select_movement("id_movimentacao = '1'")

#for item in lista:
#    print(item)

