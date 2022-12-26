a = 'A'
b = 'B'
c = 1.1325235325
string = 'a={0} b={1} c={2:.2f} d={2:.2f}'
formato =string.format(a,b,c)

'''
parametro nomeado
a = 'A'
b = 'B'
c = 1.1325235325
string = 'a={nome1} b={nome2} c={nome3:.2f} d={nome3:.2f}'
formato =string.format(nome1=a,nome2=b,nome3=c)
'''

print(formato)
print("'Já sei'")