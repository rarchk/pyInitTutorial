Python Classes  
=== 

# Class introduction 

```python 
Class Test(object):
	def __init__(self):
		... 

	@classmethod # kind of construction method 
	def from_string(cls,s); # cls is the class name of owner of that method 	 
```

Python Object system 

- getattr, setattr, delete that attribute. (only operations supported) # useful for writign general code 

h.cost() 

# Magic Methods
These are methods associated with class, where you can overload operators with your logic.   

``` 
- \+ --> __add__(4)
- \* -> __mul__(4)
- a[0] -> a.__getitem__(0)
- a[0]=1 -> a.__setitem__()
```

Other magic methods:

> def __repr__(self):
>	return 'Class name({!r},{!r},{!r},{!r})'.format(self.name,....)
>	you can change the method of representation of objects.

> def __str__(self); # more of printing operation 

repr is meant for programmers, whereas str is for output. 

> __len__ for length of object, __iter__ for for loop	

 

## Resource management in python 

with open("",r) as f: 
	... 

with statement is kind of block statement,  very useful for defining resources 

lock = treading.lock()
with lock: 
	print('Use the lock'); 

# Context manager # with statement  
__enter__(self)		
___exit__(self,ty,val,tx) classs methods  

	