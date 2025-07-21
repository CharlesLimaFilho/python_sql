import mysql.connector
from datetime import date
from implementações.cliente import Cliente
from implementações.endereco import Endereco
from implementações.ingresso import Ingresso
from implementações.evento import Evento
from implementações.setor import Setor
from implementações.tipo_ingresso import TipoIngresso


# Conecta ao banco de dados MySQL
def connect_to_db(i_host, i_user, i_password, i_database):
    db = mysql.connector.connect(
        host = i_host,
        user = i_user,
        password = i_password,
        database = i_database
    )
    cursor = db.cursor()
    return cursor, db

# Conserta a data
def fix_date(data_str: str):
    if data_str != "-1":
        dia_str, mes_str, ano_str = data_str.split("/")
        return date(int(ano_str), int(mes_str), int(dia_str))
    else:
        return data_str

# Finaliza a conexão
def finish(cursor, db):
    cursor.close()
    db.close()

mycursor, mydb = connect_to_db("", "", "", "ingressos")
options_text = ["\nDigite a tabela desejada: \n[1] - Cliente\n[2] - Endereco\n[3] - Ingresso\n[4] - Evento\n[5] - Setor\n[6] - Tipos de ingressos\n[7] - Outra operacoes\n[0] - Sair\n-> ",
                "\nDigite a opção desejada: \n[1] - Inserir\n[2] - Consultar\n[3] - Atualizar\n[4] - Excluir\n[0] - Retornar\n-> ",
                "\nDigite a opção desejada: \n[1] - Consulta unica\n[2] - Consultar todos\n-> "]

cliente = Cliente()
endereco = Endereco()
evento = Evento()
ingresso = Ingresso()
setor = Setor()
tipo_ingresso = TipoIngresso()

