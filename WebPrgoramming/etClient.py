#!/usr/bin/env python
__author__ = 'Ronak Kogta<rixor786@gmail.com>'
__description__ = \
''' Edge triggered Echo Client'''

import os;
import sys;
import socket;
import select;
import argparse; 

def parseconfig(configure_options):
	configure_options.add_argument('-p','--port', help='Enter port number of server', default=8001);
	configure_options.add_argument('--host', help='Enter host name of server', default='localhost');

def connect(host,port):
	servSock = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
	try:
		servSock.connect((host,port));
		servSock.setblocking(0);
		print ('Connected to remote host. You can start sending messages');
	except:
		print ("Failed to connect to server at %s:%d" % (host,port,));
		sys.exit();
	return servSock;	

def handle_read_events(fileno,servSock):
	try:
		while True:
			if fileno == servSock.fileno():
				response = servSock.recv(1024);
				  
				if (len(response) == 0):
					epoll.modify(fileno, select.EPOLLET);
   					servSock.shutdown(socket.SHUT_RDWR);
   					print ('<disconnect> %s' % (fileno,));
					break;
				
				print (response),; 
				sys.stdout.flush();
			else:
				request=sys.stdin.readline();sys.stdout.flush();
				servSock.send(request);
				break;
	except socket.error:
		pass;

if __name__ == '__main__':
	configure_options = argparse.ArgumentParser(description = __description__);
	parseconfig(configure_options);
	args = configure_options.parse_args();

	servSock = connect(args.host,int(args.port));
	epoll = select.epoll();

	# Creating Epoll for read events from server and standard input 
	epoll.register(servSock.fileno(), select.EPOLLIN | select.EPOLLET);
	epoll.register(sys.stdin, select.EPOLLIN | select.EPOLLET);
	
	while(1):
	      events = epoll.poll(1);
	      for fileno, event in events:
	      	# If server is read ready  
			if event & select.EPOLLIN:
				handle_read_events(fileno,servSock);
			 
			elif event & select.EPOLLHUP:
				#print "hangup event"
				epoll.unregister(fileno)
				servSock.close()
				del servSock
				sys.exit()
