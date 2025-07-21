class Ingresso:

    @staticmethod
    def inserir_ingresso(id_evento, id_cliente, id_setor, id_tipo, preco):
        sql = "INSERT INTO ingresso (id_evento, id_cliente, id_setor, id_tipo, preco_final) VALUES (%s, %s, %s, %s, %s)"
        val = (id_evento, id_cliente, id_setor, id_tipo, preco)

        return sql, val

    @staticmethod
    def consultar_ingresso():
        sql = "SELECT * FROM ingresso WHERE id_ingresso = %s"
        return sql

    @staticmethod
    def consultar_todos_ingressos():
        sql = "SELECT * FROM ingresso"
        return sql

    @staticmethod
    def atualizar_ingresso(novas_informacoes, id_atualizar):
        lista_novas_informacoes = []
        lista_campos = []

        for campo, nova_informacao in novas_informacoes.items():
            lista_campos.append(f"{campo} = %s")
            lista_novas_informacoes.append(nova_informacao)

        sql = f"UPDATE endereco SET {', '.join(lista_campos)} WHERE id_endereco = %s"
        lista_novas_informacoes.append(id_atualizar)

        return sql, lista_novas_informacoes

    @staticmethod
    def deletar_ingresso():
        sql = "DELETE FROM ingresso WHERE id_ingresso = %s"
        return sql