
inicio = int(input('digite a tabuada desejada:'))
fim = int(input('digite o final: '))
for i in range(inicio, fim+1):
    print(f'{inicio} x {i} = {inicio * i}')