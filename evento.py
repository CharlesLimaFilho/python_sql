from datetime import date

class Evento:

    @staticmethod
    def inserir_evento(nome, data_evento, id_endereco, limite):
        sql = "INSERT INTO evento (nome, data, id_endereco, limite_ingressos_por_cpf) VALUES (%s, %s, %s, %s)"
        val = (nome, data_evento, id_endereco, limite)

        return sql, val

    @staticmethod
    def consultar_evento():
        sql = "SELECT * FROM evento WHERE id_evento = %s"
        return sql

    @staticmethod
    def consultar_todos_eventos():
        sql = "SELECT * FROM evento"
        return sql

    @staticmethod
    def atualizar_evento(novas_informacoes, id_atualizar):
        lista_novas_informacoes = []
        lista_campos = []

        for campo, nova_informacao in novas_informacoes.items():
            lista_campos.append(f"{campo} = %s")
            lista_novas_informacoes.append(nova_informacao)

        sql = f"UPDATE endereco SET {', '.join(lista_campos)} WHERE id_endereco = %s"
        lista_novas_informacoes.append(id_atualizar)

        return sql, lista_novas_informacoes

    @staticmethod
    def deletar_evento():
        sql = "DELETE FROM evento WHERE id_evento = %s"
        return sql