# autor: Luan oliveira

ola = print('seja bem vindo a cafeteria Aroma e Sabor')
nome = input('digite seu nome: ')
print('Escolha o numero do seu pedido: ')
print('1 cafe: ')
print('2 cha: ')
pedido = int(input('digite o numero do seu pedido'))
if pedido == 1:
    print(f'{nome}, seu cafe esta pronto')
else:
    print(f'{nome}, seu cha esta pronto')


