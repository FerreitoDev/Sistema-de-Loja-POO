from loja.db import obter_conexao
from loja.produtos import Produto

class ProdutosDAO:

    @staticmethod
    def adicionar_produto(produto: Produto):
        with  obter_conexao() as conexao:
            cursor = conexao.cursor()

            cursor.execute(
                "INSERT INTO produtos (nome, preco, quantidade_estoque) VALUES (?, ?, ?)",
                (produto.nome, produto.preco, produto.quantidade_estoque)
            )

            conexao.commit()
            produto.id = cursor.lastrowid

    @staticmethod
    def listar_produtos():
        with  obter_conexao() as conexao:
            cursor = conexao.cursor()

            cursor.execute("SELECT id, nome, preco, quantidade_estoque FROM produtos")
            linhas = cursor.fetchall()

            produtos = []
            for linha in linhas:
                produto = Produto(id = linha[0], nome = linha[1], preco = linha[2], quantidade_estoque = linha[3])
                produtos.append(produto)

            return produtos

    @staticmethod
    def atualizar_produto(id, nome, preco, quantidade_estoque):
        with obter_conexao() as conexao:
            cursor = conexao.cursor()

            cursor.execute(
                "UPDATE produtos SET nome = ?, preco = ?, quantidade_estoque = ? WHERE id = ?",
                (nome, preco, quantidade_estoque, id)
            )
            conexao.commit()

    @staticmethod
    def deletar_produto(id):
        with obter_conexao() as conexao:
            cursor = conexao.cursor()

            cursor.execute("DELETE FROM produtos WHERE id = ?", (id,))
            conexao.commit()