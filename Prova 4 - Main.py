from prova4_classes import Marca, Carro
if __name__ == '__main__':
    m1 = Marca ('Volkswagen', 'Germany')
    m2 = Marca ('Citroen', 'Franca')
    c1 = Carro ('Gol', 2010, 'Volkswagen', 'Alemanha')
    c2 = Carro ('C3', 2010, 'Citroen', 'Franca')
    m1.set_origem('Alemanha')
    m2.set_nome('Renault')
    c1.set_ano(2020)
    c2.set_nomeModelo('Kwid')
    print ("--------- Marca 1 ---------\nNome: ", m1.get_nome(), "\nOrgiem: ", m1.get_origem())
    print ("--- Carro 1 ---\nNome: ", c1.get_nomeModelo(), "\nAno de fabricação: ", c1.get_ano(), "\nFabricante: ", c1.fabricante())
    print ("\n--------- Marca 2 ---------\nNome: ", m2.get_nome(), "\nOrgiem: ", m2.get_origem())
    print("--- Carro 2 ---\nNome: ", c2.get_nomeModelo(), "\nAno de fabricação: ", c2.get_ano(), "\nFabricante: ", c2.fabricante())
