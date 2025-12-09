"""
Criação de Classe para sistema de venda de calçados
"""

class Calcados:
   def __init__(self, nome, tipo, cor, tamanho, valor):
       self.nome = nome
       self.tipo = tipo
       self.cor = cor
       self.tamanho = tamanho
       self.valor = valor
   def get_nome (self):
       return self.nome
   def get_tipo (self):
       return self.tipo
   def get_cor (self):
       return self.cor
   def get_tamanho (self):
       return self.tamanho
   def get_valor (self):
       return self.valor
   def set_nome (self, new_nome):
       self.nome = new_nome
   def set_tipo (self, new_tipo):
       self.tipo = new_tipo
   def set_cor(self, new_cor):
       self.cor = new_cor
   def set_tamanho(self, new_tamanho):
       self.tamanho = new_tamanho
   def set_valor(self, new_valor):
       self.valor = new_valor


   def mostra_dados (self):
       print("\nO nome do tênis é ", self.nome, " do tipo ", self.tipo, ", com cor",
             self.cor, ", tamanho", self.tamanho, f"e valor R${self.valor:.2f}")

   def mostra_dados2(self):
       print("\nDados do calçado:")
       print("Nome:", self.get_nome())
       print("Tipo:", self.get_tipo())
       print("Cor:", self.get_cor())
       print("Tamanho:", self.get_tamanho())
       print(f"Valor: R${self.get_valor():.2f}")

   def reajuste(self, reajuste):
       self.valor = self.valor + reajuste


if __name__ == '__main__':
   shoes1 = Calcados ('Air max', 'Casual', 'Branco', 42,500.00)
   print (shoes1)
   shoes2 = Calcados ('Mizuno', 'Esportivo', 'Preto', 41, 450.00)
   print (shoes2)
   shoes3 = Calcados ('Havaianas', 'Chinelo', 'Azul', 43, 45.00)
   print (shoes3)
   shoes4 = Calcados ('Kenner', 'Chinelo', 'Preto', 42, 60.00)
   print(shoes4)

   shoes1.mostra_dados()
   shoes1.set_nome('Airmax')
   shoes1.mostra_dados()

   shoes4.mostra_dados2()
   shoes4.set_tipo('Sandália')
   shoes4.mostra_dados2()

   shoes3.mostra_dados2()
   shoes3.set_tamanho(40)
   shoes3.mostra_dados2()

   shoes2.reajuste(25.00)
   shoes2.mostra_dados2()

