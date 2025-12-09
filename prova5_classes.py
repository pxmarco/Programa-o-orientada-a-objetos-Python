class Calcado:
    def __init__(self, cor, marca):
        self.cor = cor
        self.marca = marca
    def get_cor(self):
        return self.cor
    def get_marca(self):
        return self.marca
    def set_cor(self, novo_cor):
        self.cor = novo_cor
    def set_marca(self, novo_marca):
        self.marca = novo_marca


class Feminino (Calcado):
    def __init__(self, tamanho, tipo, cor, marca):
        super().__init__(cor, marca)
        self.tamanho = tamanho
        self.tipo = tipo
    def get_tamanho(self):
        return self.tamanho
    def get_tipo(self):
        return self.tipo
    def set_tamanho(self, novo_tamanho):
        self.tamanho = novo_tamanho
    def set_tipo(self, novo_tipo):
        self.tipo = novo_tipo

class Masculino (Feminino):
    def __init__(self, tamanho, tipo, cor, marca):
        super().__init__(tamanho, tipo, cor, marca)