while True:
    options1 = input(options_text[0])
    match options1:
        case "1": # Cliente
            options2 = input(options_text[1])
            match options2:
                case "1": # Inserir Cliente
                    nome = input("Digite o nome do cliente: ")
                    cpf = input("Digite o CPF do cliente: ")
                    data_nascimento = input("Digite a data de nascimento do cliente (DD/MM/AAAA): ")
                    data_nascimento = fix_date(data_nascimento)
                    email = input("Digite o email do cliente: ")
                    id_endereco = input("Digite o ID do endereço do cliente: ")
                    celular = input("Digite o celular do cliente: ")

                    sql, values_cliente = cliente.inserir_cliente(nome, cpf, data_nascimento, email, id_endereco, celular)

                    if values_cliente == 1:
                        print(sql)
                    elif values_cliente == 2:
                        print(sql)
                    else:
                        mycursor.execute(sql, values_cliente)
                        mydb.commit()
                        print("O cliente foi cadastrado com sucesso!\n")

                case "2": # Consultar Cliente
                    options3 = input(options_text[2])

                    match options3:
                        case "1":
                            id_consulta = [input("Digite o id do cliente: ")]
                            sql = cliente.consultar_cliente()
                            mycursor.execute(sql, id_consulta)
                        case "2":
                            sql = cliente.consultar_todos_clientes()
                            mycursor.execute(sql)

                    result = mycursor.fetchall()
                    for row in result:
                        print(f"ID: {row[0]}, Nome: {row[1]}, CPF: {row[2]}, Data de Nascimento: {row[3]}, Email: {row[4]}, ID Endereço: {row[5]}, Celular: {row[6]}")

                case "3": # Atualizar Cliente
                    campos = ["nome", "data_nascimento", "email", "id_endereco", "celular"]
                    novos_dados = []
                    disc_atualizar = {}
                    id_atualizar = input("Digite o id do cliente: ")

                    print("Caso não queira alterar digite '-1'\n")
                    novos_dados.append(input("Digite o novo nome do cliente: "))
                    data = (input("Digite a nova data de nascimento do cliente (DD/MM/AAAA): "))
                    novos_dados.append(fix_date(data))
                    novos_dados.append(input("Digite o novo email do cliente: "))
                    novos_dados.append(input("Digite o ID do novo endereço do cliente: "))
                    novos_dados.append(input("Digite o novo celular do cliente: "))

                    for i, dado in enumerate(novos_dados, start=0):
                        if dado != "-1":
                            disc_atualizar.update({campos[i]: novos_dados[i]})

                    sql, atualizacoes = cliente.atualizar_cliente(disc_atualizar, id_atualizar)
                    mycursor.execute(sql, atualizacoes)
                    mydb.commit()

                case "4": # Excluir Cliente
                    id_excluir = [input("Digite o id do cliente: ")]
                    sql = cliente.deletar_cliente()
                    mycursor.execute(sql, id_excluir)
                    mydb.commit()

                case "0":
                    continue
        case "2":  # Endereco
            options2 = input(options_text[1])
            match options2:
                case "1": # Inserir Endereco
                    rua = input("Digite o nome da rua: ")
                    numero = input("Digite o numero: ")
                    cidade = input("Digite a cidade: ")
                    estado = input("Digite o estado: ")

                    sql, values_endereco = endereco.inserir_endereco(rua, numero, cidade, estado)

                    mycursor.execute(sql, values_endereco)
                    mydb.commit()
                case "2": # Consultar Endereco
                    options3 = input(options_text[2])

                    match options3:
                        case "1":
                            id_endereco = [input("Digite o id do endereco: ")]
                            sql = endereco.consultar_endereco()
                            mycursor.execute(sql, id_endereco)
                        case "2":
                            sql = endereco.consultar_todos_enderecos()
                            mycursor.execute(sql)

                    result = mycursor.fetchall()
                    for row in result:
                        print(f"ID: {row[0]}, Rua: {row[1]}, Numero: {row[2]}, Cidade: {row[3]}, Estado: {row[4]}")
                case "3": # Atualizar Endereco
                    campos = ["rua", "numero", "cidade", "estado"]
                    novos_dados = []
                    disc_atualizar = {}
                    id_atualizar = input("Digite o id do endereco: ")

                    print("Caso não queira alterar digite '-1'\n")
                    novos_dados.append(input("Digite o novo nome da rua: "))
                    novos_dados.append(input("Digite o novo numero: "))
                    novos_dados.append(input("Digite a nova cidade: "))
                    novos_dados.append(input("Digite o novo estado: "))

                    for i, dado in enumerate(novos_dados, start=0):
                        if dado != "-1":
                            disc_atualizar.update({campos[i]: novos_dados[i]})

                    sql, atualizacoes = endereco.atualizar_endereco(disc_atualizar, id_atualizar)
                    mycursor.execute(sql, atualizacoes)
                    mydb.commit()
                case "4": # Excluir Endereco
                    id_excluir = [input("Digite o id do endereco: ")]
                    sql = endereco.deletar_endereco()
                    mycursor.execute(sql, id_excluir)
                    mydb.commit()
                case "0":
                    continue
        case "3":  # Ingresso
            options2 = input(options_text[1])
            match options2:
                case "1": # Inserir Ingresso
                    evento = input("Digite o ID do evento: ")
                    cliente = input("Digite o ID do cliente: ")
                    setor = input("Digite o ID do setor: ")
                    tipo = input("Digite o ID tipo do ingresso: ")

                    # Caclular preco do ingresso
                    mycursor.execute("SELECT valor_base FROM setor WHERE id_setor = %s", tuple(setor))
                    valor_base = mycursor.fetchall()
                    mycursor.execute("SELECT fator FROM tipo_ingresso WHERE id_tipo = %s", tuple(tipo))
                    fator = mycursor.fetchall()
                    preco = valor_base[0][0] * fator[0][0]

                    # Checar limite
                    mycursor.execute("SELECT limite_ingressos_por_cpf FROM evento WHERE id_evento = %s", tuple(evento))
                    limite = mycursor.fetchall()
                    cliente_evento = (cliente, evento)
                    mycursor.execute("SELECT COUNT(*) FROM ingresso WHERE id_cliente = %s AND id_evento = %s", cliente_evento)
                    ingressos_cliente = mycursor.fetchall()
                    if ingressos_cliente[0][0] == limite[0][0]:
                        print("\nLimite de ingressos atingido nesse cpf\n")
                        continue

                    sql, values_ingresso = ingresso.inserir_ingresso(evento, cliente, setor, tipo, preco)

                    mycursor.execute(sql, values_ingresso)
                    mydb.commit()
                case "2": # Consultar Ingresso
                    options3 = input(options_text[2])

                    match options3:
                        case "1":
                            id_ingresso = [input("Digite o id do ingresso: ")]
                            sql = ingresso.consultar_ingresso()
                            mycursor.execute(sql, id_ingresso)
                        case "2":
                            sql = ingresso.consultar_todos_ingressos()
                            mycursor.execute(sql)

                    result = mycursor.fetchall()
                    for row in result:
                        print(f"ID: {row[0]}, ID evento: {row[1]}, ID cliente: {row[2]}, ID setor: {row[3]}, ID tipo: {row[4]}, Preco: {row[5]}")
                case "3": # Atualizar Ingresso
                    campos = ["id_evento", "id_cliente", "id_setor", "id_tipo", "preco_final"]
                    novos_dados = []
                    disc_atualizar = {}
                    id_atualizar = input("Digite o id do ingresso: ")

                    print("Caso não queira alterar digite '-1'\n")
                    novos_dados.append(input("Digite o novo ID de evento: "))
                    novos_dados.append(input("Digite o novo ID de cliente: "))
                    novos_dados.append(input("Digite a nova ID de setor: "))
                    novos_dados.append(input("Digite o novo ID de tipo: "))
                    novos_dados.append(input("Digite o novo preco final: "))

                    for i, dado in enumerate(novos_dados, start=0):
                        if dado != "-1":
                            disc_atualizar.update({campos[i]: novos_dados[i]})

                    sql, atualizacoes = ingresso.atualizar_ingresso(disc_atualizar, id_atualizar)
                    mycursor.execute(sql, atualizacoes)
                    mydb.commit()

                case "4":  # Excluir Ingresso
                    id_excluir = [input("Digite o id do ingresso: ")]
                    sql = ingresso.deletar_ingresso()
                    mycursor.execute(sql, id_excluir)
                    mydb.commit()

                case "0":
                    continue
        case "4":  # Evento
            options2 = input(options_text[1])
            match options2:
                case "1": # Inserir Evento
                    nome = input("Digite o nome do evento ")
                    data = input("Digite a data do evento (DD/MM/AAAA): ")
                    data = fix_date(data)
                    id_endereco = input("Digite o ID do endereco: ")
                    limite = input("Digite o limite de ingressos por cpf: ")

                    sql, values_evento = evento.inserir_evento(nome, data, id_endereco, limite)

                    mycursor.execute(sql, values_evento)
                    mydb.commit()
                case "2": # Consultar Evento
                    options3 = input(options_text[2])

                    match options3:
                        case "1":
                            id_consulta = [input("Digite o id do evento: ")]
                            sql = evento.consultar_evento()
                            mycursor.execute(sql, id_consulta)
                        case "2":
                            sql = evento.consultar_todos_eventos()
                            mycursor.execute(sql)

                    result = mycursor.fetchall()
                    for row in result:
                        print(f"ID: {row[0]}, Nome: {row[1]}, Data: {row[2]}, ID Endereco: {row[3]} Limite: {row[4]}")
                case "3": # Atualizar Evento
                    campos = ["nome", "data", "id_endereco", "limite_ingressos_por_cpf"]
                    novos_dados = []
                    disc_atualizar = {}
                    id_atualizar = input("Digite o id do evento: ")

                    print("Caso não queira alterar digite '-1'\n")
                    novos_dados.append(input("Digite o novo nome do evento: "))
                    data = (input("Digite a nova data do evento (DD/MM/AAAA): "))
                    novos_dados.append(fix_date(data))
                    novos_dados.append(input("Digite o ID do novo endereco: "))
                    novos_dados.append(input("Digite o novo limite: "))

                    for i, dado in enumerate(novos_dados, start=0):
                        if dado != "-1":
                            disc_atualizar.update({campos[i]: novos_dados[i]})

                    sql, atualizacoes = evento.atualizar_evento(disc_atualizar, id_atualizar)
                    mycursor.execute(sql, atualizacoes)
                    mydb.commit()
                case "4": # Excluir Evento
                    id_excluir = [input("Digite o id do evento: ")]
                    sql = evento.deletar_evento()
                    mycursor.execute(sql, id_excluir)
                    mydb.commit()
                case "0":
                    continue
        case "5":  # Setor
            options2 = input(options_text[1])
            match options2:
                case "1": # Inserir Setor
                    nome = input("Digite o nome do setor: ")
                    valor = input("Digite o valor base do setor: ")

                    sql, values_setor = setor.inserir_setor(nome, valor)

                    mycursor.execute(sql, values_setor)
                    mydb.commit()

                case "2": # Consultar Setor
                    options3 = input(options_text[2])

                    match options3:
                        case "1":
                            id_consulta = [input("Digite o id do setor: ")]
                            sql = setor.consultar_setor()
                            mycursor.execute(sql, id_consulta)
                        case "2":
                            sql = setor.consultar_todos_setores()
                            mycursor.execute(sql)

                    result = mycursor.fetchall()
                    for row in result:
                        print(f"ID: {row[0]}, Nome: {row[1]}, Valor: {row[2]}")
                case "3": # Atualizar Setor
                    campos = ["nome", "valor_base"]
                    novos_dados = []
                    disc_atualizar = {}
                    id_atualizar = input("Digite o id do setor: ")

                    print("Caso não queira alterar digite '-1'\n")
                    novos_dados.append(input("Digite o novo nome do setor: "))
                    novos_dados.append(input("Digite o novo valor base: "))

                    for i, dado in enumerate(novos_dados, start=0):
                        if dado != "-1":
                            disc_atualizar.update({campos[i]: novos_dados[i]})

                    sql, atualizacoes = setor.atualizar_setor(disc_atualizar, id_atualizar)
                    mycursor.execute(sql, atualizacoes)
                    mydb.commit()

                case "4": # Excluir Setor
                    id_excluir = [input("Digite o id do setor: ")]
                    sql = setor.deletar_setor()
                    mycursor.execute(sql, id_excluir)
                    mydb.commit()

                case "0":
                    continue
        case "6":  # Tipos de ingressos
            options2 = input(options_text[1])
            match options2:
                case "1": # Inserir Tipo de Ingresso
                    nome = input("Digite o nome do tipo de ingresso: ")
                    fator = input("Digite o fator: ")

                    sql, values_tipo_ingresso = tipo_ingresso.inserir_tipo(nome, fator)

                    mycursor.execute(sql, values_tipo_ingresso)
                    mydb.commit()

                case "2": # Consultar Tipo de Ingresso
                    options3 = input(options_text[2])

                    match options3:
                        case "1":
                            id_consulta = [input("Digite o id do tipo: ")]
                            sql = tipo_ingresso.consultar_tipo()
                            mycursor.execute(sql, id_consulta)
                        case "2":
                            sql = tipo_ingresso.consultar_todos_tipos()
                            mycursor.execute(sql)

                    result = mycursor.fetchall()
                    for row in result:
                        print(f"ID: {row[0]}, Nome: {row[1]}, Fator: {row[2]}")

                case "3": # Atualizar Tipo de Ingresso
                    campos = ["nome", "fator"]
                    novos_dados = []
                    disc_atualizar = {}
                    id_atualizar = input("Digite o id do tipo: ")

                    print("Caso não queira alterar digite '-1'\n")
                    novos_dados.append(input("Digite o novo nome do tipo: "))
                    novos_dados.append(input("Digite o novo fator: "))

                    for i, dado in enumerate(novos_dados, start=0):
                        if dado != "-1":
                            disc_atualizar.update({campos[i]: novos_dados[i]})

                    sql, atualizacoes = tipo_ingresso.atualizar_tipo(disc_atualizar, id_atualizar)
                    mycursor.execute(sql, atualizacoes)
                    mydb.commit()

                case "4": # Excluir Tipo de Ingresso
                    id_excluir = [input("Digite o id do tipo: ")]
                    sql = tipo_ingresso.deletar_tipo()
                    mycursor.execute(sql, id_excluir)
                    mydb.commit()

                case "0":
                    continue
        case "7":
            mycursor.execute("""SELECT cliente.nome, cliente.cpf, evento.nome, COUNT(ingresso.id_ingresso) AS Total_Comprados
                                FROM cliente
                                INNER JOIN ingresso ON cliente.id_cliente = ingresso.id_cliente
                                LEFT JOIN evento ON ingresso.id_evento = evento.id_evento
                                GROUP BY cliente.cpf, evento.id_evento""")
            for row in mycursor.fetchall():
                print(f"Nome: {row[0]}, CPF: {row[1]}, Evento: {row[2]}, Total Comprados: {row[3]}")
        case "0":
            break

finish(mycursor, mydb)