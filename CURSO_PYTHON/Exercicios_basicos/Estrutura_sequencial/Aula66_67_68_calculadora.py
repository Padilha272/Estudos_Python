#Calculadora com while

#Solução 1:
'''
while True:
    numero_1 = input("Digite um número: ")
    numero_2 = input("Digite outro número: ")
    operador = input("Digite o operador (+-/*): ")

    try:
        numero_1_float = float(numero_1)
        numero_2_float = float(numero_2)

        match operador:
            case '+':
                print("Soma: ",(numero_1_float+numero_2_float))
            case '-':
                print("Subtração: ",(numero_1_float-numero_2_float))
            case '*':
                print("Multiplicação: ",(numero_1_float*numero_2_float))
            case '/':
                print("Subtração: ",(numero_1_float/numero_2_float))
            case other:
                print('Operação inválida')

        sair = input("Quer sair ? [s]im: ").lower().startswith('s')
        
        
        if sair is True:
            break

    except:
        print('Valores inválidos')
'''

#Solução 2:

while True:
    numero_1 = input("Digite um número: ")
    numero_2 = input("Digite outro número: ")
    operador = input("Digite o operador (+-/*): ")
    numero_1_float = 0
    numero_2_float = 0
    numeros_validos = None

    try:
        numero_1_float = float(numero_1)
        numero_2_float = float(numero_2)
        numeros_validos = True

    except:
        numeros_validos = None

    if numeros_validos is None:
       print('Um ou ambos os números digitados são válidos.')
       continue

    operadores_permitidos = '+-*/'
    if operador not in operadores_permitidos:
        print("Operador inválido.")
        continue
    
    if len(operador)>1:
        print("Digite apenas um operador.")
        continue
    
    match operador:
            case '+':
                print("Soma: ",(numero_1_float+numero_2_float))
            case '-':
                print("Subtração: ",(numero_1_float-numero_2_float))
            case '*':
                print("Multiplicação: ",(numero_1_float*numero_2_float))
            case '/':
                print("Subtração: ",(numero_1_float/numero_2_float))
            case other:
                print('Operação inválida')
    
    sair = input("Quer sair ? [s]im: ").lower().startswith('s')

    if sair is True:
        break   
        
