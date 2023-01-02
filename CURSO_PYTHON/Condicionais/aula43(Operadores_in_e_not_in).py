nome = 'Otávio'
#print(nome[2])
#print(nome[-4])
#print('vio' in nome)
#print('zero' in nome)
#print(10*'-')
#print('vio' not in nome)
#print('zero' not in nome)

nome = input('Digite o seu nome:')
encontrar = input('Digite o que você quer encontrar: ')

if(encontrar in nome):{
    print(f'{encontrar} está em {nome}')
}
else:{
    print(f'{encontrar} não  está em {nome}')
}
