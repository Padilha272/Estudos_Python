pessoa = {
    'nome':'Luiz Otávio',
    'Sobrenome':'Miranda',
    "idade":18,
    'Altura':1.8,
    'Endereços':[
        {'rua':'tal tal','número':123},
        {'rua':'outra rua','número':321},
    ],
}

#pessoa = dict(nome='Luiz Otávio' , sobrenome="Miranda")
#print(pessoa, type(pessoa))
print(pessoa['nome'])
print(pessoa['Sobrenome'])

for chave in pessoa:
    print(chave, pessoa[chave])