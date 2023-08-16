'''
len - Return the number of keys
keys - Iterable with keys
values - Iterable with values
items - Iterable with keys and values
setdefault - Add a value if the key does not exist
copy - Return a shallow copy
get - Get a key
pop - Erase an item with a especific key
popitem - Erase the last added item
update - Updates a dictionary with another 
'''

pessoa = {
    'nome':'Luiz Otávio',
    'sobrenome':'Miranda',
    'idade':900,
}

pessoa.setdefault('idade', 0)
print(pessoa['idade'])


#print(len(pessoa))
#print(list(pessoa.keys()))
#print(list(pessoa.values()))
#print(list(pessoa.items()))

# for valor in pessoa.values():
#     print(valor)

# for chave, valor in pessoa.items():
#     print(chave , valor)