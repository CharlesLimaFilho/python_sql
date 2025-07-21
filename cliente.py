from datetime import date
import re

class Cliente:


    def verificar_cpf(self, cpf: str):
        cpf = re.sub(r'\D', '', cpf)
        if len(cpf) != 11:
            return 1
        digitos = [int(d) for d in cpf]

        soma = 0
        for i in range(9):
            soma += digitos[i] * (10 - i)
        primeiro_digito = (soma * 10) % 11

        if primeiro_digito == 10:
            primeiro_digito = 0

        soma = 0
        for i in range(10):
            if i == 9:
                soma += primeiro_digito * 2
            else:
                soma += digitos[i] * (11 - i)
        segundo_digito = (soma * 10) % 11

        if primeiro_digito == digitos[9] and segundo_digito == digitos[10]:
            return cpf
        else:
            return 2

    def inserir_cliente(self, nome, cpf, data_nascimento, email, id_endereco, celular):
        cpf = self.verificar_cpf(cpf)
        if cpf == 1:
            return "Cpf de tamanho incorreto", 1
        elif cpf == 2:
            return "Cpf invalido", 2

        sql = "INSERT INTO cliente (nome, cpf, data_nascimento, email, id_endereco, celular) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (nome, cpf, data_nascimento, email, id_endereco, celular)

        return sql, val

    @staticmethod
    def consultar_cliente():
        sql = "SELECT * FROM cliente WHERE id_cliente = %s"
        return sql

    @staticmethod
    def consultar_todos_clientes():
        sql = "SELECT * FROM cliente"
        return sql

    @staticmethod
    def atualizar_cliente(novas_informacoes, id_atualizar):
        lista_novas_informacoes = []
        lista_campos = []

        for campo, nova_informacao in novas_informacoes.items():
            lista_campos.append(f"{campo} = %s")
            lista_novas_informacoes.append(nova_informacao)

        sql = f"UPDATE cliente SET {', '.join(lista_campos)} WHERE id_cliente = %s"
        lista_novas_informacoes.append(id_atualizar)

        return sql, lista_novas_informacoes

    @staticmethod
    def deletar_cliente():
        sql = "DELETE FROM cliente WHERE id_cliente = %s"
        return sql