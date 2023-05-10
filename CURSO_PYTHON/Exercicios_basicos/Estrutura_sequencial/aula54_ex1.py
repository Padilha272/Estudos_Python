numero = input("Digite um número: ")

''' 

try:
    numero_int = int(numero)
    if numero_int%2 ==0:
        print(f"O número {numero_int} é par")
    else :
        print(f"O número {numero_int} é impar")
except:
    print(f"{numero} não é um número inteiro")   


'''
if numero.isdigit():
    numero_int = int(numero)
    par_impar = numero_int%2 ==0
    par_impar_texto = 'Impar'
    if par_impar:
        par_impar_texto ='par'
    print(f'O número {numero_int} é {par_impar_texto}')

else:
    print(f"{numero} não é um número inteiro")        