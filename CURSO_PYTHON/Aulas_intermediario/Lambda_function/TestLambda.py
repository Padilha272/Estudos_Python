'''

def sum (*args):
    result=0
    for number in args:
        result +=number
    return result
print(sum(10+20+30+40))


sum = lambda x,y:x+y
print(sum(3,4))
numbers=[1,2,3,4,5,6,7,8]
even_numbers=list(filter(lambda x:x%2==0,numbers))
print(even_numbers)


#1st Test:
numbers=[]
for i in range(1,4,1):
    number = input(f"{i}-) Please, type a number:")
    int_number=int(number)
    numbers.append(int_number)
print(numbers)
odd_numbers = list(filter(lambda x:x%2!=0,numbers))
print(odd_numbers)


#2nd Test:
names=['Bruno','Alice','Abel','Lucia','Carolina']
names.sort()
print(names)

#3rd Test:
numbers=[1,2,3,4,5]
squared_numbers=list(map(lambda x:x**2,numbers))
print(squared_numbers)

#4th Test:
words = ['apple','banana','cherry','donuts','garlic']
words.sort(key=lambda x: x,reverse=True)
print(words)

#5th Test:
number_list=[1,20,13,8,7]
lista=list(filter(lambda x: x>10,number_list))
print(lista)
lista_sum=list(map(lambda x: x+1,number_list))
print(lista_sum)


#6th Test:
def executa(funcao,*args):
    return funcao(*args)
    

soma = lambda x,y : x+y
print(executa(lambda x,y : x+y,2,3))
'''
def executa(funcao,*args):
    return funcao(*args)

duplica  = executa(lambda m : lambda n : n*m,2)
print(duplica(5))

print(
    executa(
        lambda *args : sum(args),1,2,3,4,5

    )
)