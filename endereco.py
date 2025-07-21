class Endereco:

    @staticmethod
    def inserir_endereco(rua, numero, cidade, estado):
        sql = "INSERT INTO endereco (rua, numero, cidade, estado) VALUES (%s, %s, %s, %s)"
        val = (rua, numero, cidade, estado)

        return sql, val

    @staticmethod
    def consultar_endereco():
        sql = "SELECT * FROM endereco WHERE id_endereco = %s"
        return sql

    @staticmethod
    def consultar_todos_enderecos():
        sql = "SELECT * FROM endereco"
        return sql

    @staticmethod
    def atualizar_endereco(novas_informacoes, id_atualizar):
        lista_novas_informacoes = []
        lista_campos = []

        for campo, nova_informacao in novas_informacoes.items():
            lista_campos.append(f"{campo} = %s")
            lista_novas_informacoes.append(nova_informacao)

        sql = f"UPDATE endereco SET {', '.join(lista_campos)} WHERE id_endereco = %s"
        lista_novas_informacoes.append(id_atualizar)

        return sql, lista_novas_informacoes

    @staticmethod
    def deletar_endereco():
        sql = "DELETE FROM endereco WHERE id_endereco = %s"
        return sql