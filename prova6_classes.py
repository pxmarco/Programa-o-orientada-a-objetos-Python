class Pais:
    def __init__(self, ddi, pais):
        self.pais = pais
        self.ddi = ddi
    def get_ddi(self):
        return self.ddi
    def get_pais(self):
        return self.pais
    def set_ddi(self, novoddi):
        self.ddi = novoddi
    def set_pais(self, novopais):
        self.pais = novopais

class Cidade (Pais):
    def __init__(self, ddi, pais, cidade, ddd):
        super().__init__(ddi, pais)
        self.cidade = cidade
        self.ddd = ddd
    def get_cidade(self):
        return self.cidade
    def get_ddd(self):
        return self.ddd
    def set_ddd(self, novoddd):
        self.ddd = novoddd
    def set_cidade(self, novacidade):
        self.cidade = novacidade

class Telefone (Pais):
    def __init__(self, ddi, pais, telefone):
        super().__init__(ddi, pais)
        self.telefone = telefone
    def get_telefone(self):
        return self.telefone
    def set_telefone(self, novotelefone):
        self.telefone = novotelefone