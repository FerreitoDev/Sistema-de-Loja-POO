import re

PADRAO = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
MIN_CARACTERES_SENHA = 8

def validar_texto_vazio(texto):
    if not texto.strip():
        raise ValueError("Campo não pode ser vazio")
    return True

def validar_email(email):
    validar_texto_vazio(email)
    if not re.match(PADRAO, email):
        raise ValueError ("Email inválido.")
    return True
    
def validar_nome(nome):
    nome_verificacao = nome.replace(" ", "")
    if not nome_verificacao.isalpha():
        raise ValueError ("Nome não pode conter números ou símbolos")
    print("Teste")
    return True

def validar_senha(senha):
    tem_numero = any(char.isdigit() for char in senha)
    tem_letra = any(char.isalpha() for char in senha)

    if len(senha) < MIN_CARACTERES_SENHA:
        raise ValueError ("Senha deve ter no mínimo 8 caracteres")
    elif not tem_numero or not tem_letra:
        raise ValueError ("Senha deve conter letras e números")
    print("validado")
    

