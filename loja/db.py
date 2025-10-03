import os
import sqlite3
from .produtos import Produto

NOME_BD = "loja.db"
DIRETORIO_ATUAL = os.path.dirname(os.path.abspath(__file__))
CAMINHO_DB = os.path.join(DIRETORIO_ATUAL, "..", NOME_BD)

class Database:
    @staticmethod
    def obter_conexao():
        return sqlite3.connect(CAMINHO_DB)

def obter_conexao():
    return Database.obter_conexao()

def criar_tabela_produtos():
    with Database.obter_conexao() as conexao:
        cursor = conexao.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            preco REAL NOT NULL,
            quantidade_estoque INTEGER NOT NULL               
        )
        """)

        conexao.commit()

def criar_tabela_adm():
    with Database.obter_conexao() as conexao:
        cursor = conexao.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS adm (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            senha TEXT NOT NULL      
        )
        """)

        conexao.commit()

def criar_tabela_clientes():
    with Database.obter_conexao() as conexao:
        cursor = conexao.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            senha TEXT NOT NULL      
        )
        """)

        conexao.commit()