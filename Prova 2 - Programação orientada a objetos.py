"""
Criação de Classe para cálculo de índice de massa corporal (IMC), tendo a altura em cm totais (int) e peso em kg (float)
"""

class Paciente:
   def __init__(self, nome, peso, altura):
       self.nome = nome
       self.peso = peso
       self.altura = altura
   def get_nome (self):
       return self.nome
   def get_peso (self):
       return self.peso
   def get_altura (self):
       return self.altura
   def set_nome (self, new_nome):
       self.nome = new_nome
   def set_peso (self, new_peso):
       self.peso = new_peso
   def set_altura(self, new_altura):
       self.altura = new_altura


   def imc (self):
       imc = self.peso/((self.altura/100)**2)
       if imc <= 18.5:
           print (f"{self.nome} está abaixo do peso")
       elif imc > 18.5 and imc <= 25:
           print (f"{self.nome} está com peso normal")
       elif imc > 25 and imc <= 30:
           print (f"{self.nome} está com sobrepeso")
       else:
           print (f"{self.nome} está com obesidade")


if __name__ == '__main__':
   pessoa1 = Paciente ('Jair', 85.0, 172)
   print (pessoa1)
   pessoa2 = Paciente ('Dilma', 50.0, 165)
   print (pessoa2)
   pessoa3 = Paciente ('Lula', 90.0, 167)
   print (pessoa3)
   pessoa1.set_nome('Bolsonaro')
   print ("- Paciente 1:\nNome:", pessoa1.get_nome(), "\nPeso:", pessoa1.get_peso(), "\nAltura:", pessoa1.get_altura())
   pessoa3.set_altura(166)
   print("- Paciente 3:\nNome:", pessoa3.get_nome(), "\nPeso:", pessoa3.get_peso(), "\nAltura:", pessoa3.get_altura())
   pessoa2.set_peso(60.0)
   print ("- Paciente 2:\nNome:", pessoa2.get_nome(), "\nPeso:", pessoa2.get_peso(), "\nAltura:", pessoa2.get_altura(), "\n")

pessoa1.imc()
pessoa2.imc()
pessoa3.imc()
