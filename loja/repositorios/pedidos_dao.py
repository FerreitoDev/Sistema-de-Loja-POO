from loja.db import DataBase
from loja.pedidos import Pedido, PedidoItem, PedidoItemDetalhado
class PedidosDAO:

    @staticmethod
    def criar_pedido(pedido: Pedido):
        with DataBase.obter_conexao() as conexao:
            cursor = conexao.cursor()

            cursor.execute(
                "INSERT INTO pedidos (cliente_id, total, status, data) VALUES (?, ?, ?, ?)",
                (pedido.cliente_id, pedido.total, pedido.status, pedido.data)    
            )

            pedido.id = cursor.lastrowid

            for item in pedido.itens:
                cursor.execute("""
                    INSERT INTO pedido_itens (pedido_id, produto_id, quantidade, preco_unitario, subtotal)
                    VALUES (?, ?, ?, ?, ?)               
                    """, (
                        pedido.id,
                        item.produto_id,
                        item.quantidade,
                        item.preco_unitario,
                        item.subtotal
                    ))
            
            conexao.commit()

    @staticmethod
    def atualizar_pedido(carrinho: Pedido):
        with DataBase.obter_conexao() as conexao:
            cursor = conexao.cursor()


            for item in carrinho.itens:

                cursor.execute("""
                    SELECT id FROM pedido_itens WHERE pedido_id = ? AND produto_id = ?
                    """, (carrinho.id, item.produto_id))
                item_dados = cursor.fetchone()

                if item_dados: #atualiza os items ja existentes
                    item_id = item_dados[0]
                    cursor.execute("""
                        UPDATE pedido_itens SET quantidade = ?, subtotal = ? WHERE id = ?
                    """, (item.quantidade, item.subtotal, item_id))

                else:
                    cursor.execute("""
                        INSERT INTO pedido_itens (pedido_id, produto_id, quantidade, preco_unitario, subtotal)
                        VALUES (?, ?, ?, ?, ?)
                    """, (carrinho.id, item.produto_id, item.quantidade, item.preco_unitario, item.subtotal))

                cursor.execute("UPDATE pedidos SET total = ?, status = ? WHERE id = ?", (carrinho.total, carrinho.status, carrinho.id))
           
            conexao.commit()

    @staticmethod
    def buscar_cliente_pedido_aberto(client_id):
        with DataBase.obter_conexao() as conexao:
            cursor = conexao.cursor()

            cursor.execute("""
                SELECT id, cliente_id, total, status, data
                FROM pedidos
                WHERE cliente_id = ? AND status = 'aberto'
                LIMIT 1
            """,(client_id,))

            dados_pedido = cursor.fetchone()

            if not dados_pedido:
                return None
            
            pedido = Pedido(
                cliente_id = dados_pedido[1], id = dados_pedido[0], total = dados_pedido[2],
            )
            pedido.status = dados_pedido[3]
            pedido.data = dados_pedido[4]

            cursor.execute("""
                SELECT id, produto_id, quantidade, preco_unitario, subtotal
                FROM pedido_itens
                WHERE pedido_id = ?
            """, (pedido.id,))

            itens = cursor.fetchall()

            for item in itens:
                pedido_item = PedidoItem(
                produto_id=item[1],
                    pedido_id=pedido.id,
                    preco_unitario=item[3],
                    quantidade=item[2],
                    id=item[0]
                )
                pedido_item.subtotal = item[4]
                pedido.itens.append(pedido_item)

            return pedido  
         
    @staticmethod
    def visualizar_pedido(pedido_id):
       
        with DataBase.obter_conexao() as conexao:
            cursor = conexao.cursor()
            
            # Busca os itens do pedido com JOIN para pegar o nome do produto
            cursor.execute("""
                SELECT 
                    p.nome, 
                    pi.quantidade, 
                    pi.preco_unitario,
                    pi.subtotal
                FROM pedido_itens pi
                JOIN produtos p ON pi.produto_id = p.id
                WHERE pi.pedido_id = ?
            """, (pedido_id,))
            
            resultados = cursor.fetchall()
            
            # Monta objetos detalhados
            itens_detalhados = [
                PedidoItemDetalhado(nome, quantidade, preco_unitario, subtotal)
                for nome, quantidade, preco_unitario, subtotal in resultados
            ]
            
            return itens_detalhados