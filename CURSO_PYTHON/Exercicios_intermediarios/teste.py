lista=[[1,2,3,4,5,6,7,8,9,10],[11,12,13,14,15,16,17,18,19,20]]

def pares_em_uma_lista(lista):
    pares=set()
    for sublista in lista:
        for numero in sublista:
            if (numero%2==0):
                pares.add(numero)
        print(sublista)
    print(pares)    
pares_em_uma_lista(lista)
