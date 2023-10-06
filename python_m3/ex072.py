lista_num = []
lista_alt = []
for c in range (10):
    num_aluno = int(input('Digite seu número: '))
    lista_num.append(num_aluno) # Coloca na lista os elementos
    alt_aluno = int(input('Digite sua altura em cm: '))
    lista_alt.append(alt_aluno) # Coloca na lista os elementos
lista_alt_crescente = sorted(lista_alt)
print(f'A menor altura é {lista_alt_crescente[0]}cm e maior altura é {lista_alt_crescente[-1]}cm')# Aqui ele pega primeir0 e o ultimo elemento
pos_alt_menor = lista_alt.index(lista_alt_crescente[0]) # Aqui ele vai encontar a posição do elemento na lista_alt que está na ordem que o usuário colocou  e o parametro é o lista_alt_crescente[0](o elemento que quer encontrar)
pos_alt_maior = lista_alt.index(lista_alt_crescente[-1])
print(f'O número do menor em altura é {lista_num[pos_alt_menor]} e o maior é {lista_num[pos_alt_maior]}')