import os
import csv
from datetime import datetime

RELATORIO_PEDIDOS = "relatorio_pedidos"
RELATORIO_ITEMS = "relatorio_item"
RELATORIO_ESTOQUE = "relatorio_estoque"

#Caminho base
CAMINHO = "relatorios/"

os.makedirs(CAMINHO, exist_ok = True)

class Relatorios:

    @staticmethod
    def caminho_relatorio(relatorio_const):
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        return f"{CAMINHO}{relatorio_const}_{timestamp}.csv"

    @staticmethod
    def gerar_relatorio_pedidos(pedidos, produtos):

        caminho = Relatorios.caminho_relatorio(RELATORIO_PEDIDOS)
        with open(caminho, 'w', encoding = 'utf8', newline = '') as arquivo:
            writer = csv.writer(arquivo)
            writer.writerow(["Pedido ID", "Cliente", "Data", "Status", "Total", "Itens"])

            for pedido in pedidos:
                itens_texto = "; ".join(
                    f"{produtos[item.produto_id].nome} x{item.quantidade} = {item.subtotal:.2f}"
                    for item in pedido.itens
                )
                writer.writerow([
                    pedido.id,
                    pedido.cliente_id,
                    pedido.data,
                    pedido.status,
                    f"{pedido.total:.2f}",
                    itens_texto
                ])

    @staticmethod
    def gerar_relatorio_itens(pedidos, produtos):
        caminho = Relatorios.caminho_relatorio(RELATORIO_ITEMS)
        with open(caminho, 'w', encoding='utf-8', newline='') as arquivo:
            writer = csv.writer(arquivo)
            writer.writerow(["Pedido ID", "Cliente", "Produto", "Qtd", "Preço Unit", "Subtotal", "Data"])
            
            for pedido in pedidos:
                for item in pedido.itens:
                    writer.writerow([
                        pedido.id,
                        pedido.cliente_id,
                        produtos[item.produto_id].nome,
                        item.quantidade,
                        f"{item.preco_unitario:.2f}",
                        f"{item.subtotal:.2f}",
                        pedido.data
                    ])

    @staticmethod
    def gerar_relatorio_estoque(produtos):
        caminho = Relatorios.caminho_relatorio(RELATORIO_ESTOQUE)
        with open(caminho, 'w', encoding = 'utf-8', newline = '') as arquivo:
            writer = csv.writer(arquivo)
            writer.writerow(["Produto ID", "Nome", "Preço", "Qtd Estoque"])

            for produto in produtos:
                writer.writerow([
                    produto.id,
                    produto.nome,
                    produto.preco,
                    produto.quantidade_estoque,
                ])
    
    