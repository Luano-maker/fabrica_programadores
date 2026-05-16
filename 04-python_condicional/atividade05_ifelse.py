# Autor: Luan oliveira
# projeto: condicionais

# definicao de variaveis
nome = input('Digite seu nome')
nota =int(input('Digite sua primeira nota'))
nota2 =int(input('Digite sua segunda nota'))
media = nota + nota2 / 2
media1 = print('Sua media é', media)
if nota >= 6:
    print('aprovado')
else:
    print('reprovado')