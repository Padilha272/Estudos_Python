'''
print(1234)
print(456)
int('a')
'''
numero_str = input('Vou dobrar o numero que vc digitar: ')

try:
    numero_float=float(numero_str)
    print('Float: ', numero_float)
    print(f'O dobro de {numero_str} é {numero_float*2:.2f}')
except:
    print('Isso não é um número')



'''
if(numero_str.isdigit()):

    numero_float=float(numero_str)

    print(f'O dobro de {numero_str} é {numero_float*2:.2f}')

else:

    print('Isso não é um número')

'''



     

