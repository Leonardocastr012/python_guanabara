#Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:  
# A) Quantas pessoas foram cadastradas. 
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.
cadastro = []
pessoa = []
maiorPeso = menorPeso = 0
pessoaMaior = pessoaMenor = ''
while True:
    #Coletando os dados
    pessoa.append(str(input('Nome: ')))
    pessoa.append(float(input('Peso: ')))

    #Analisando os dados
    for p in cadastro:
        if p[1] > maiorPeso or maiorPeso == 0:
            maiorPeso = p[1]
            pessoaMaior = p[0]
        if p[1] < menorPeso or menorPeso == 0:
            menorPeso = p[1]
            pessoaMenor = p[0]
    
    cadastro.append(pessoa[:])
    pessoa.clear()

    escolha = str(input('Quer continuar? [S/N] ')).upper()[0]
    if 'N' in escolha:
        break
print(f'''Total de pessoas cadastradas: {len(cadastro)}
O maior peso foi {maiorPeso}kg. Peso de {pessoaMaior}
O menor peso foi {menorPeso}kg. Peso de {pessoaMenor}''')