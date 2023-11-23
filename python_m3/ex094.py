#Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. 
'''No final, mostre: 
A) Quantas pessoas foram cadastradas 
B) A média de idade 
C) Uma lista com as mulheres 
D) Uma lista de pessoas com idade acima da média'''
pessoas = []
idadeSomada = 0
while True:
    pessoa = dict()
    pessoa['Nome'] = str(input('Nome: '))
    sexo = str(input('Sexo [M/F]: ')).upper()[0]
    if sexo == 'M' or sexo == 'F':
          pessoa['Sexo'] = sexo
    else: #Quando usuário errar a opcão
        print('ERRO! Responda apenas com S ou N')
        sexo = str(input('Sexo [M/F]: ')).upper()[0]
    pessoa['Idade'] = int(input('Idade: '))
    
    idadeSomada += pessoa['Idade']

    pessoas.append(pessoa.copy())
    escolha = str(input('Deseja continuar[S/N]? ')).upper()[0]
    if escolha == 'N':
         break
    if escolha != 'S': #Quando usuário errar a opcão
        escolha = str(input('Deseja continuar[S/N]? ')).upper()[0]
        if escolha == 'N':
            break
print(f'Ao todo temos {len(pessoas)} pessoas cadastradas')
#Média
mediaIdade = idadeSomada / len(pessoas)
print(f'A média de idade é {mediaIdade} anos')
#Mulheres cadastradas
#Acima da idade média
