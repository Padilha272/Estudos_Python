'''
The word global makes an variable of a extern scope
be the same as a variable with the same name in the intern scope.

We can't access a nome in a intern scope in a extern scope.

'''

x = 1 
def escopo():
    #global x
    #global x is manituplating the x value declared out of the escopo function 
    x = 10 
    def outra_funcao():
        #global x
        x = 11
        y = 2
        print(x, y)
    outra_funcao()
    print(x)

print(x)
escopo()
print(x)