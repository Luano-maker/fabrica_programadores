nome = input('digite seu nome: ')
telefone = input('digite seu numero de telefone: ')
cidade = input('digite sua cidade: ')
salario = int(input('digite seu salario: '))

if salario >= 1000:
    print(f'{nome}, Você possui uma renda boa')
elif salario >= 700:
    print(f'{nome}, voce possui uma renda razoavel')
elif salario >= 500:
    print(f'{nome}, Você possui uma renda baixa')
else:
    print(f'{nome}, voce possui uma renda muito baixa')