nome = input("Digite o seu nome: ")

if len(nome) >1 :
    if len(nome) <=4:
        print("Seu nome é curto")
    elif len(nome)>=5 and len(nome) <=6: 
        print("O seu nome é normal")    
    else:
        print("O seu nome é muito grande")
else:
    print('Digite mais de uma letra')