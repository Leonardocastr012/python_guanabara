#Funções 2
def linha():
    print('-'*30)
#Interactive Help
#help()
#print(input.__doc__)

#docstrings
#ex1
linha()
def contador(i,f,p):
    """
    -> Faz uma contagem e mostra na tela.
    Parâmetro i: início da contagem
    Parâmetro f: fim da contagem
    Parâmetro p: passo da contagem
    return: sem retorno
    """
    #docstring
    c = i
    while c <= f:
        print(f'{c}', end=' ')
        c += p
    print('FIM!')
contador(2,10,2)
linha()
help(contador)
#Parâmetros opcionais
#ex2
linha()
def somar(a,b,c=0): #Caso c não tenha valor ele fica com valor 0, o parâmetro opcional pode ser colocado em qualquer parâmetro
    s = a + b + c
    print(f'A soma vale {s}')

somar(3,2,5)
somar(8,4)
linha()    
#Escopo de variáveis
#ex3
def teste():
    x = 8 #Escopo local(só funciona nessa parte, neste caso dentro dessa função)
    print(f'Na função teste, n = {n}')
    print(f'Na função teste, x = {x}')
#Programa pricipal
n = 2 #Escopo global
print(f'No programa principal, n = {n}')
teste()
linha()
#ex4
def função():
    global n1 #nesse caso agora o n1 daqui dentro é o global e o de fora não tem valor
    n1 = 4
    print(f'N1 dentro vale {n1}')
n1 = 2 #Escopo global, mas agora tá sem valor pelo comando global dentro da função
função()
print(f'N1 fora vale {n1}')
#Retorno de resultados

