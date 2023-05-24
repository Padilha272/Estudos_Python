#range -> range(start,stop,step)

numeros = range(0,100,1)

for numero in numeros:
    if numero %3 ==0:
        print(numero)