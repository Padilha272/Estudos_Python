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
            print(perguntas[i]['Opções'][j])