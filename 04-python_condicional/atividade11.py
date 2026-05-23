nome = input('digite seu nome: ')
idade = int(input('digite sua idade: '))
if idade >= 18:
    print('voce é maior de idade')
    cnh = input('voce tem cnh: (sim, nao)')
    if cnh == 'sim':
        print('voce pode dirigir')
    else:
      print('voce nao pode dirigir')
if idade < 18:
    print('voce é menor de idade')