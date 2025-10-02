import os
import sqlite3
from .produtos import Produto

NOME_BD = "loja.db"
DIRETORIO_ATUAL = os.path.dirname(os.path.abspath(__file__))
CAMINHO_DB = os.path.join(DIRETORIO_ATUAL, "..", NOME_BD)

def _obter_conexao():
    return sqlite3.connect(CAMINHO_DB)

def criar_tabela_produtos():
    with _obter_conexao() as conexao:
        cursor = conexao.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            preco REAL NOT NULL,
            quantidade INTEGER NOT NULL               
        )
        """)

        conexao.commit()

def adicionar_produto(produto: Produto):
    with  _obter_conexao() as conexao:
        cursor = conexao.cursor()

        cursor.execute(
            "INSERT INTO produtos (nome, preco, quantidade) VALUES (?, ?, ?)",
            (produto.nome, produto.preco, produto.quantidade)
        )

        conexao.commit()
        produto.id = cursor.lastrowid

def listar_produtos():
    with  _obter_conexao() as conexao:
        cursor = conexao.cursor()

        cursor.execute("SELECT id, nome, preco, quantidade FROM produtos")
        linhas = cursor.fetchall()

        produtos = []
        for linha in linhas:
            produto = Produto(id = linha[0], nome = linha[1], preco = linha[2], quantidade = linha[3])
            produtos.append(produto)

        return produtos

def atualizar_produto(id, nome, preco, quantidade):
    with _obter_conexao() as conexao:
        cursor = conexao.cursor()

        cursor.execute(
            "UPDATE produtos SET nome = ?, preco = ?, quantidade = ? WHERE id = ?",
            (nome, preco, quantidade, id)
        )
        conexao.commit()

def deletar_produto(id):
    with _obter_conexao() as conexao:
        cursor = conexao.cursor()

        cursor.execute("DELETE FROM produtos WHERE id = ?", (id,))
        conexao.commit()