
'''
input string
inputString = "tutorialsoint"

adding character 'p' at a specific position i.e, at index 9
inputString = inputString[:9] + 'p' + inputString[9:]

printing the resultant string 
print("Adding 'p' at 9th index of an input string:\n", inputString)
'''
nome = input('Digite o seu nome: ')
tamanho_nome = len(nome)

'''


print(nome)
print(tamanho_nome)
nova_string = nome
contador=0

while contador <= 2*len(nome):   
    nova_string = nova_string[:contador] + '*' +nova_string[contador:]
    contador+=2


print(nova_string)
'''
nova_string = ""
contador=0

while contador < len(nome):
    nova_string += f'*{nome[contador]}'
    contador+=1
print(nova_string)

