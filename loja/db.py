import os
import sqlite3

NOME_BD = "loja.db"
DIRETORIO_ATUAL = os.path.dirname(os.path.abspath(__file__))
CAMINHO_DB = os.path.join(DIRETORIO_ATUAL, "..", NOME_BD)

class DataBase:
    @staticmethod
    def obter_conexao():
        return sqlite3.connect(CAMINHO_DB)

    @classmethod
    def criar_tabelas(cls):
        with cls.obter_conexao() as conexao:
            cursor = conexao.cursor()

            cursor.execute("""
            CREATE TABLE IF NOT EXISTS produtos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                preco REAL NOT NULL,
                quantidade_estoque INTEGER NOT NULL               
            )
            """)

            cursor.execute("""
            CREATE TABLE IF NOT EXISTS adm (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                senha TEXT NOT NULL      
            )
            """)

            cursor.execute("""
            CREATE TABLE IF NOT EXISTS clientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                senha TEXT NOT NULL      
            )
            """)

            conexao.commit()
