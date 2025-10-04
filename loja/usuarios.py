from loja.utils import validar_texto_vazio
from loja.repositorios.produtos_dao import ProdutosDAO
class Usuario:

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, texto):
        if not validar_texto_vazio(texto):
            raise ValueError ("Nome não pode ser vazio")
        self._nome = texto.strip().title()

    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, texto):
        if not validar_texto_vazio(texto):
            raise ValueError ("Email não pode ser vazio")
        self._email = texto.lower().strip()

    @property
    def senha(self):
        return self._senha
    
    @senha.setter
    def senha(self, senha_hash):
        if not validar_texto_vazio(senha_hash):
            raise ValueError ("Senha não pode ser vazia")
        self._senha = senha_hash

class Cliente(Usuario):
    def __init__(self, nome, email, senha, id = None):
        super().__init__(nome, email, senha)
        self.id = id
        

class Adm(Usuario):
    def __init__(self, nome, email, senha, id = None):
        super().__init__(nome, email, senha)
        self.id = id

    @staticmethod
    def cadastrar_produto(produto):
        ProdutosDAO.adicionar_produto(produto)

    @staticmethod
    def alterar_produto(id, nome, preco, quantidade_estoque):
        ProdutosDAO.atualizar_produto(id, nome, preco, quantidade_estoque)

    @staticmethod
    def excluir_produto(id):
        ProdutosDAO.deletar_produto(id)

