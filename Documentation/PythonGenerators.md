Generators in python 
=== 
Everything that for loop does is iterate over an iterable object. 
Now an iterable object can be a list dictionary tuple or set, or it can be a generator function 

generator function is kind of in suspending state until you starts iterating on it.
customize iteration with genertors or generator expression 


function has suspended on yield 

__iter__()
__next__()

stop iteration 

with open(filename) as f: 
	for line in f:
		if pattern in line: 
			yield line; 

for line in a generator function 

s = (x*x in nums)

with generators, you could throw away after using them and they can be only used once, but with the use of class you might use them again and again 

class Countdown(object):
	def __init__(self,start):
		self.start=start # turns out that you can define self in this way 

	def __iter__(self):
		n=self.start; 
		while n>0:
			yield n 
			n -= 1 

for c in Countdown(5)	 # with this you can repeteadly call and call this generator function

## good for real time data processing 
print "{:>10s} = {:10.3f}".format(a,b) # complex printing mechanisms 

# processing pipeline and other frameworks 




