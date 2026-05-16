# Autor: Luan oliveira
# projeto: condicionais

# definicao de variaves
nome = input('Digite seu nome')
idade = int(input('Digite sua idade'))
cidade = input('Digite sua cidade')
carteira = str(input('voce possui carteira de motorista?(sim ou nao)'))
if  carteira == 'sim':
    print('voce pode dirigir!')
else:
    print('voce nao pode dirigir')