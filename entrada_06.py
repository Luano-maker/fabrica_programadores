# autor: Luan Oliveira
# Projeto: IMC com input e f-string

# Declaracao de variaveis
peso = float(input('digite seu peso: '))
altura = float(input('digite sua altura: '))
IMC = peso / (altura * altura)

# exibindo os resultados
print(f'Seu IMC é: {IMC:.2f}')