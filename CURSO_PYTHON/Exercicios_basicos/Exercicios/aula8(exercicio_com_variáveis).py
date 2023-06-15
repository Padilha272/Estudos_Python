nome = input('Digite o seu nome:')
sobrenome = input('Digite o seu sobrenome :')
idade = input('Digite a sua idade: ')
idade_final=int(idade)
ano_de_nascimento=input('Digite o seu ano de nascimento: ')
ano=int(ano_de_nascimento)
maior_de_idade=idade_final>=18
altura=input('Digite a sua altura: ')
altura_final=float(altura)

print('Nome: ',nome)
print('sobrenome: ',sobrenome)
print('Idade: ',idade_final)
print('É maior de idade? ',maior_de_idade)
print('Ano de nascimento: ',ano)
print('Altura em metros: ',altura_final)


