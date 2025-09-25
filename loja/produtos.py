class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

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
        if not texto.strip():
            raise ValueError("Nome não pode ser vazio")
        self._nome = texto.strip().title()

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, valor):
        if Produto.validar_valor(valor):
            self._preco = valor

    @property
    def quantidade(self):
        return self._quantidade
    
    @quantidade.setter
    def quantidade(self, qtd):
        if Produto.validar_valor(qtd):
            self._quantidade = qtd

    def __str__(self):
        return f"nome: {self._nome}, preço: {self._preco}, quantidade: {self._quantidade}" 


