#Faça um programa que tenha uma função chamada maior(), que receba vários
#parâmetros com valores inteiros. Seu programa tem que analisar todos os valores
#e dizer qual deles é o maior.

def maior(*valores):
    print("O maior numero é",max(valores))


maior(30,10,40,11,39)