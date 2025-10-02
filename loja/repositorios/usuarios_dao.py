from loja.db import obter_conexao
from loja.usuarios import Cliente, Adm

TABELA_CLIENTE = "cliente"
TABELA_ADM = "adm"

def _adicionar_usuario(usuario, tabela):
    with obter_conexao() as conexao:
        cursor = conexao.cursor()

        cursor.execute(f"SELECT 1 FROM {tabela} WHERE email = ?", (usuario.email,))
        if cursor.fetchone():
            raise EmailJaCadastrado ("Erro: Email já cadastrado.")

        cursor.execute(
            f"INSERT INTO {tabela} (nome, email, senha) VALUES (?, ?, ?)",
            (usuario.nome, usuario.email, usuario.senha)
        )

        conexao.commit()
        usuario.id = cursor.lastrowid

class EmailJaCadastrado(Exception):
    pass

def adicionar_adm(adm : Adm):
    _adicionar_usuario(adm, TABELA_ADM)

def adicionar_cliente(cliente : Cliente):
    _adicionar_usuario(cliente, TABELA_CLIENTE)