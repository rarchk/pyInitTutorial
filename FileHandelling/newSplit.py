#!/usr/bin/env python3
__author__ = 'Ronak Kogta<rixor786@gmail.com>'
__description__ = \
''' Splits the file into smaller files '''

import argparse;  

if __name__ == '__main__':

	parser = argparse.ArgumentParser(description = __description__);					# parsing arguments 		
	parser.add_argument('-i','--input', help='input file to split', required=True);
	parser.add_argument('-n','--nlines', help='number Of lines in each split file', required=True);
	parser.add_argument('-s','--suffix', help='suffix for new split files',default='part');
	args = parser.parse_args();

	with open(args.input,'r') as f:
		chunkSize = int(args.nlines);
		counter = 0;
		checkFlag = 0;
		partition_count = 1; 
		while (True):
			counter = 0;
			splitFile =  ('%s-%s%d%s' % (str(args.input.split('.')[0]), args.suffix, partition_count,\
			str("."+args.input.split('.')[1])));
			
			print ("Writing %s" % splitFile);

			with open(splitFile,'w') as fw:
				while (counter != chunkSize):
					EOFflag = 0;  
					for line in f:						# making file as an iterable object
						fw.write(line);
						print ("writing %s at %d" %(line,counter));
						EOFflag = 1;
						break;
					counter += 1;
					if (EOFflag == 0):
						checkFlag = 1;
						break; 
			
			if (checkFlag == 1): 				# Last part of file 
				break;

			partition_count += 1;	 	  	
			


		



