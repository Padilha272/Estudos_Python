'''
perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções' :['1','4','5','6'],
        'Resposta':'4',     
     },
     {
        'Pergunta': 'Quanto é 5*5?',
        'Opções' :['25','55','10','51'],
        'Resposta':'25',  

     },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções' :['4','5','2','1'],
        'Resposta':'5',  

    },   
    ]
folha_de_respostas=[]
for i in range (0,3,1):
    print(perguntas[i]['Pergunta'])
    for j in range (0,4,1):
            print(j+1,'-)',perguntas[i]['Opções'][j])

    resposta=input('Digite a sua resposta: ')

    if resposta == perguntas[i]['Resposta']:
        print(f"Você acertou! a resposta é : {perguntas[i]['Resposta']}")
        folha_de_respostas.append(f'{i+1}-)Certo')
    else:
        print(f"Você errou, a resposta é : {perguntas[i]['Resposta']}")
        folha_de_respostas.append(f'{i+1}-)Errado')
    print()
print(folha_de_respostas)


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções' : ['1', '4', '5'],
        'Resposta': '4',     
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções' : ['25', '55', '10', '51'],
        'Resposta': '25',  
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções' : ['4', '5', '2', '1'],
        'Resposta': '5',  
    },   
]

folha_de_respostas = []

def fazer_pergunta(pergunta):
    print(pergunta['Pergunta'])
    print(pergunta['Opções'])
    resposta = input('Digite a sua resposta: ')
    if resposta == pergunta['Resposta']:
        print(f"Você acertou! A resposta é: {pergunta['Resposta']}")
        return 'Certo'
    else:
        print(f"Você errou, a resposta é: {pergunta['Resposta']}")
        return 'Errado'

for i, pergunta in enumerate(perguntas):
    resultado = fazer_pergunta(pergunta)
    folha_de_respostas.append(f'{i+1}-){resultado}')

print(folha_de_respostas)

'''
perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções' : ['1', '3', '4','5'],
        'Resposta': '4',     
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções' : ['25', '55', '10', '51'],
        'Resposta': '25',  
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções' : ['4', '5', '2', '1'],
        'Resposta': '5',  
    },   
]

qtd_acertos=0
for i,pergunta in enumerate(perguntas):
    print(f'Pergunta {i+1}:',pergunta['Pergunta'])
    print()

    opcoes=pergunta['Opções']
    for j,opcao in enumerate(opcoes):
        print(f"{j}) {opcao}")
    print(end="\n\n")
    
    escolha=input('Escolha uma opção: ')


    acertou=False
    escolha_int=None
    qtd_opcoes = len(opcoes)

    if escolha.isdigit():
        escolha_int = int(escolha)

    if escolha_int is not None:
        if escolha_int >=0 and escolha_int< qtd_opcoes:
            if opcoes[escolha_int]==pergunta['Resposta']:
                acertou=True
    print()
    if acertou:
        print('Acertou! ')
        qtd_acertos+=1
    else:
        print('Errou')

    print()

print(f'Você acertou {qtd_acertos} de {len(perguntas)} perguntas.')    


