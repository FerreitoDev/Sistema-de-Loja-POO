Sistema de Loja POO

Descrição:
Esta é uma aplicação de linha de comando em Python que implementa uma loja simples com: cadastro e login de usuários (clientes e administradores), gerenciamento de produtos, carrinho de compras, processamento de pedidos e geração de relatórios em CSV. Os dados são persistidos em SQLite.

Pré-requisitos:
- Python 3.8+ instalado
- Dependência: bcrypt (instalar com pip se desejar usar cadastro/login que hasheia senhas)

Instalação rápida:
1) Abra um terminal na pasta do projeto.
2) (Opcional) crie e ative um ambiente virtual.
3) Instale o bcrypt: pip install bcrypt

Como executar:
1) No terminal, rode: python main.py
2) Na primeira execução, o arquivo de banco SQLite `loja.db` será criado automaticamente.
3) Siga os menus para cadastrar usuários, gerenciar produtos e processar pedidos.

Estrutura do projeto (resumo):
- main.py: entrada da aplicação e loop de menus
- loja/db.py: criação de tabelas e conexão SQLite
- loja/utils.py: validadores e helper de input
- loja/autenticador.py: validação e hashing de senha usando bcrypt
- loja/usuarios.py: classes Usuario, Cliente, Adm
- loja/produtos.py: modelo Produto
- loja/pedidos.py: Pedido, PedidoItem, regras de totalização
- loja/pagamentos.py: simulação de pagamentos (Cartão, Boleto, Pix)
- loja/relatorios.py: exporta relatórios em CSV na pasta relatorios/
- loja/interface/: menus e fluxo de interação com o usuário
- loja/repositorios/: DAOs para produtos, pedidos e usuários (interagem com SQLite)

Observações importantes:
- Senhas são armazenadas como hash com bcrypt. Garanta que a dependência esteja instalada para cadastrar/login funcionar corretamente.
- O arquivo `loja.db` é gerado automaticamente e está listado em .gitignore.
- Arquivos de relatório são salvos na pasta `relatorios/` em CSV com timestamp no nome.

Autor: FerreitoDev
Repositorio: Sistema-de-Loja-POO

