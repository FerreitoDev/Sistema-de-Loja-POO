from loja import db
from loja.repositorios.usuarios_dao import UsuarioDAO
from loja.autenticador import Autenticador


# if __name__ == "__main__":
#     db.criar_tabela_produtos()

#     novo_produto = produtos.Produto("Sabão em pó", 22.00, 15)
#     produtos_dao.adicionar_produto(novo_produto)

#     todos_produtos = produtos_dao.listar_produtos()
#     for c in produtos_dao.listar_produtos():
#         print(c)

#     produtos_dao.atualizar_produto(1, "Nescao", 14, 54)
#     for c in produtos_dao.listar_produtos():
#         print(c)

#     produtos_dao.deletar_produto(2)
#     for c in produtos_dao.listar_produtos():
#         print(c)

# db.criar_tabela_adm()

# try:
#     adm = Autenticador.cadastro_adm("Administrador", "administrador@loja.com", "contateste123@")
#     UsuarioDAO.adicionar_adm(adm)
# except ValueError as e:
#     print(e)