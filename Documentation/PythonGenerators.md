Generators/Iterators in python 
=== 

## Iterators and Iterables 
Lists, tuples and dictionary, sets are said to be iterable in python, so you can for loop them. 

Collections*(lists,tuples..)* apart, any class can be made iterable, if it has two functions implemented. 

-  __getitem__() # for  backward compatability. 
-  __iter__()

So, a basic test for any object to be iterable is to 

```python 
>>> iter(object)
```
It returns an iterator object, if it is iterable otherwise it raises a TypeError. An iterator is something that iterates over an iterable object with the help of 

```python
>>> next(iterObject);
>>> __iter__(iterObject); # Returns itself
``` 
If all elements of an iterable objects are exhausted by next of iterator, then it raises an StopIteration error. Furthermore, it is not possible to reset an iterator, even if you call iter over iterator object, as __iter__ of an iterator object returns itself. 

```python
# simple for loop 
for i in [1,2,3]:
	print (i);

# same loop broken down 
i = iter([1,2,3]);
while True:
	try:
		print (next(i));
	except StopIteration:
		del i; 
		break; 	 	 
``` 

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




