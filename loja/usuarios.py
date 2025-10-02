from utils import validar_texto_vazio
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
    def __init__(self, nome, email, senha):
        super().__init__(nome, email, senha)
        

class Adm(Usuario):
    def __init__(self, nome, email, senha):
        super().__init__(nome, email, senha)

