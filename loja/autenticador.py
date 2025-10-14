import re
from loja.usuarios import Adm, Cliente
from bcrypt import hashpw, gensalt, checkpw
from loja.utils import validar_texto_vazio
from loja.repositorios.usuarios_dao import UsuarioDAO

PADRAO = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
MIN_CARACTERES_SENHA = 8

class Autenticador:

    class ErroLogin(Exception):
        pass


    @staticmethod
    def hashear_senha(senha_pura):
        salt = gensalt()

        senha_hash = hashpw(senha_pura.encode('utf-8'), salt)

        return senha_hash

    @staticmethod
    def verificar_senha_login(senha_pura_digitada, senha_hash_do_bd):
        senha_digitada_bytes = senha_pura_digitada.encode('utf-8')
        return checkpw(senha_digitada_bytes, senha_hash_do_bd)

    @staticmethod
    def validar_email(email):
        validar_texto_vazio(email)
        if not re.match(PADRAO, email):
            raise ValueError ("Email inválido.")
    
    @staticmethod    
    def validar_nome(nome):
        nome_verificacao = nome.replace(" ", "")
        if not nome_verificacao.isalpha():
            raise ValueError ("Nome não pode conter números ou símbolos")
    
    @staticmethod
    def validar_senha(senha):
        tem_numero = tem_letra = False
        for char in senha:
            if char.isdigit():
                tem_numero = True
            elif char.isalpha():
                tem_letra = True

        if len(senha) < MIN_CARACTERES_SENHA:
            raise ValueError ("Senha deve ter no mínimo 8 caracteres")
        
        elif not tem_numero or not tem_letra:
            raise ValueError ("Senha deve conter letras e números")

    @classmethod
    def cadastrar_adm(cls, nome, email, senha):
        cls.validar_nome(nome)
        cls.validar_email(email)
        cls.validar_senha(senha)
        senha_hash = cls.hashear_senha(senha)
        adm = Adm(nome, email, senha_hash)
        UsuarioDAO.adicionar_adm(adm)
    
    @classmethod
    def logar(cls, email, senha):
        usuario = UsuarioDAO.procurar_usuarios(email)

        if not usuario:
            raise cls.ErroLogin("Erro: Usuario não encontrado.")
        
        if cls.verificar_senha_login(senha, usuario.senha):
                return usuario
        
        raise cls.ErroLogin("Erro: Email ou senha incorretos.")

    @classmethod
    def cadastrar_cliente(cls, nome, email, senha):
        cls.validar_nome(nome)
        cls.validar_email(email)
        cls.validar_senha(senha)

        senha_hash = cls.hashear_senha(senha)
        cliente = Cliente(nome, email, senha_hash)
        UsuarioDAO.adicionar_cliente(cliente)