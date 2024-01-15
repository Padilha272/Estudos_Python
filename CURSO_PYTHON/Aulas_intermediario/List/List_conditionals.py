numbers=[1,2,3,4,5,6,7,8,9,10]
new_numbers=[number for number in numbers if number>5]
odd_numbers=[number for number in numbers if number%2 != 0]
even_numbers=[number for number in numbers if number%2 == 0]
other_if=[
    number
      if number !=6 else 600 
      for number in even_numbers
]
print(numbers)
print(new_numbers)
print(odd_numbers)
print(even_numbers)
print(other_if)