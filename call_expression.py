class Callee:
	def __call__(self,*args,**kwargs):
		print('Called:', args, kwargs)
		
c = Callee()
#c(1,2, 3)
#c(1,2,3,a=4,b=5)
#d =[3,4]
#e = {'g':'hello'}
#c(1,2,*d, h=6,**e)

class Prod:
	def __init__(self,val):
		self.val=val
	def __call__(self,other):
		return self.val*other
		
class Prod2:
	def __init__(self,val):
		self.val=val
	def comp(self,other):
		return self.val*other
		
x = Prod(3)
y = Prod2(3)
#print(x(3))
#print(y.comp(3))

class CallBack:
	def __init__(self,color):
		self.color=color
		
	def changeColor(self):
		print('turn', self.color)
		
b1 = CallBack('blue')
obj = b1.changeColor
#obj()

#B1 = Button(command=b1)
#B2 = Button(command=b2)

def callBack(color):
		def oncall():
			print('turn',color)
		return oncall
		
cb = callBack('yellow')
#cb()

cb4 = (lambda color="red": 'turn '+color)
#print(cb4())

