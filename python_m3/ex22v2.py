list_alt = []
list_num = []
menor = maior = 0
for i in range(5):
    num = int(input('Digite seu número: '))
    list_num. append (num) # Coloca na lista os elementos
    alt = int(input('Digite sua altura em cm: '))
    list_alt. append(alt) # Coloca na lista os elementos
    if list_alt[i] < menor or menor == 0: # Vai executar quando a lista tiver um elemento menor que o armazenado em menor
        menor = list_alt[i]
        num_menor = list_num[i] # Vai pegar o número digitado pelo usuário no mesmo loop que pega a altura(que está acontecendo acima)
    if list_alt[i] > maior or maior == 0: # Vai executar quando a lista tiver um elemento maior que o armazenado em maior
        maior = list_alt[i]
        num_maior = list_num[i] # Vai pegar o número digitado pelo usuário no mesmo loop que pega a altura(que está acontecendo acima)
print(f'''A menor altura foi {menor}cm e seu número: {num_menor}
A maior altura foi {maior}cm e seu número: {num_maior}''')