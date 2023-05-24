frase = 'O Python é uma linguagem de '\
'programação multiparadigma. Python foi '\
'criado por Guido van Rossum'

i = 0 
maior = 0
letra_que_apareceu_mas_vezes =''
while i < len(frase):
    letra_atual = frase[i]
    qtd_atual = frase.count(letra_atual)
    
    if letra_atual == ' ':
        i+=1
        continue
    '''
    Instead of using the 'continue' you could add another condition in the if method below.
    Ex: if quantas_vezes_letra_apareceu > maior and letra_atual != ' ':
        maior = quantas_vezes_letra_apareceu
        letra_que_apareceu_mas_vezes = letra_atual
     
    '''
    if qtd_atual > maior :
        maior = qtd_atual
        letra_que_apareceu_mas_vezes = letra_atual
    
    
    
    print(letra_atual, qtd_atual)
    i+=1


print(f'{maior}, {letra_que_apareceu_mas_vezes}')