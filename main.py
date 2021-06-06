class A:
	def __init__(self,name,age):
		self.name = name
		self.age = age
		self.lists = []
		self.lists2 = []
		self.lists3 = []
		
	def change_age(self,age):
		self.age = age
		
	def show_change(self):
		return self.age
		
	def sept_2(self):
		return self.show_change()
		
	def w_on_lst(self):
		l = None
		for l in range(1,8):
			if l %2==0:
				self.lists.append(l)
			elif l%3==0:
				#print('old num')
				self.lists2.append(l)
			elif l%2!=0 and l%3!=0:
				#print('1 and itself can do it')
				self.lists3.append(l)
		return self.lists,self.lists2,self.lists3
				
	def sept3(self):
		return self.w_on_lst()
			
class B(A):
		def __init__(self,name,age, vab):
			self.name = name
			self.age = age
			self.vab = vab
			super().__init__(name,age)
			
		def set(self,a):
			self.age = a
			
		def get(self):
			return self.age
			
def hello():
		def hi():
			return B('Dari',22,'yellow')
		return hi()
		
		
obj = hello()
#print(obj.name,obj.age,obj.vab)
#print(obj.w_on_lst())
		
#obj = hello()
#print(obj.name, obj.age)
#obj.set(50)
#print(obj.get())
#print(obj.w_on_lst())
		
#o = B('jim',20, 'Green')
#print(o.w_on_lst())
#print('I\'m %s and I\'m %s years old and also, %s is my favorate color..' % (o.name, o.age,o.vab))
		
#ob = A('Tim', 35, )
#print(ob.age)
#ob.change_age(25)
#print(ob.w_on_lst())
#ob.sept3()
