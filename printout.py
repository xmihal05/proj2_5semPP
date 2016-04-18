#!/usr/bin/python

#SYN:

#This file prints out formatted output

import arguments, sys, re

def print_output(sin,rules):
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

#	count_line = 0
	#check if formating file was stated
	if arguments.format_file != True:
		#if not print input on output
		if arguments.args.br == True:
			for item in sin.split("\n"):
				#MOZNO KONTROLOVAT POCET RIADKOV => ==1 vypis, >1 vypis -1
#				count_line = count_line + 1 
				fout.write(item.rstrip('\n') + '<br />\n')
		else:
			fout.write(sin)
#		print count_line
		sys.exit(0)
	else:
		print 'uprav vypis podla pravidiel!'
		print '\n toto je vstup: \n'
		print sin
		print '\n a toto su pravidla: \n'
		print rules
