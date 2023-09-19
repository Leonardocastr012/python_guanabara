#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome “SANTO’’
NomeCidade = str(input('Digite o nome de uma cidade: ')).lower() # Deixa tudo minúsculo para facilitar a comparação
listaNomeCidade = NomeCidade.split() # Separa o nome em elementos de uma lista
'santo' in listaNomeCidade[0] # Aqui vai ver se o primeiro elemenyo da lista é o elemento "santo"
print('santo' in listaNomeCidade[0])