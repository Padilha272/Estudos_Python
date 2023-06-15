#Enumerate - Used to enumerate iterables(indexes)
lista = ['Maria','Helena','Luiz']
lista.append('João')
#lista_enumerada = enumerate(lista)

#print(next(lista_enumerada))

''' 
item in enumerate(lista):
    print(item)
lista_enumerada = list(enumerate(lista))

print(lista_enumerada)

''' 

for item in enumerate(lista):
    index, name = item
    print(index,name)
#Alternative way:

#for index, name in enumerate(lista):
    #print(index,name)
