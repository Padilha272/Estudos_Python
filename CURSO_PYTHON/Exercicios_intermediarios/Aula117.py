def multiplicar(multiplicador):
    def calculo(num):
        return num*multiplicador
    return calculo

duplicar = multiplicar(2)
triplicar = multiplicar(3)
quadruplicar = multiplicar(4)

print(duplicar(2))
print(triplicar(2))
print(quadruplicar(2))