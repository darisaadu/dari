# function decorator
def print_arg(f):
	def inner_func(*args,**kwargs):
		print(args)
		print(kwargs)
		return f(*args,**kwargs)
	return inner_func

@print_arg
def multiply(num1,num2,**kwargs):
	pass
	
#d = {'1': 5,'2': 10}	
#multiply(3,5,x=2,z="hello world")

def print_arg(f):
	def inner_f(*args,**kwargs):
		print(args)
		print(kwargs)
		return f(*args, **kwargs)
	return inner_f

@print_arg	
def multiply(num1,num2,**kwargs):
	#print(kwargs)
	pass
	
# for cheching type func

import types
from types import MethodType
	
#multiply(3,5,x=3,y=9)
#print(isinstance(multiply, types.FunctionType))
#print(type(multiply))

# class decorator

class Decorator(object):
	def __init__(self, func):
		self.func = func
		
	def __call__(self, *args, **kwargs):
		print('Before decorator')
		res = self.func(*args,**kwargs)
		print('After decorator')
		print(args)
		print(kwargs)
		return res

@Decorator		
def test(x,y,**d):
	print('inside test')

k = {'name': 'tim'}	
#test(2,5, a="hello", **k)

#method decorator

class Decorator(object):
	def __init__(self,func):
		self.func = func
		
	def __call__(self,*args,**kwargs):
		print('Inside the method decorator')
		res = self.func(*args,**kwargs)
		
	def __get__(self, instance,cls):
		return self if instance is None else MethodType(self, instance)
		
		
class Test(object):
		
		@Decorator
		def __init__(self):
			print('inside test ')
		

#a = Test()

# counting instance share the same decorator

class Decorator(object):
	def __init__(self,func):
		self.func = func
		self.ncall = 0
		
	def __call__(self,*args,**kwargs):
		#print('Inside the method decorator')
		self.ncall += 1
		res = self.func(*args,**kwargs)
		
	def __get__(self, instance,cls):
		return self if instance is None else MethodType(self, instance)
				
class Test(object):
		def __init__(self):
			pass
			#print('inside test')
		
		@Decorator	
		def do_something(self):
			return "something was done"



a = Test()
a.do_something()
#print(a.do_something.ncall)
b = Test()
b.do_something()
#print(b.do_something.ncall)


#decorator with abitrary arg
def decoratorfactory(message=[]):
	def decorator(func):
		def wrapped_f(*args,**kwargs):
			print('Decorator want to tell you: {}'.format(message[1::]))
			return func(*args, **kwargs)
		return wrapped_f
	return decorator

@decoratorfactory(message=['Hello World!!!',50,90,55])	
def test():
	pass
	
#test()

# decorator contain argument
def decoratorfactory(*dec_args, **dec_kwargs):
	class  Decorator(object):
		def __init__(self,func):
			self.func = func
			
		def __call__(self,*args,**kwargs):
			print('Decorator argument: {}'.format( dec_kwargs))
			return self.func(*args,**kwargs)
			
	return Decorator
	
@decoratorfactory(a=10)
def test():
	pass
	
#test()

from functools import wraps

# as a func
def decorator(func):
	@wraps(func)
	def wrapped_func(*args,**kwargs):
		return func(*args,**kwargs)
	return wrapped_func
	
@decorator
def test():
	'''hello world.'''
	
#print(test.__doc__)
#print(test.__name__)


# as a class
class Decorator(object):
	def __init__(self, func):
		self._wrapped = wraps(func)(self)
		
	def __call__(self, *args, **kwargs):
		return self._wrapped(*args,**kwargs)	
		
@Decorator
def test():
	'''This is a docstring'''
	pass

#print(test.__doc__)

# create singleton class with decorator
def singleton(cls):
	instance = [None]
	def wrapper(*args,**kwargs):
		if instance[0] is None:
			instance[0] = cls(*args,**kwargs)
		return instance[0]
	return wrapper
	
@singleton
class SomeSingletonClass(object):
	x = 2
	def __init__(self):
		print('Created')
		
#instance = SomeSingletonClass()
#instance = SomeSingletonClass()

#print(instance.x)
#instance.x= 3
#print(instance.x)
#print(SomeSingletonClass().x)



import time

def timer(func):
	def inner(*args,**kwargs):
		t1 = time.time()
		f =func(*args, **kwargs)
		t2 = time.time()
		print('Runtime took {0} seconds'.format(t2 - t1))
		return f
	return timer

@timer	
def test():
	pass
	
#print(test(5))   # ?


# create singleton class with decorator
def singleton(cls):
	instance = [None]
	def wrapper(*args,**kwargs):
		if instance[0] is None:
			instance[0] = cls(*args,**kwargs)
		return instance[0]
	return wrapper
	
@singleton
class SomeSingletonClass(object):
	x = 2
	def __init__(self):
		print('Created')
		
#instance = SomeSingletonClass()
#instance = SomeSingletonClass()
#print(instance.x)
#instance.x= 3
#print(instance.x)
#print(SomeSingletonClass().x)


import time

def timer(func):
	def inner_f(*args,**kwargs):
		t1 = time.time()
		f = func(*args,**kwargs)
		t2 = time.time()
		t3 = t2 - t1
		print('Runtime took {0}, t1 is {1} and t2 is {2}'.format(t3,t1,t2))
		return f
	return inner_f
	
	
@timer	
def test():
	pass
	
#test()







