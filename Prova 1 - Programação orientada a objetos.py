"""
Projete o programa que leia vários valores reais digitados pelo usuário e no final mostre as seguintes informações:
- A quantidade de valores digitados;
- A soma dos valores digitados;
- A média aritmética dos valores digitados;
- E a quantidade de valores digitados maior que 20.
"""
cont = 0
soma = 0
cont2 = 0
print ("\nDigite [-1] para sair")
while True:
   valor = float(input("Valor: "))
   if valor == -1:
       break
   cont = cont+1
   soma = soma+valor
   if valor > 20:
       cont2 = cont2+1
print ("\nQuantidade de valores: ", cont)
media = soma/cont
print ("\nMedia dos valores:", media)
print ("\nQuantidade de valores acima de 20: ", cont2)

"""
Elabore o programa para somar todos os números inteiros que se encontram no intervalo de um a quinhentos.
"""
soma = 0
for i in range(1, 501, 1):
   soma = soma + i
print("Soma de todos os valores: ", soma)

"""
Elabore o programa para somar todos os números inteiros que são ao mesmo tempo ímpar e múltiplo de três que se encontram no intervalo de um a quinhentos.
"""
soma = 0
for i in range(1, 501, 1):
   if i % 3 == 0 and i % 2 != 0:
       soma = soma + i
print("Soma de todos os valores ímpares/multiplos de 3: ", soma)

"""
Crie uma função para somar três valores. Ela recebe os três valores, calcula a soma e retorna o resultado do cálculo. 
A função main lê os três valores inteiros, chama a função passando os valores lidos e depois mostra o valor retornado pela função, ou seja, o resultado obtido.
"""
def calc_soma (v1, v2, v3):
    soma = v1 + v2 + v3
    return soma
if __name__ == '__main__':
    n1 = int (input("Digite um valor: "))
    n2 = int (input("Digite outro valor: "))
    n3 = int (input("Digite mais um valor: "))
    soma = calc_soma(n1, n2, n3)
    print ("O resultado da soma é: ", soma)

"""
Elabore a função (def) valor absoluto que recebe um número qualquer e retorna o valor absoluto (módulo) correspondente. O programa lê o número digitado pelo usuário, chama a função valor absoluto passando o número lido e depois gera a tela de saída com o valor retornado pela função valor absoluto. Lembrando que valor absoluto de um número positivo é ele mesmo e o valor absoluto de um número negativo é ele multiplicado por -1. Não use a função abs da linguagem.
"""
def absolut (v1):
    if v1 >= 0 :
        v1 = v1
    else:
        v1 = v1 * -1
    return v1
if __name__ == '__main__':
    n1 = int(input("Digite um valor: "))
    v_abs = absolut(n1)
    print ("Valor absoluto é |", n1, "| = ", v_abs)

"""
Simule uma calculadora com as quatro operações aritméticas. Implemente uma função para cada operação aritmética. Ela recebe dois valores e não retorna nada. A função executa o cálculo e mostra o resultado do cálculo. O usuário fornecerá a operação desejada (operador: +, -, x, / ) e os dois valores dentro do programa (função main) que chamará uma das quatro funções. O resultado do cálculo será mostrado dentro de cada função. Use variável local.
"""
def somar(v1, v2):
    result = v1 + v2
    print("O resultado da soma é: ", result)

def subtrair(v1, v2):
    result = v1 - v2
    print("O resultado da subtração é: ", result)

def multiplicar(v1, v2):
    result = v1 * v2
    print("O resultado da multiplicação é: ", result)

def dividir(v1, v2):
    result = v1 / v2
    print("O resultado da divisão é: ", result)

def main():
    operacao = input("Digite a operação desejada (+, -, x, /): ")
    n1 = float(input("Digite o primeiro valor: "))
    n2 = float(input("Digite o segundo valor: "))
    if operacao == '+':
        somar(n1, n2)
    elif operacao == '-':
        subtrair(n1, n2)
    elif operacao == 'x':
        multiplicar(n1, n2)
    elif operacao == '/':
        dividir(n1, n2)

if __name__ == "__main__":
    main()