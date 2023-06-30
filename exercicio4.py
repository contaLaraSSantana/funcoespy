#.Crie um programa que tenha uma função chamada voto() que vai receber
# como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando
# se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

def voto(ano):
    ano = 2023 - ano
    if ano < 16:
        print('voto NEGADO')
    elif ano >= 16 and ano <= 18:
        print('voto OPCIONAL')
    else:
        print('voto OBRIGATÓRIO')


a= int(input("Digite o anoo do seu nascimento: "))
voto(a)