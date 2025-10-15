from loja import utils
from loja.db import DataBase
from loja.interface import menus
from loja.usuarios import Adm, Cliente
from loja.interface.interfaces import Interface
from loja.repositorios.pedidos_dao import PedidosDAO

DataBase.criar_tabelas()

#Criar conta adm
# try:
#     adm = Autenticador.cadastrar_adm("Administrador", "administrador@loja.com", "contateste123@")
#     UsuarioDAO.adicionar_adm(adm)
# except ValueError as e:
#     print(e)

def main():
    login = False
    while True:
        while True:
            if not login:
                menus.menu_login_cadastro()
                opcao, sucesso = utils.obter_opcao()

                if not sucesso:
                    continue

                match opcao:
                    case 1:
                        login, usuario_login = Interface.logando()
                        
                    case 2:
                        Interface.cadastrando()

                    case 3:
                        exit()
                    case _:
                        print("\nErro: Opção inválida")

            break

        if login and isinstance(usuario_login, Adm):
            while True:
                menus.menu_adm()
                opcao, sucesso = utils.obter_opcao()

                if not sucesso:
                    continue

                match opcao:
                    case 1:
                        Interface.exibir_produtos_usuario()
                    case 2:
                        Interface.cadastrando_produto(usuario_login)
                    case 3:
                        Interface.atualizando_produto(usuario_login)
                    case 4:
                        Interface.exibir_pedidos()
                    case 5:
                        Interface.gerar_relatorios()
                    case 6:
                        Interface.cadastrando_adm()
                    case 7:
                        login = False
                        break 
                    case _:
                        print("\nErro: Opção inválida.")         
        if login and isinstance(usuario_login, Cliente):
            while True:
                carrinho = PedidosDAO.buscar_cliente_pedido_aberto(usuario_login.id)
                menus.menu_cliente()
                opcao, sucesso = utils.obter_opcao()

                if not sucesso:
                    continue

                match opcao:
                    case 1:
                        Interface.exibir_produtos_usuario()
                    case 2:                               
                        Interface.adicionando_produto_carrinho(usuario_login, carrinho)
                    case 3:
                        Interface.exibir_carrinho(carrinho)
                    case 4:
                        Interface.exibir_historico(usuario_login.id)
                    case 5:
                        login = False
                        break
                        
                    case _:
                        print("\nErro: Opção inválida.")     


if __name__ == "__main__":
    main()
 
