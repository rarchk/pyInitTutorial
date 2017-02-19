#!/usr/bin/env python3
__author__ = 'Ronak Kogta<rixor786@gmail.com>'
__description__ = \
''' Splits the file into smaller files '''

import argparse;
import sys;
import os;  

if __name__ == '__main__':

	parser = argparse.ArgumentParser(description = __description__);					# parsing arguments 		
	parser.add_argument('-i','--input', help='input file to split', required=True);
	parser.add_argument('-n','--nlines', help='number Of lines in each split file', required=True);
	parser.add_argument('-s','--suffix', help='suffix for new split files',default='part');
	args = parser.parse_args();

	with open(args.input,'r') as f:
		CHUNK_SIZE = int(args.nlines);
		INPUT_FILE = args.input; 
		EXIT_FLAG = 0;
		PARTITION_COUNT = 1;
		iterFile = iter(f);
		
		while (True):
			chunk_index = 0;
			NEW_SPLIT_FILE = "{}-{}{}{}".format(str(INPUT_FILE.split('.')[0]),\
			args.suffix, PARTITION_COUNT, str("."+args.input.split('.')[1]));
			 
			with open(NEW_SPLIT_FILE,'w') as fw:
				while (chunk_index != CHUNK_SIZE):
					try:
						fw.write(next(iterFile));
					except: 
						EXIT_FLAG = 1;					# End of file  
						break;	
					chunk_index += 1;	 
			
			if (EXIT_FLAG and chunk_index == 0):		# Last part of file, and if empty 
				os.remove(NEW_SPLIT_FILE);
				break;

			print ("Writing %s" % NEW_SPLIT_FILE);	
			PARTITION_COUNT += 1;	 	  	
			


		



