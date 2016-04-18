#!/usr/bin/python

#SYN:

# This file is used to parse arguments from commad line

import argparse, sys

# parse arguments and their options
options = argparse.ArgumentParser(
			prog='syn.py',
			description='SYN: Script for highlighting syntax',
			epilog='Each optional parameter can be used only once.')

options.add_argument('--format', dest='f_file', required=False,
			help='A path and name of a formatting file')
options.add_argument('--input', dest='in_file', required=False,
			help='A path and name of an input file')
options.add_argument('--output', dest='out_file', required=False,
			help='A path and name of an output file')
options.add_argument('--br', action='store_true', required=False,
			help='Adds <br /> into formatted output at the end of each line')

#read arguments
try:
	args = options.parse_args()

except SystemExit:
	sys.exit(1)	#in case of error exits with one

#set true or false values for further arguments check
if args.f_file:
	format_file = True
else:
	format_file = False

if args.in_file:
	input_file = True
else:
	input_file = False

if args.out_file:
	output_file = True
else:
	output_file = False

count_length = len(sys.argv)	#count number of arguments

if count_length > 5:	#if too many arguments are used exit 1
	sys.exit(1)	

#check if any argument was used more than once
if (count_length == 3):
	if input_file == True:
		if output_file != True and format_file != True and args.br != True:
			sys.exit(1)
	elif output_file == True:
		if format_file != True and args.br != True:
			sys.exit(1)
	elif format_file == True:
		if args.br != True:
			sys.exit(1)
	#none of the above were right so next one must be error as well
	elif args.br == True:
		sys.exit(1)
	

elif (count_length == 4):
	if input_file == True:
		if output_file != True and format_file != True and args.br != True:
			sys.exit(1)
		else:
			if output_file == True:
				if format_file != True and args.br != True:
					sys.exit(1)
			elif args.br == True:
				if format_file != True:
					sys.exit(1)
			#none of above were true, this is also error
			elif format_file == True:
				sys.exit(1)

	elif output_file == True:
		if format_file != True or args.br != True:
			sys.exit(1)
	#others are errors also
	elif format_file == True or args.br == True:
		sys.exit(1)

elif (count_length == 5):
	if input_file != True or output_file != True or format_file != True or args.br != True:
		sys.exit(1)
	
