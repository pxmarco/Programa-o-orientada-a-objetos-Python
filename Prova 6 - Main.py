from prova6_classes import Pais, Cidade, Telefone
p1 = Pais ('+52', 'Breizil')
c1 = Cidade ('+55', 'Brasil', 'Planalto', 61)
c2 = Cidade('+55', 'Brasil', 'Arinos', 30)
t1 = Telefone ('+55', 'Brasil', '98291-3537')
print (p1, c1, c2, t1)
p1.set_pais('Brasil')
p1.set_ddi('+55')
c1.set_cidade('Brasília')
c2.set_ddd(38)
t1.set_telefone('98291-7612')
print ("\n--------- País ---------\nDDI: ", p1.get_ddi(), "\nPaís: ", p1.get_pais())
print ("\n------- Cidade 1 -------\nDDI: ", c1.get_ddi(), "\nPaís: ", c1.get_pais(),
       "\nCidade: ", c1.get_cidade(), "\nDDD: ", c1.get_ddd())
print ("\n------- Cidade 2 -------\nDDI: ", c2.get_ddi(), "\nPaís: ", c2.get_pais(),
       "\nCidade: ", c2.get_cidade(), "\nDDD: ", c2.get_ddd())
print ("\n------- Telefone -------\nDDI: ", t1.get_ddi(),"\nPaís: ", t1.get_pais(),
       "\nTelefone: (", c1.get_ddd(), ")", t1.get_telefone())
