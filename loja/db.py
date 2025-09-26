import sqlite3

conexao = sqlite3.connect("lojabd.db")
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXIST produtos (
    id INTEGER PRIMARY KAY AUTOINCREMENT,
    nome TEXT NOT NULL,
    preco REAL NOT NULL,
    quantidade INTEGER NOT NULL               
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXIST clientes (
    id INTEGER PRIMARY KAY AUTOINCREMENT,
    nome TEXT NOT NULL,
    preco REAL NOT NULL,
    quantidade INTEGER NOT NULL               
)
""")