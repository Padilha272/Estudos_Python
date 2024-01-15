produto = {
    'nome': 'Caneta azul',
    'preco': 2.5,
    'categoria': 'Escritorio',
}
'''
for chave in produto.keys():
    print(chave)
print('\n')
for valor in produto.values():
    print(valor)
print('\n')
for chave,valor in produto.items():
    print(f'{chave}: {valor}')
'''

dc = {
    chave: valor.upper()
    if isinstance(valor,str) else valor
    for chave, valor 
    in produto.items()
    if chave != 'categoria'
}

lista = [ 
    ('a','valor a'),
    ('b','valor a'),
    ('b','valor a'),
]

'''
dc = {
    chave: valor
    for chave, valor in
    lista
}
'''

#print(dict(lista))

s1 = {2 ** i for i in range(10) }
print(s1)