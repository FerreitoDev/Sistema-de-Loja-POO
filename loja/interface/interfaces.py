from loja.autenticador import Autenticador
from loja.repositorios.produtos_dao import ProdutosDAO
from loja.repositorios.pedidos_dao import PedidosDAO
from loja.relatorios import Relatorios
from loja import utils
from loja.produtos import Produto
from loja.interface import menus
from loja.pedidos import Pedido
from loja.pagamentos import CartaoCredito, Boleto, Pix

class Interface:
    @staticmethod
    def logando():

        while True:
            print("\n=== Login ===")
            print("Para voltar digite '0'.")
            try:
                email = input("Email: ")
                if email.strip() == "0":
                    return False, None
                
                senha = input("Senha: ")
                if senha.strip() == "0":
                    return False, None

                Autenticador.validar_email(email)
                usuario_login = Autenticador.logar(email, senha)
                if usuario_login:
                    print("\nUsuario logado com sucesso.")
                    return True, usuario_login
            except (Autenticador.ErroLogin, ValueError) as e:
                print("\nErro:", e)

    @staticmethod
    def cadastrando():
         while True:
            print("\n=== Cadastro ===")
            print("Para voltar digite '0'.")
            try:
                nome = input("Nome: ")
                if nome.strip() == '0':
                    return
                
                email = input("Email: ")
                if email.strip() == '0':
                    return
                
                senha = input("Senha: ")
                if senha.strip() == '0':
                   return
                Autenticador.cadastrar_cliente(nome, email, senha)
                print("\nCliente cadastrado com sucesso.")
                
                break
            except ValueError as e:
                print("\nErro:", e)

    @staticmethod
    def cadastrando_adm():
         while True:
            print("\n=== Cadastro ===")
            print("Para voltar digite '0'.")
            try:
                nome = input("Nome: ")
                if nome.strip() == '0':
                    return
                
                email = input("Email: ")
                if email.strip() == '0':
                    return
                
                senha = input("Senha: ")
                if senha.strip() == '0':
                   return
                Autenticador.cadastrar_adm(nome, email, senha)
                print("\nAdministrador cadastrado com sucesso.")
                
                break
            except ValueError as e:
                print("\nErro:", e)


    @staticmethod
    def exibir_produtos_usuario():
        print("\n=== Produtos ===")
        try: 
            produtos = ProdutosDAO.listar_produtos()
            for produto in produtos:
                print(produto)
        except ValueError as e:
            print("\nErro:", e)

    @staticmethod
    def cadastrando_produto(usuario_login):
        while True:
            print("\n=== Cadastrar Produto ===")
            cadastro_produto = False
            try:
                nome_produto = input("Nome do Produto: ")
                preco_produto = float(input("Valor do Produto: R$"))
                quantidade_produto = int(input("Quantidade do Produto: "))

                opcao = int(input("\nConfirmar cadastro:\n1. Sim\n0. Não\n"))
                match opcao:
                    case 1:
                        pass
                    case 0:
                        print("\nCadastro Cancelado")
                        return
                    case _:
                        print("\nOpção inválida")
                        continue
                    

                if utils.validar_texto_vazio(nome_produto) and utils.validar_valor(preco_produto) and utils.validar_valor(quantidade_produto):
                    cadastro_produto = True
                if cadastro_produto:
                    usuario_login.cadastrar_produto(Produto(nome_produto, preco_produto, quantidade_produto))
                    print("Produto cadastrado com sucesse.")
                    break
                
            except ValueError as e:
                print("\nErro:", e)
    
    @staticmethod
    def atualizando_produto(usuario_login):
        print("\n=== Atualizar Produtos ===")
        while True:
            try:
                print("Para voltar digite '0'.")
                id_produto = input("Informe o ID do produto: ")

                if id_produto == '0':
                    break
                
                id_produto = int(id_produto)
                if utils.validar_id(id_produto):
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
                            usuario_login.alterar_produto(produto_atualizar)
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
                            usuario_login.alterar_produto(produto_atualizar)
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
                            usuario_login.alterar_produto(produto_atualizar)
                            print(f"\nQuantidade atualizada para: {nova_quantidade_produto}.")
                            break

                    except ValueError as e:
                        print("\nErro:", e)
                        continue
                case 4:
                    break

                case _:
                    print("\nErro: Opção inválida")

    @staticmethod
    def adicionando_produto_carrinho(usuario_login, carrinho):
         while True:
            print("\n=== Adicionando produto ao carrinho ===")
            try:
                print("Para voltar digite '0'.")
                id_produto = input("Informe o ID do produto: ")

                if id_produto == '0':
                    break
                
                id_produto = int(id_produto)
                if utils.validar_id(id_produto):
                    produto_carrinho = ProdutosDAO.pegar_produto(id_produto)

                if not carrinho:
                    pedido = Pedido(usuario_login.id)
                    pedido.adicionar_item(produto_carrinho.id, produto_carrinho.preco)
                    PedidosDAO.criar_pedido(pedido)
                    print("\nProduto adicionado ao carrinho.")
                    break

                carrinho.adicionar_item(produto_carrinho.id, produto_carrinho.preco)
                PedidosDAO.atualizar_pedido(carrinho)
                print("\nProduto adicionado ao carrinho.")
                break

            except ValueError as e:
                print("\nErro:", e)

    @staticmethod
    def exibir_carrinho(carrinho):
        try:
            while True:
                if carrinho:
                    itens = PedidosDAO.visualizar_pedido(carrinho.id)
                else:
                    print("\nCarrinho vazio.")
                    return
                
                print("\n=== Carrinho ===")
                print("Itens:")
                for item in itens:
                    print(item)

                print(f"\nTotal: R${carrinho.total:.2f}")
                menus.menu_carrinho()
                opcao, sucesso = utils.obter_opcao()

                if not sucesso:
                    continue

                match opcao:
                    case 0:
                        return
                    case 1:
                        Interface.remover_produto_carrinho(carrinho)
                        continue
                    case 2:
                        Interface.pagando(carrinho)
                        return
        except ValueError as e:
            print("\nErro:", e)
    
    @staticmethod
    def exibir_historico(usuario_id):
        print("\n=== Histórico ===")
        pedidos = PedidosDAO.buscar_cliente_pedidos_fechado(usuario_id)
        if pedidos:
            for pedido in pedidos:
                print(f"\nPedido ID: {pedido.id}\nData: {pedido.data}")
                itens = PedidosDAO.visualizar_pedido(pedido.id)
                print("Itens:")
                for item in itens:
                    print(item)

                print(f"\nTotal: R${pedido.total:.2f}")
        else:
            print("\nNão há histórico de pedidos.")
    
    @staticmethod
    def exibir_pedidos():
        print("\n=== Pedidos ===")
        pedidos = PedidosDAO.buscar_pedidos()
        if pedidos:
            for pedido in pedidos:
                print(f"Pedido ID: {pedido.id}\nData: {pedido.data} \nCliente ID: {pedido.cliente_id}")
                itens = PedidosDAO.visualizar_pedido(pedido.id)
                print("Itens:")
                for item in itens:
                    print(item)

                print(f"\nTotal: R${pedido.total:.2f}")
        else:
            print("\nNenhum pedido registrado.")

    @staticmethod
    def pagando(carrinho):
        while True:
            print("\nDeseja finalizar a compra?\n1. Sim \n0. Não")
            opcao = int(input())

            match opcao:
                case 0:
                    return
                case 1:
                    pass
                case _:
                    raise ValueError("Opção inválida.")
                
            menus.menu_pagamento()

            opcao = int(input())

            match opcao:
                case 1:
                    ProdutosDAO.atualizar_estoque(carrinho)
                    CartaoCredito().processar()
                    carrinho.finalizar()
                    PedidosDAO.atualizar_pedido(carrinho)
                    break
                case 2:
                    ProdutosDAO.atualizar_estoque(carrinho)
                    Boleto().processar()
                    carrinho.finalizar()
                    PedidosDAO.atualizar_pedido(carrinho)
                    break
                case 3:
                    ProdutosDAO.atualizar_estoque(carrinho)
                    Pix().processar()
                    carrinho.finalizar()
                    PedidosDAO.atualizar_pedido(carrinho)
                    break
                case _:
                    raise ValueError("Opção inválida.")
    
    @staticmethod
    def remover_produto_carrinho(carrinho : Pedido):
        while True:
            try:
                print("\nPara voltar digite '0'.")
                id_produto = input("Informe o ID do produto: ")

                if id_produto == '0':
                    break

                id_produto = int(id_produto)
                if utils.validar_id(id_produto):
                    for item in carrinho.itens:
                        if item.produto_id == id_produto:
                            if item.quantidade > 1:
                                item.quantidade -= 1
                                print("\nRemovido 1 tem do carrinho.")
                                PedidosDAO.atualizar_pedido(carrinho)
                                return
                            else:
                                carrinho.itens.remove(item)
                                print("\nItem Removido do Carrinho.")
                                PedidosDAO.remover_pedido_item(carrinho.id, item.produto_id)
                                return
                            
                    print("Produto não encontrado")
                    return
                
            except ValueError as e:
                print("Erro:", e)
    
    @staticmethod 
    def gerar_relatorios():
        try:
            pedidos = PedidosDAO.buscar_pedidos()
            produtos = ProdutosDAO.listar_produtos()


            # cria o dicionário de produtos
            produtos_dict = {p.id: p for p in produtos}
           
            Relatorios.gerar_relatorio_pedidos(pedidos, produtos_dict)
            Relatorios.gerar_relatorio_itens(pedidos, produtos_dict)
            Relatorios.gerar_relatorio_estoque(produtos)
            print("\nRelatórios Gerados com sucesso")
        except Exception as e:
            print("Erro:", e)
        



        