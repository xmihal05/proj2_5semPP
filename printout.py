#!/usr/bin/python

#SYN:

#This file prints out formatted output

import arguments, sys

def print_output(sin):
	#opens output file
	if arguments.output_file == True:

		try:
			fout = open(arguments.args.out_file, 'w')
		#couldnt open file => exit 1
		except IOError:
			sys.exit(3)
	else:
		#no output file => use stdout
		fout = sys.stdout

	#check if formating file was stated
	if arguments.format_file != True:
		#if not print input on output
		fout.write(sin)
		sys.exit(0)
	else:
		print 'uprav vypis podla pravidiel!'
