nome = input('Digite o seu nome: ')
idade = input('Digite a sua idade: ')

if( nome == '' or idade ==''):{
    print("Desculpe, você deixou campos vazios")
}

else:
    
    print(f'O seu nome é: {nome}')
    print(f'O seu nome invertido é: {nome[::-1]}')
    if(' ' in nome):{
    print('O seu nome contém espaços')
    }
    else:{
    print('O seu nome não contém espaços')
    }
    print(f'O seu nome contém {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A ultima letra do seu nome é {nome[-1]}')

