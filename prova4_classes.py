class Marca:
    def __init__(self, nome, origem):
        self.nome = nome
        self.origem = origem
    def get_nome(self):
        return self.nome
    def get_origem(self):
        return self.origem
    def set_nome(self, novo_nome):
        self.nome = novo_nome
    def set_origem(self, novo_origem):
        self.origem = novo_origem
    def fabricante(self):
        if self.origem in ('Alemanha', 'Franca', 'Espanha', 'Reino Unido', 'Italia'):
            fabricante = 'Europeia'
        elif self.origem in ('China', 'Japao', 'Coreia do Sul', 'India'):
            fabricante = 'Asiatica'
        else:
            fabricante = 'Americana'
        return fabricante


class Carro (Marca):
    def __init__(self, nome_modelo, ano, nome, origem):
        super().__init__(nome, origem)
        self.nome_modelo = nome_modelo
        self.ano = ano
    def get_nomeModelo(self):
        return self.nome_modelo
    def get_ano(self):
        return self.ano
    def set_nomeModelo(self, novo_nomeModelo):
        self.nome_modelo = novo_nomeModelo
    def set_ano(self, novo_ano):
        self.ano = novo_ano