#Faça um programa que tenha uma função chamada área(), que receba as
#dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

def area(largura,comprimento):
    a = largura*comprimento
    print('A área é de:', a)

area(float(input('Digite a largura:')), float(input('Digite o comprimento:')))



