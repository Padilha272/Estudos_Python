# add_lambda = lambda x,y: x+y
# result=add_lambda(2,2)
# print(result)

# names = ['Abigail','Joseph','Bob','Natan','Carl']
# sorted_names = sorted(names , key = lambda name: name)
# print(sorted_names)

def sum(parameter):
    return lambda x : x+parameter
f=sum(32)
print(f(3))
f=sum(42)
print(f(1))
