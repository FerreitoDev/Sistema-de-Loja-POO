from loja import db
# from loja.repositorios.usuarios_dao import UsuarioDAO
from loja.autenticador import Autenticador
from loja import menus
db.criar_tabela_clientes()
def main():
    login = False
    while True:
        if not login:
            logar = cadastrar = False
            menus.menu_login_cadastro()
            try:
                opcao = int(input("Escolha uma opção: "))
            except ValueError:
                print("\nErro: Valor inválido")
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
                print("=== Login ===")
                while True:
                    try:
                        print("Para voltar digite 'sair' no campo Email.")
                        email = input("Email: ")
                        if email.upper().strip() == "SAIR":
                            break
                        Autenticador.validar_email(email)
                        senha = input("Senha: ")
                        usuario_login = Autenticador.logar(email, senha)
                        if usuario_login:
                            login = True
                            print("Usuario logado com sucesso.")
                            break
                    except (Autenticador.ErroLogin, ValueError) as e:
                        print("Erro:", e)
                        continue

if __name__ == "__main__":
    main()
 










# db.criar_tabela_adm()
# try:
#     adm = Autenticador.cadastro_adm("Administrador", "administrador@loja.com", "contateste123@")
#     UsuarioDAO.adicionar_adm(adm)
# except ValueError as e:
#     print(e)