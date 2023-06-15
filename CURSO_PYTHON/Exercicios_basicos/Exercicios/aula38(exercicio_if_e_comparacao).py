num1 = input("Primeiro valor: ")
num2 = input("Segundo valor: ")

float_num1 = float(num1)
float_num2 = float(num2)

if num1 > num2 : 
    print(f'{float_num1=} é maior que {float_num2=}')
elif num2 > num1 :    
    print(f'{float_num2=} é maior que {float_num1=}')
else:
    print(f'{float_num1=} é igual a {float_num2=}')    