from loja.db import obter_conexao
from loja.usuarios import Cliente, Adm

def _adicionar_usuario(usuario, tabela):
    with obter_conexao() as conexao:
        cursor = conexao.cursor()

        cursor.execute(
            f"INSERT INTO {tabela} (nome, email, senha) VALUES (?, ?, ?)",
            (usuario.nome, usuario.email, usuario.senha)
        )

    conexao.commit()
    usuario.id = cursor.lastrowid

def adicionar_adm(adm : Adm):
    _adicionar_usuario(adm, "adm")

def adicionar_cliente(cliente : Cliente):
    _adicionar_usuario(cliente, "cliente")