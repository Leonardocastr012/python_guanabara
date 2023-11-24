#Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
def linha():
    print('--'*20)
jogadores = []
jogador =  dict()
gols = []
golsTotais = 0
while True:
    jogador['Nome'] = str(input('Nome: '))
    jogador['Partidas'] = int(input('Números de partidas: '))
    for i in range (1, jogador['Partidas'] + 1):
        golPorPartida = int(input(f'Quantos gols fez na partida {i}? '))
        gols.append(golPorPartida)
        golsTotais += golPorPartida
    jogador['gols'] = gols[:]
    jogador['golsTotais'] = golsTotais
    jogadores.append(jogador.copy())
    #Limpando os dados para o próximo loop
    gols.clear()
    golsTotais = 0
    escolha = str(input('Deseja continuar[S/N]? ')).upper()[0]
    if escolha == 'N':
         break
linha()
print(f'{"cod":<4}{"nome":<15}{"gols":<15}{"total"}')
for i , elemento in enumerate(jogadores):
    print(f'{i:>4}{elemento["Nome"] :<15}{elemento["gols"] :<15}{elemento["golsTotais"] :<5}')
linha()





# linha()
# print(jogador)
# linha()
# for k, v in jogador.items():
#     print(f'O {k} tem valor {v}')

# linha()
# print(f'O jogador {jogador["Nome"]} jogou {jogador["Partidas"]} partidas')
# for i in range (0, jogador['Partidas']): # fiz o range normal pois na lista o range começa no 0 
#     print(f'   =>Na partida {i + 1}, fez {gols[i]} gols')
# print(f'Foi um total de {jogador["golsTotais"]} gols ')