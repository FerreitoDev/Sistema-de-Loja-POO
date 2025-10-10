class Pagamento:
    def processar(self):
        print("Processando...")

class CartaoCredito(Pagamento):
    def processar(self):
        print("\nPagamento com cartão de crédito aprovado")
        return True

class Boleto(Pagamento):
    def processar(self):
        print("\nPagamento com boleto registrado")
        return True

class Pix(Pagamento):
    def processar(self):
        print("\nPagamento com PIX concluído")
        return True
    
    
    
    