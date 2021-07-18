class Course(object):
	def __init__(self, name, id):
		self.id = id
		self.name = name
	
if __name__ == '__main__':	
	obj1 = Course('dari', 1)
	obj2 = Course('salim', 2)
	obj3 = Course('jim', 3)
	print(obj1.id)
	print(obj1.name)