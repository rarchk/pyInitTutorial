Python Co routines 
=== 
- python 3.5 

async def greet(name):
	return 'hey '+name 

g = greet('Guido') # a courotine function that will be needed to be managed by another function.

import asyncio 
loop=asyncio.get_event_loop()
loop.run_until_complete(g);


async def h():
	names =[1,2,3]
	for name in names:
		print(await greeting(name)) # one coroutine can call another 


# Echo server 
nc localhost 25000 +
		