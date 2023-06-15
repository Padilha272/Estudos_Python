'''
#Minha solução:
import os
lista=[]
faca = 0
i=0

while faca == 0:   
    print('1-Inserir 2-Apagar 3-Listar 4-Sair', end="\n\n")
 
    valor = input("Olá, o que gostaria ?")
    print()
    
    
    match valor:
        case "1":
            item = input("Digite o nome do item: ")
            lista.insert(i,item)
            i+=1
            print()   
        case "2":           
            chave = 0          
            if lista ==[]:
                print('lista vazia!')
                continue    
            for indice,nome in enumerate(lista):
                    print(indice,nome)
            
            while chave ==0:
                
                try:
                    apagar = input("Digite o indice do numero que gostaria de excluir:")
                    apagar_int = int(apagar)
                    lista.pop(apagar_int)
                    chave=1
                except:
                    print("Indice inválido!")
                    continue
                
                print() 
        case "3":
            if lista !=[]:
                for indice,nome in enumerate(lista):
                    print(indice,nome)
            else:
                print("Sua lista está vazia!")
            print() 
        case "4":
            break
        case _ :
            print("Opção inválida")
            print() 

'''
#Solução do curso:
import os

lista = []

while True:
    print("Selecione uma opção:")
    opcao = input('[i]nserir [a]pagar [l]istar:')

    if opcao == 'i':
        os.system('cls')
        valor = input("Digite um valor: ")
        lista.append(valor)

    elif opcao == 'a':
        os.system('cls')
        indice_str = input("Escolha o indice para apagar:")
        for index,nome in enumerate(lista):
                print(index,nome)
        try:
            indice = int(indice_str)
            del lista[indice]
        except IndexError:
            print("Indice não existe na lista") 
        except ValueError:
            print("Por favor, digite um numero inteiro")
        except:
            print("Erro desconhecido")
    elif opcao == 'l':
        
        

        if len(lista) == 0 :
            print("Nada a listar")
        else:
            for index,nome in enumerate(lista):
                print(index,nome)
        
    else:
        print('Por favor, escolha i, a ou l.')
    