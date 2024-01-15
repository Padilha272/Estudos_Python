def divisionFN(x,y):
    return x/y

def multiplyFn(x,y):
    return x*y

def exponentiationFn(x,y):
    return x**y

numbers = [1,2,3,4,5]
# novos_numeros =numeros.copy()
# novos_numeros[0]=20
# print(numeros)
# print(novos_numeros)
division = [divisionFN(number,2) for number in numbers]
multiply = [multiplyFn(number,2) for number in numbers]
square = [exponentiationFn(number,2) for number in numbers]
print(numbers)
print(division)
print(multiply)
print(square)