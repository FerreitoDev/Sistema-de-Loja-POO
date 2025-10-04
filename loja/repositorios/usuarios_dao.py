from loja.db import DataBase
from loja.usuarios import Cliente, Adm

class UsuarioDAO:

    TABELA_CLIENTE = "clientes"
    TABELA_ADM = "adm"

    class EmailJaCadastrado(Exception):
        pass


    @staticmethod
    def _adicionar_usuario(usuario, tabela):
        with DataBase.obter_conexao() as conexao:
            cursor = conexao.cursor()

            cursor.execute(f"SELECT 1 FROM {tabela} WHERE email = ?", (usuario.email,))
            if cursor.fetchone():
                raise UsuarioDAO.EmailJaCadastrado ("Erro: Email já cadastrado.")

            cursor.execute(
                f"INSERT INTO {tabela} (nome, email, senha) VALUES (?, ?, ?)",
                (usuario.nome, usuario.email, usuario.senha)
            )

            conexao.commit()
            usuario.id = cursor.lastrowid

    @classmethod
    def adicionar_adm(cls, adm : Adm):
        cls._adicionar_usuario(adm, cls.TABELA_ADM)

    @classmethod
    def adicionar_cliente(cls, cliente : Cliente):
        cls._adicionar_usuario(cliente, cls.TABELA_CLIENTE)

    @staticmethod
    def procurar_usuarios(email):
        with DataBase.obter_conexao() as conexao:
            cursor = conexao.cursor()

            cursor.execute("""
                SELECT 'adm' as tipo, nome, email, senha, id FROM adm WHERE email = ?
                UNION ALL
                SELECT 'cliente' as tipo, nome, email, senha, id FROM clientes WHERE email = ?
                """, (email, email))
            
            usuario = cursor.fetchone()

            if usuario:
                tipo, *dados = usuario
                if tipo == "adm":
                    return Adm(*dados)
                else:
                    return Cliente(*dados)
            return None