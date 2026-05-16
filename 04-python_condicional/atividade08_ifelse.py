# Autor: Luan oliveira
# projeto: condicionais

# definicao de variaveis
nome = print('Digite seu nome')
peso = float(input('Digite seu peso'))
Altura = float(input('Digite sua altura'))
IMC = peso / (Altura * Altura)
if IMC >= 18.05:
    print('voce esta abaixo do peso')
else:
    print('peso normal ')