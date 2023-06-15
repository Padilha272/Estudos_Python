codigo1 = input('Codigo 1: ')
num1 = int(input('Número de peças 1: '))
valor1 = float(input('Valor unitário 1: '))

codigo2 = input('Codigo 2: ')
num2 = int(input('Número de peças 2: '))
valor2 = float(input('Valor unitário 2: '))

total =(num1*valor1)+(num2*valor2)

print(f'Valor a pagar: {total:,.2f}')