'''
condicao = True

if(condicao == True):{
    print('Este é o código do if')
} 
'''

entrada = input('Você quer "entrar" ou "sair" ? ')

if entrada == 'entrar':
    print('Você entrou no sistema')
elif entrada =='sair':    
    print('Você saiu do sistema')
else:
    print('Você não digitou nem entrar nem sair.')