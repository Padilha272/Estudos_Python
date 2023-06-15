'''
split - Used to divide a string
join - Used to Unite a string
'''

frase = '   Olha só    , que coisa interessante     '
lista_frases_cruas = frase.split(',')

lista_frases =[]
for i, frase in enumerate(lista_frases_cruas):
    lista_frases.append(lista_frases_cruas[i].strip())

#print(lista_frases_cruas)
#print(lista_frases)

frases_unidas = ', '.join(lista_frases)
print(frases_unidas)