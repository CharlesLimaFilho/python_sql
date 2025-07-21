class Setor:

    @staticmethod
    def inserir_setor(nome, valor):
        sql = "INSERT INTO setor (nome, valor_base) VALUES (%s, %s)"
        val = (nome, valor)

        return sql, val

    @staticmethod
    def consultar_setor():
        sql = "SELECT * FROM setor WHERE id_setor = %s"
        return sql

    @staticmethod
    def consultar_todos_setores():
        sql = "SELECT * FROM setor"
        return sql

    @staticmethod
    def atualizar_setor(novas_informacoes, id_atualizar):
        lista_novas_informacoes = []
        lista_campos = []

        for campo, nova_informacao in novas_informacoes.items():
            lista_campos.append(f"{campo} = %s")
            lista_novas_informacoes.append(nova_informacao)

        sql = f"UPDATE endereco SET {', '.join(lista_campos)} WHERE id_endereco = %s"
        lista_novas_informacoes.append(id_atualizar)

        return sql, lista_novas_informacoes

    @staticmethod
    def deletar_setor():
        sql = "DELETE FROM setor WHERE id_setor = %s"
        return sql
