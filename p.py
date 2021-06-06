my_dict = {9: 'two', 5:'three', 4:'four'}
d = my_dict


print(d)
print(d.keys())
print(d.values())
print(d.items())
print(d[4]) # by using get()
print(d.get(7, 'Is not a key'))
print(d.setdefault(7, 'seven'))
print(d)
print(d.pop(5))#rm & retn ele
print(d.popitem())#rm&rt k-v
k = ['apple', True]
n_d = dict.fromkeys(k, 5)
#print(n_d)
sd = {'apple': 9, True: 'boolen'}
u_d = {"orange": 8, True: 10}
print(sd)
print(u_d)
u_d.update(sd)
print(u_d);print(sd)

c_d = u_d.copy()
c_d[True] = 20
c_d['orange'] = 100
print(c_d)
print(len(c_d))
print(my_dict)
print(sorted(my_dict))


#for n in my_dict:
#	print("key is %s and value is %s." % (n, my_dict[n]))
print('----------------------------------')

lst_of_tuple = [('name', 'Jim'), ('age', 35)]
newdict = dict(lst_of_tuple)
d = ['a', 'b']
n = enumerate(d)
#print(dict(n))
#print(dict(list(n))) # enum
#print(dict.fromkeys(d, 3))# fk
#print(newdict) # dict()

# using lst comp
d = {x: x*2 for x in range(1,13) if x % 3 == 1}
#print(d)
com = {
 	'dada': {'name':'Jim', 'salary': 30},
 	'sasa': {'name': 'Tim', 'salary': 9}
}
print(com['dada']['name'])
#d = [(k,v) for k,v in com.items()]
#print(d[0])
#print(d[0][1].values())
#s = d[1][1]
#print(s['salary'])
#print(d[1][1].keys())
g = [(k,v) for k,v in com.items() if any(y for y in com[k] if y == 9)]
#print(g)  # ?

#number = int(input('Enter a num: '))
# initialize total and counter

#total = 0
#c = 1
#new_lst = []
#while c <= number:
#	total += c
#	c += 1
#	new_lst.append(c)
#print('The total is ', total)
#print(new_lst)

# for loop
animals = ['lion', 'tiger', 'monkey', 'sloth', 'elephant']

#for name in animals:
#	if name == 'sloth':
#		continue
#	print('Cool animal: ', name)
#print('Amezing animals!')

#c = 0
#while c <= len(animals) -1:
#	name = animals[c]
#	#print(name)
#	c += 1
#	if name == 'sloth':
#		continue
#	print('Cool animal: ', name)
#print('Amezing animals!')
#print(len(animals))

#import math
# this is infinite loop
#while True:
#	num = int(input('Enter a number: '))
#	
#	print('The square root of number is: ', math.sqrt(num))

letters ='ABCDEFGHIJKLMNOPRSTVUWSYZabcdefghijklmnopqrstvwxwz'

#while True:

#	l = input('Please, enter a letter: ')
#	if l in letters:
#		break
#	print('That is not a letter. Please, try again.')
#print('Perfect!')

import random

#while True:
#	input('Enter a num: ')
#	number = random.randint(1,20)
#	print('Yoy got', number)
#	
#	choice = input('Do you want to play again? (y/n) ')
#	if choice == 'n':
#		break


def greet(name):
	'''greet the person 
use as argument'''
	
	print('Hello,', name)
	print(greet.__doc__)
	
#greet('Tim')

# return s value
def absolute_v(number):
	if number >= 0:
		return number
	else:
		return  - number
		
#print(absolute_v(100))
#print(absolute_v(-12))
#print(absolute_v(-50))

def even_n(number):
	if number % 2== 0:
		return number
	else:
		print('Sorry, the number is not even.')
		
#print(even_n(22))
#print(even_n(13))

def stringprinter(str):
	print(str)
	
#stringprinter('I am tanimu saadu')

def class_sum(num):
	return num * 3
	
def school_sum(m):
	return class_sum(m) + 3
	
#print(school_sum(5))

Mark = {
    'Name': 'Mark Spark',
    'Quizzes': [89.0,80.0,95.0],
    'Homework': [80.0,75.0,90.0],
    'Recitation': [90.0,90.0,75.0],
    'Test': [80.0,95.0]
}
Selen = {
    'Name': 'Selen Job',
    'Quizzes': [69.0,80.0,75.0],
    'Homework': [80.0,75.0,90.0],
    'Recitation': [90.0,90.0,75.0],
    'Test': [90.0,95.0]
}
Shane = {
    'Name': 'Shane Taylor',
    'Quizzes': [60.0,70.0,75.0],
    'Homework': [70.0,75.0,90.0],
    'Recitation': [70.0,80.0,75.0],
    'Test': [90.0,80.0]
}

def average(number):
	total = sum(number)
	result = total/len(number)
	return result
	
def get_average(student):
	Quizzes = average(student['Quizzes'])
	Homework = average(student['Homework'])
	Recitation = average(student['Recitation'])
	Test = average(student['Test'])
	print(student['Name'])
	
	return .2*Quizzes + .1*Homework +.3*Recitation + .4*Test
	

#print(get_average(Mark))
#print('-----------------')
#print(get_average(Selen))
#print('-----------------')
#print(get_average(Shane))

# lambda function
square = lambda x: x ** 2
#print(square(2))
upper = lambda: 'hello world'.upper()
#print(upper())

# map and lambda funcs
s = [2,3,4]
x = list(map(lambda x: x**2, s))
y =list(filter(lambda x: x % 2==0, s))
#print(y)

def factorial(num):
	if num == 1:
		return 1
	else:
		return num * factorial(num-1)
		
#print(factorial(7))