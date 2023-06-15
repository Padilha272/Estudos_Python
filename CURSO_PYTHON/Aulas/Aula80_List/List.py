'''
#Aula80


#Aula81
lista = [10,20,30,40]
#lista[2] = 300
#print(lista)
#print(lista)
#print(lista[2])
lista.append(50)
lista.pop()
lista.append(60)
lista.append(70)
ultimo_valor = lista.pop()
print(lista, "Removido: ",ultimo_valor)

Methods:
append- Add an item in the end of the list
insert- Add an item with chosen index
pop- Remove an item in the final or with an chosen index
del- Delete an index
clear- Clear the list
extend- Extend the list
+- Concatenate the list  

#Aula82
lista = [10,20,30,40]
lista.append('Luiz')
nome = lista.pop()
lista.append(1233)
del lista[-1]
#lista.cleear()
lista.insert(0,5)
'''
#Aula 83
lista_a = [1,2,3]
lista_b = [4,5,6]
lista_c = lista_a + lista_b
lista_d = lista_a.extend(lista_b)
print(lista_a)
'''
lista_a = [1,2,3]
lista_b = [4,5,6]
lista_c = []
for i in range(0,3,1):
    lista_c.insert(i,lista_a[i] + lista_b[i])
print(lista_c)
'''

