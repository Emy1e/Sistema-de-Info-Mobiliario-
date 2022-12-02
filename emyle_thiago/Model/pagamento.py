#Classe Pagamento
class Pagamento:
    def __init__(self, forma_pagamento):
        self.forma_pagamento = forma_pagamento

    #
    def nova_forma_pagamento(forma_pagamento):
        if(forma_pagamento == "cartao"):
            print("cartao")