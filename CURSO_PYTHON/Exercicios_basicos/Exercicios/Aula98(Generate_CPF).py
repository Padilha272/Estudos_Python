'''
#My Solution
import re

cpf = input("Digite o CPF: ")

parcelas_cpf = re.split(r'[.-]',cpf)

cpf_separado =[]

for i,item in enumerate(parcelas_cpf):
    cpf_separado.append(parcelas_cpf[i].strip())

    print(list(cpf_separado))
    cpf = ''.join(cpf_separado)
    print(cpf)
    contador = 10
    soma = 0
    i=0
if (len(cpf)<11):
        print('Invalid CPF')
else:
    try:
        while i<(len(cpf)-2):
            numero_int = int(cpf[i])
            soma += numero_int*contador
            contador-=1
            i+=1
        print(f"A soma dos valores é {soma}")
        soma = soma*10
        print(f"multiplicar o resultado anterior por 10: {soma}")
        soma = soma%11
        print(f"Resto da divisão por 11: {soma}")
        #print("O resultado é zero " if (soma >9) else "O Primeiro digito é 7")
    except ValueError:
        print("Valor inválido")
    #ValueError
'''

#VideoSolution
'''
import re
import sys

entrada = input('CPF [746.824.890-70]: ')
cpf_enviado_usuario = re.sub(r'[^0-9]','', entrada)

#Alternative method to replace . or - :
#cpf_enviado_usuario = '746.824.890-70'.replace('.','').replace('-','')

entrada_e_sequencial = entrada == entrada[0] * len(entrada)

if entrada_e_sequencial:
    print('Você enviou dados sequenciais')
    sys.exit()

nove_digitos = cpf_enviado_usuario[:9]
'''
import random
import sys

for _ in range(100):
    nove_digitos =''
    for i in range(9):
        nove_digitos += str(random.randint(0,9))


    contador_regressivo_1 = 10 
    soma = 0

    resultado_digito_1 = 0

    for digito in nove_digitos:
        resultado_digito_1 += int(digito)*contador_regressivo_1
        contador_regressivo_1 -=1
    digito_1 = ((resultado_digito_1 * 10) % 11)
    digito_1 = digito_1 if digito_1 <=9 else 0

    dez_digitos = nove_digitos + str(digito_1)
    contador_regressivo_2 =11

    resultado_digito_2 = 0

    for digito in dez_digitos:
        resultado_digito_2 +=(int(digito)*contador_regressivo_2)
        contador_regressivo_2 -=1 
    digito_2 = (resultado_digito_2*10)%11
    digito_2 = digito_2 if digito_2 <=9 else 0

    cpf_gerado_pelo_calculo  = f'{nove_digitos}{digito_1}{digito_2}'

    print(cpf_gerado_pelo_calculo)
