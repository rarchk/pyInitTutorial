Python functions as data 
=== 
function is an object. You can put it in dictionaries and you can put it in list. 

def add(x,y):
	def do_add():
		print() '{} {} ->{}'.format(x,y,x+y));
		return x+y
	return do_add 
	
# closure, when you define an internal function, it captures variable that it needs. 

after(10,add(2,3)); 		 