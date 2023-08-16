'''
#Ex1
def multiplicacao(*args):
    mult = 1
    for numero in args:
        mult *= numero
    return mult

valor = multiplicacao(1,2,3,4,5)
print(valor)
'''

#Ex2

def par_impar(num):
    if num ==0:
        return f'O número é zero.'
    elif num % 2==0:
        return f'O número {num} é par.'   
    return f'O número {num} é impar.'

print(par_impar(3))
