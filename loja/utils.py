from numbers import Number

def validar_texto_vazio(texto):
    if not texto.strip():
        raise ValueError("Campo não pode ser vazio")
    return True

def obter_opcao():
    try:
        return int(input("Escolha uma opção: ")), True
    except ValueError:
        print("\nErro: Valor inválido")
        return None, False
    
def validar_valor(valor):
    if not isinstance(valor, Number):
        raise ValueError("Valor tem que ser um número.")
    if valor <= 0:
        raise ValueError("Valor tem que ser maior ou igual 0")
    return True

def validar_id(id):
    if not isinstance(id, int):
        raise ValueError("Id deve ser um número inteiro")
    if id <= 0:
        raise ValueError("Id inválido")
    return True

