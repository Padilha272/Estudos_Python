s1 = set()
s1.add('Luiz')
s1.add(1)
#You can only add one value per '.add'.
s1.update(('Olá mundo',1,2,3,4))
#s1.clear() - You can use this method to clear your set.
s1.discard('Olá mundo')
s1.discard('Luiz')
print(s1)