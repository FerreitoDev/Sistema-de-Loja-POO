from .utils import validar_texto_vazio
class Produto:
    def __init__(self, nome, preco, quantidade_estoque, id = None):
        self.id = id
        self.nome = nome
        self.preco = preco
        self.quantidade_estoque = quantidade_estoque

    @staticmethod
    def validar_valor(valor):
        if valor <= 0:
            raise ValueError("Valor tem que ser maior que 0")
        return True
    
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
        if Produto.validar_valor(valor):
            self._preco = valor

    @property
    def quantidade_estoque(self):
        return self._quantidade_estoque
    
    @quantidade_estoque.setter
    def quantidade_estoque(self, qtd):
        if Produto.validar_valor(qtd):
            self._quantidade_estoque = qtd

    def __str__(self):
        return f"ID: {self.id}, nome: {self._nome}, preço: {self._preco:.2f}, quantidade_estoque: {self._quantidade}" 


