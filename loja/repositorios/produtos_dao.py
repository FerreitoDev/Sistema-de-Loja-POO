from loja.db import DataBase
from loja.produtos import Produto

class ProdutosDAO:

    @staticmethod
    def adicionar_produto(produto: Produto):
        with  DataBase.obter_conexao() as conexao:
            cursor = conexao.cursor()

            cursor.execute(
                "INSERT INTO produtos (nome, preco, quantidade_estoque) VALUES (?, ?, ?)",
                (produto.nome, produto.preco, produto.quantidade_estoque)
            )

            conexao.commit()
            produto.id = cursor.lastrowid

    @staticmethod
    def listar_produtos():
        with  DataBase.obter_conexao() as conexao:
            cursor = conexao.cursor()

            cursor.execute("SELECT id, nome, preco, quantidade_estoque FROM produtos")
            linhas = cursor.fetchall()

            if not linhas:
                raise ValueError("Nenhum produto foi encontrado")

            produtos = []
            for linha in linhas:
                produto = Produto(id = linha[0], nome = linha[1], preco = linha[2], quantidade_estoque = linha[3])
                produtos.append(produto)

            return produtos
        
    @staticmethod
    def listar_produtos_cliente():
        with  DataBase.obter_conexao() as conexao:
            cursor = conexao.cursor()

            cursor.execute("SELECT id, nome, preco, quantidade_estoque FROM produtos")
            linhas = cursor.fetchall()

            if not linhas:
                raise ValueError("Nenhum produto foi encontrado")

            produtos = []
            for linha in linhas:
                produto = Produto(id = linha[0], nome = linha[1], preco = linha[2], quantidade_estoque = linha[3])
                produtos.append(produto)

            return produtos

    @staticmethod
    def atualizar_produto(produto: Produto):
        with DataBase.obter_conexao() as conexao:
            cursor = conexao.cursor()

            cursor.execute(
                "UPDATE produtos SET nome = ?, preco = ?, quantidade_estoque = ? WHERE id = ?",
                (produto.nome, produto.preco, produto.quantidade_estoque, produto.id)
            )

            if cursor.rowcount == 0:
                raise ValueError("Produto não encontrado")
            conexao.commit()

    def pegar_produto(id):
        with DataBase.obter_conexao() as conexao:
            cursor = conexao.cursor()

            cursor.execute("SELECT nome, preco, quantidade_estoque, id FROM produtos WHERE id = ?",(id,))
            produto_db = cursor.fetchone()
            
            if not produto_db:
                raise ValueError("Produto não encontrado")
            
            produto = Produto(nome = produto_db[0], preco = produto_db[1], quantidade_estoque = produto_db[2], id = produto_db[3])

            return produto
            

