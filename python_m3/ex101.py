#Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
# retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
def voto(num):
    from datetime import date
    anoAtual = date.today().year
    idade = anoAtual - num
    return idade

n = int(input('Ano de nascimento: '))
print(f'Com {voto(n)} anos: ', end='')
if voto(n) < 16:
    print('Voto NEGADO!')
elif  16 <= voto(n) < 18:
    print('Voto OPCIONAL!')
else:
    print('Voto OBRIGATÓRIO!')