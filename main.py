from loja.db import DataBase
from loja.autenticador import Autenticador
from loja.usuarios import Adm, Cliente
from loja.repositorios.produtos_dao import ProdutosDAO
from loja import menus
from loja import utils
from loja.produtos import Produto

DataBase.criar_tabelas()
def main():
    login = False
    while True:
        if not login:
            logar = cadastrar = False
            menus.menu_login_cadastro()
            opcao, sucesso = utils.obter_opcao()

            if not sucesso:
                continue

            match opcao:
                case 1:
                    logar = True
                case 2:
                    cadastrar = True
                case 3:
                    exit()
                case _:
                    print("\nErro: Opção inválida")

            if logar:
                while True:
                    print("\n=== Login ===")
                    try:
                        print("Para voltar digite '0' no campo Email.")
                        email = input("Email: ")
                        print(email)
                        if email.strip() == "0":
                            break
                        Autenticador.validar_email(email)
                        senha = input("Senha: ")
                        print(senha)
                        usuario_login = Autenticador.logar(email, senha)
                        if usuario_login:
                            login = True
                            print("Usuario logado com sucesso.")
                            break
                    except (Autenticador.ErroLogin, ValueError) as e:
                        print("Erro:", e)
                        continue
        if login and isinstance(usuario_login, Adm):
            while True:
                menus.menu_adm()
                opcao, sucesso = utils.obter_opcao()

                if not sucesso:
                    continue

                match opcao:
                    case 1:
                        print("\n=== Produtos ===")
                        produtos = ProdutosDAO.listar_produtos()
                        for produto in produtos:
                            print(produto)
                    case 2:
                        print("\n=== Cadastrar Produto ===")
                        cadastro_produto = False
                        try:
                            nome_produto = input("Nome do Produto: ")
                            preco_produto = float(input("Valor do Produto: R$"))
                            quantidade_produto = int(input("Quantidade do Produto: "))
                            if utils.validar_texto_vazio(nome_produto) and utils.validar_valor(preco_produto) and utils.validar_valor(quantidade_produto):
                                cadastro_produto = True
                            if cadastro_produto:
                                usuario_login.cadastrar_produto(Produto(nome_produto, preco_produto, quantidade_produto))
                                print("Produto")
                        except ValueError as e:
                            print("Erro:", e)
                    case 3:
                        
                        while True:
                            print("\n=== Atualizar Produtos ===")
                            try:
                                print("Para voltar digite '0'.")
                                entrada = input("Informe o ID do produto: ")

                                if entrada == '0':
                                    break

                                id_produto = utils.obter_id(int(entrada))
                                produto_atualizar = ProdutosDAO.pegar_produto(id_produto)

                            except ValueError as e:
                                print("\nErro:", e)
                                continue
                            menus.menu_atualizar_produto()
                            opcao, sucesso = utils.obter_opcao()

                            if not sucesso:
                                continue

                            match opcao:
                                case 1:
                                    novo_nome_produto = input("Digite o novo nome do produto: ")

                                    try:
                                        if utils.validar_texto_vazio(novo_nome_produto):
                                            produto_atualizar.nome = novo_nome_produto
                                            ProdutosDAO.atualizar_produto(produto_atualizar)
                                            print(f"\nNome do produto atualizado para: {novo_nome_produto}.")
                                            break

                                    except ValueError as e:
                                        print("\nErro:", e)
                                        continue
                                case 2:
                                    novo_preco_produto = float(input("Digite o novo preço do produto: R$"))

                                    try:
                                        if utils.validar_valor(novo_preco_produto):
                                            produto_atualizar.preco = novo_preco_produto
                                            ProdutosDAO.atualizar_produto(produto_atualizar)
                                            print(f"\nPreço do produto atualizado para: R${novo_preco_produto}.")
                                            break

                                    except ValueError as e:
                                        print("\nErro:", e)
                                        continue
                                case 3:
                                    nova_quantidade_produto = int(input("Digite a nova quantidade do produto: "))
                                    
                                    try:
                                        if utils.validar_valor(nova_quantidade_produto):
                                            produto_atualizar.quantidade_estoque = nova_quantidade_produto
                                            ProdutosDAO.atualizar_produto(produto_atualizar)
                                            print(f"\nQuantidade atualizada para: {nova_quantidade_produto}.")
                                            break

                                    except ValueError as e:
                                        print("\nErro:", e)
                                        continue
                                case 4:
                                    break

                    case 4:
                        
                        while True:
                            print("\n=== Deletar Produto ===")
                            try:
                                print("Para voltar digite '0'.")
                                entrada = input("Informe o ID do produto: ")

                                if entrada == '0':
                                    break

                                id_produto = utils.obter_id(int(entrada))
                                produto_deletar = ProdutosDAO.pegar_produto(id_produto)

                            except ValueError as e:
                                print("\nErro:", e)
                                continue
                            print("\n" + 50 * "=")
                            print(produto_deletar)
                            print(50* "=")
                            confirmacao = input("\nTem certeza que deseja deletar esse produto? (sim/não): ")
                            
                            if confirmacao.strip().upper() == "SIM":
                                ProdutosDAO.deletar_produto(id_produto)
                                print("\nProduto deletado com sucesso.")
                                break

                            elif confirmacao.strip().upper() == "NÃO" or confirmacao.strip().upper() == "NAO":
                                print("\nVoltando a seleção do produto...")
                                continue

                            else:
                                print("Opção inválida. Tente novamente.")
                                continue
                    case 5:
                        pass
                    case 6:
                        pass
                    case 7:
                        pass
                    case 8:
                        login = False
                        break       




if __name__ == "__main__":
    main()
 







# DataBase.criar_tabela_adm()
# try:
#     adm = Autenticador.cadastro_adm("Administrador", "administrador@loja.com", "contateste123@")
#     UsuarioDAO.adicionar_adm(adm)
# except ValueError as e:
#     print(e)