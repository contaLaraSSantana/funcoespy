#Faça um programa que tenha uma função chamada ficha(), que receba
#dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou.
#O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado
#não tenha sido informado corretamente

def ficha(nome="", gol=0):
    print("O nome do jogador é ",nome," e a quantidade de gols foi de ",gol)

ficha(nome='Bruno')
