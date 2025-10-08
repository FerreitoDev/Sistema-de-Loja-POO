from .utils import validar_texto_vazio, validar_valor
class Produto:
    def __init__(self, nome, preco, quantidade_estoque, id = None):
        self.id = id
        self.nome = nome
        self.preco = preco
        self.quantidade_estoque = quantidade_estoque

    
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, texto):
        if validar_texto_vazio(texto):
            self._nome = texto.strip().title()

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, valor):
        if validar_valor(valor):
            self._preco = float(valor)

    @property
    def quantidade_estoque(self):
        return self._quantidade_estoque
    
    @quantidade_estoque.setter
    def quantidade_estoque(self, qtd):
        if validar_valor(qtd):
            self._quantidade_estoque = qtd

    def __str__(self):
        return f"ID: {self.id}, Nome: {self._nome}, Preço: R${self._preco:.2f}, Quantidade: {self._quantidade_estoque}" 
    

