class Cliente:
    def __init__(self, n, fone):
        self.nome = n
        self.telefone = fone

    #metodo set
    def set_nome(self, nome):
        self._nome = nome
        
    
    