from loja import db, produtos


if __name__ == "__main__":
    db.criar_tabela_produtos()

    # novo_produto = produtos.Produto("Sabão em pó", 22.00, 15)
    # db.adicionar_produto(novo_produto)

    # todos_produtos = db.listar_produtos()
    # for c in db.listar_produtos():
    #     print(c)

    # db.atualizar_produto(1, "Nescao", 14, 54)
    for c in db.listar_produtos():
        print(c)

    db.deletar_produto(2)
    for c in db.listar_produtos():
        print(c)
