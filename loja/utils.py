def validar_texto_vazio(texto):
    if not texto.strip():
        raise ValueError("Campo não pode ser vazio")
    return True


    


