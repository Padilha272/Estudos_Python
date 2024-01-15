string = 'Matheus Padilha'
numero_de_letras = 1
#nova_string = [ letra for letra in string]
nova_string='.'.join([ 
    string[indice:indice+numero_de_letras] 
    for indice in range(0,len(string),numero_de_letras)])
print(nova_string)