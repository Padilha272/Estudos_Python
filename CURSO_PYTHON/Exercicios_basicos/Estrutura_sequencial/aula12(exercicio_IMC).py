nome=input('Digite o seu nome: ')
altura=input('Qual a sua altura ? ')
altura_float=float(altura)
peso=input('Qual o seu peso ? ')
peso_float=float(peso)
imc = peso_float/(altura_float**2)
print(nome,' tem ',altura_float,' de altura, pesa ',peso_float,' quilos e seu IMC é ',imc)