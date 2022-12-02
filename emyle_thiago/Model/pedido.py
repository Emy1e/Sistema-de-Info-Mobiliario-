#Classe Pedido
from pagamento import Pagamento
from produto import Produto
class Pedido:
    def __init__(self, valor_pedido, forma_pagamento, desconto, frete):
        produto = Produto()
        self.valor_pedido = valor_pedido
        forma_pagameto = Pagamento()
        self.desconto = desconto 
        self.frete = desconto

