

'''
salas = [['Maria', 'Helena'] , ['Elaine'],['Luiz','joão','Eduarda',(0,10,20,30,40)]]
print(salas[1][0])
print(salas[0][1])
print(salas[2][2])
print(salas[2][3][3])
'''

salas = [['Maria', 'Helena'] , ['Elaine'],['Luiz','joão','Eduarda']]
for sala in  salas:
    print(f'a sala é {sala}')
    for aluno in sala: 
        print(aluno)

