nome = input('digite seu nome: ')
nota = int(input('digite sua primeira nota: '))
nota2 = int(input('digite sua segunda nota: '))
nota3 = int(input('digite sua terceira nota: '))
media = (nota + nota2 + nota3) / 3
if media >= 7:
    print('Aprovado')
elif media >= 4:
    print('voce esta de recuperacao')
else:
    print('Reprovado')