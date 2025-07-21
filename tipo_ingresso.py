class TipoIngresso:

    @staticmethod
    def inserir_tipo(nome, fator):
        sql = "INSERT INTO tipo_ingresso (nome, fator) VALUES (%s, %s)"
        val = (nome, fator)

        return sql, val

    @staticmethod
    def consultar_tipo():
        sql = "SELECT * FROM tipo_ingresso WHERE id_tipo = %s"
        return sql

    @staticmethod
    def consultar_todos_tipos():
        sql = "SELECT * FROM tipo_ingresso"
        return sql

    @staticmethod
    def atualizar_tipo(novas_informacoes, id_atualizar):
        lista_novas_informacoes = []
        lista_campos = []

        for campo, nova_informacao in novas_informacoes.items():
            lista_campos.append(f"{campo} = %s")
            lista_novas_informacoes.append(nova_informacao)

        sql = f"UPDATE endereco SET {', '.join(lista_campos)} WHERE id_endereco = %s"
        lista_novas_informacoes.append(id_atualizar)

        return sql, lista_novas_informacoes

    @staticmethod
    def deletar_tipo():
        sql = "DELETE FROM tipo_ingresso WHERE id_tipo = %s"
        return sql