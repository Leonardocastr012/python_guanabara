#Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
'''– Quantidade de notas
– A maior nota
– A menor nota
– A média da turma
– A situação (opcional)'''

def notas(*num, situação=False):
    #Dicionário
    notas = dict()
    #Transformando em lista
    num = list(num)
    #Pecorrer a lista para informar a quantidade de notas e fazer a soma das notas
    contador = somaDasNotas = 0
    for elemento in num:
        somaDasNotas += elemento
        contador += 1
    notas['Total'] = contador
    #Encontrar o maior e o menor
    notas['Maior'] = notas['Menor'] = 0
    for i in range(0,len(num)):
        if notas['Maior'] == 0 and notas['Menor'] == 0:
            notas['Menor'] = num[i]
            notas['Maior'] = num[i]
        if notas['Maior'] < num[i]:
            notas['Maior'] = num[i]
        if notas['Menor'] > num[i]:
            notas['Menor'] = num[i]
    #Média das notas
    media = somaDasNotas/ contador
    notas['Média'] = media
    #Caso opcional
    if situação == True:
        if media < 7:
            notas['Situação'] = 'Ruim'
        elif 7 <= media <= 8:
            notas['Situação'] = 'Boa'
        else:
            notas['Situação'] = 'Excelente'
    print(notas)

notas(1,2,3,4,5)
notas(9.9,9.5,10,9,8, situação=True)
