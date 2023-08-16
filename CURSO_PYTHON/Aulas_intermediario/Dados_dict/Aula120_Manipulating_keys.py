pessoa = {}

chave = 'nome'

pessoa[chave] = 'Matheus'

pessoa['sobrenome'] = 'Padilha'


print(pessoa[chave])

pessoa[chave] = 'João'

del pessoa['sobrenome']

print(pessoa)
print(pessoa['nome'])

#print(pessoa.get('sobrenome','Não existe'))

if pessoa.get('sobrenome') is None:
    print('Não xiste')
else:
    print(pessoa['sobrenome'])