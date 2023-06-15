'''
lista = ['Maria','Helena','Luiz']
i = 0
for nome in lista:
    print(nome,f'indice: {i}')
    i+=1


#Exercise:
lista = ['Maria','Helena','Luiz']
indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice])


#Empacotamento e desempacotamento
nome1 , *resto = ["Maria", "Helena","Luiz"]
print(nome1, resto)
'''
#Tuple - An immutable list, is used when you don't need to change the values of the list.
nomes = 'Maria','Helena','Luiz'
# Alternative way : nomes = ('Maria','Helena','Luiz')
print(nomes[0])
print(nomes)
#Turn the list into a tuple:
exemplo = ['Carlos','Manuel','Ana']
exemplo = tuple(exemplo)
print(exemplo)
#Turn the tuple into a list:
exemplo = list(exemplo)
print(exemplo)


