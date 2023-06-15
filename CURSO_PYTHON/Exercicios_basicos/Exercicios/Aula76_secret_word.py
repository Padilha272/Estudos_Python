'''
My solution:
palavra = 'girafa'
mascara = '******'
tentativa=0
i=0 
while True:
    print(f'Tentativa {tentativa} x')
    letra=input("Digite uma letra: ")
    tentativa+=1
    if len(letra)>1:
        print('Digite apenas uma letra')       
    else:
        while i< len(palavra):      
            if palavra[i] == letra:
                mascara = mascara[:i]+letra+mascara[i+1:]
            i+=1
                    
        print(mascara)
        i=0
        if mascara == palavra:
            break
print('VOCÊ GANHOU! PARABÉNS!')
print("Tentativas: ",tentativa)
'''
#Video solution:
import os

palavra_secreta = 'perfume'
letras_acertadas=''
numero_tentativas = 0

while True:
    
    letra_digitada = input("Digite uma letra:")
    numero_tentativas +=1
    if len(letra_digitada)>1:
        print('Digite apenas uma letra')
        continue
    
    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada
    
    palavra_formada=''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
    print(f'{palavra_formada = }')   
    
    if palavra_formada == palavra_secreta:
        os.system('cls')
        print('VOCÊ GANHOU!!! PARABÉNS!')
        print('A palavra era: ',palavra_secreta)
        print('Tentativas: ',numero_tentativas)
        letras_acertadas=''
        numero_tentativas=0
        
