from bcrypt import hashpw, gensalt, checkpw

def hashear_senha(senha_pura):
    salt = gensalt()

    senha_hash = hashpw(senha_pura.encode('utf-8'), salt)

    return senha_hash

def verificar_senha(senha_pura_digitada, senha_hash_do_bd):
    senha_digitada_bytes = senha_pura_digitada.encode('utf-8')
    return checkpw(senha_digitada_bytes, senha_hash_do_bd)


senha = "1233453452424"
nova_senha = hashear_senha(senha)
if verificar_senha(senha, nova_senha):
    print("Certinho")