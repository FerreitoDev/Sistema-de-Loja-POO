from loja.db import obter_conexao
from loja.produtos import Produto

def adicionar_produto(produto: Produto):
    with  obter_conexao() as conexao:
        cursor = conexao.cursor()

        cursor.execute(
            "INSERT INTO produtos (nome, preco, quantidade) VALUES (?, ?, ?)",
            (produto.nome, produto.preco, produto.quantidade)
        )

        conexao.commit()
        produto.id = cursor.lastrowid

def listar_produtos():
    with  obter_conexao() as conexao:
        cursor = conexao.cursor()

        cursor.execute("SELECT id, nome, preco, quantidade FROM produtos")
        linhas = cursor.fetchall()

        produtos = []
        for linha in linhas:
            produto = Produto(id = linha[0], nome = linha[1], preco = linha[2], quantidade = linha[3])
            produtos.append(produto)

        return produtos

def atualizar_produto(id, nome, preco, quantidade):
    with obter_conexao() as conexao:
        cursor = conexao.cursor()

        cursor.execute(
            "UPDATE produtos SET nome = ?, preco = ?, quantidade = ? WHERE id = ?",
            (nome, preco, quantidade, id)
        )
        conexao.commit()

def deletar_produto(id):
    with obter_conexao() as conexao:
        cursor = conexao.cursor()

        cursor.execute("DELETE FROM produtos WHERE id = ?", (id,))
        conexao.commit()