from prova5_classes import Calcado, Feminino, Masculino
if __name__ == '__main__':
    c1 = Calcado ('Preto', 'Louboutin')
    c2 = Calcado ('Preto', 'Vans')
    f1 = Feminino (36, 'Salto', 'Preto', 'Gucci')
    f2 = Feminino (34, 'Sapatilha', 'Branco', 'Vans')
    m1 = Masculino(40, 'Sapato', 'Preto', 'Gucci')
    m2 = Masculino(42, 'Tenis', 'Branco', 'Vans')
    c1.set_marca('Gucci')
    f2.set_tamanho(35)
    c2.set_cor('Branco')
    m1.set_tipo('Sapatenis')
    m2.set_cor('Preto')
    print ("--------- Calçado 1 ---------\nCor: ", c1.get_cor(), "\nMarca: ", c1.get_marca())
    print ("\n--------- Calçado 2 ---------\nCor: ", c2.get_cor(), "\nMarca: ", c2.get_marca())
    print("\n--- Calçado feminino 1 ---\nTamanho: ", f1.get_tamanho(), "\nTipo: ", f1.get_tipo(),
    "\nCor: ", f1.get_cor(), "\nMarca: ", f1.get_marca())
    print("\n--- Calçado feminino 2 ---\nTamanho: ", f2.get_tamanho(), "\nTipo: ", f2.get_tipo(),
    "\nCor: ", f2.get_cor(), "\nMarca: ", f2.get_marca())
    print("\n--- Calçado Masculino 1 ---\nTamanho: ", m1.get_tamanho(), "\nTipo: ", m1.get_tipo(),
    "\nCor: ", m1.get_cor(), "\nMarca: ", m1.get_marca())
    print("\n--- Calçado Masculino 2 ---\nTamanho: ", m2.get_tamanho(), "\nTipo: ", m2.get_tipo(),
    "\nCor: ", m2.get_cor(), "\nMarca: ", m2.get_marca())
