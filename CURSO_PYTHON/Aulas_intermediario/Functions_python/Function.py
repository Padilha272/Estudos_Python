# a and b -> Parameters
# 3 and 4 -> Arguments


def conta(a,b):
    print(f'The multiplication between {a} and {b} is equal to: {a*b}')
    
def batman():
    return 'Joker'  

def saudacao(nome='Nimguem'):
    print(f'Olá, {nome}!')

conta(3,4)
conta(2,5)
print(batman())
saudacao('Batman')
saudacao()