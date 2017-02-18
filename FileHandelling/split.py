#!/usr/bin/env python3
__author__ = 'Ronak Kogta<rixor786@gmail.com>'
__description__ = \
''' Splits the file into smaller files '''

import argparse;  

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description = __description__);
	parser.add_argument('-i','--input', help='input file to split', required=True);
	parser.add_argument('-n','--nlines', help='number Of lines in each split file', required=True);
	parser.add_argument('-s','--suffix', help='suffix for new split files',default='part');
	args = parser.parse_args();

	with open(args.input,'r') as f:
		lines = f.readlines();
		file_size = len(lines);
		partition_file_offset = int(args.nlines); 

		seekCounter = 0;
		partition_count = 1;  
		while(file_size > 0):
			current_offset = 0; 
			if (file_size > partition_file_offset):
				current_offset = partition_file_offset;
				file_size -= partition_file_offset;  
			else:
				current_offset = file_size; 
				file_size -= file_size; 

			partition_file_name =  ('%s-%s%d%s' % (str(args.input.split('.')[0]), args.suffix, partition_count,\
			str("."+args.input.split('.')[1])));
			
			print ("Writing %s" % partition_file_name);

			with open(partition_file_name,'w') as fw: 
				for i in range(0,current_offset,1):
					fw.write(lines[seekCounter+i]); 

			seekCounter += current_offset; 
			partition_count += 1; 		



		



