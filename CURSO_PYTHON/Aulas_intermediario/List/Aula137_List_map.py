produtos=[
    {'nome':'p1','preco':20,},
    {'nome':'p2','preco':10,},
    {'nome':'p3','preco':30,},
]
novos_produtos=[
    {**produto,'preco':produto['preco']*1.05} 
    if produto['preco']>20 else {**produto}
    for produto in produtos
]

produtos_quadrados=list(map(lambda produto:produto['preco']**2,produtos))
##print(novos_produtos)
print(*novos_produtos, sep='\n')
print(produtos_quadrados)