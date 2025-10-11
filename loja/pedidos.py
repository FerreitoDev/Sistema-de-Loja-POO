from datetime import datetime

DATA = datetime.now().strftime("%Y%m%d_%H%M%S")

class Pedido:
    def __init__(self, cliente_id, id = None, total = 0.0):
        self.id = id
        self.cliente_id = cliente_id
        self.itens= []
        self.total = total
        self.status = "aberto"
        self.data = DATA

    def adicionar_item(self, produto_id, preco_unitario):
        for item in self.itens:
            if item.produto_id == produto_id:
                item.quantidade +=1
                item.atualizar_subtotal(item.quantidade, preco_unitario )
                self.atualizar_total()
                return
        novo_item = PedidoItem(produto_id, self.id, preco_unitario)
        self.itens.append(novo_item) 
        self.atualizar_total()
        
    def atualizar_total(self):
        self.total = sum(item.subtotal for item in self.itens)

    def __str__(self):
        pedido = f"Pedido ID: {self.id}\nCliente ID: {self.cliente_id}\nData: {self.data}\nStatus: {self.status}\nTotal: R${self.total:.2f}\nItens:\n"
        for item in self.itens:
            pedido += "  - "  + str(item) + "\n"
        return pedido

class PedidoItem:
    def __init__(self, produto_id, pedido_id, preco_unitario = 0.0, quantidade = 1, id = None):
        self.id = id
        self.pedido_id = pedido_id
        self.produto_id = produto_id
        self.quantidade = quantidade
        self.preco_unitario = preco_unitario
        self.subtotal = preco_unitario 

    def atualizar_subtotal(self, quantidade, preco_unitario):
        self.subtotal = quantidade * preco_unitario
    
    def __str__(self):
        return f"Produto ID: {self.produto_id}, Quantidade: {self.quantidade}, Preço Unit: R${self.preco_unitario:.2f}, Subtotal: R$ {self.subtotal:.2f}"
    
class PedidoItemDetalhado:
    def __init__(self, produto_id, produto_nome, quantidade, preco_unitario, subtotal):
        self.produto_id = produto_id
        self.produto_nome = produto_nome
        self.quantidade = quantidade
        self.preco_unitario = preco_unitario
        self.subtotal = subtotal 

    def __str__(self):
        return f"ID: {self.produto_id}. {self.produto_nome}, Qtd: {self.quantidade}, Preço Unit: R${self.preco_unitario:.2f}, Subtotal: R${self.subtotal:.2f}"