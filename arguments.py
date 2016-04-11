#!/usr/bin/python

#SYN:

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

if count_length > 8:	#if too many arguments are used exit 1
	sys.exit(1)	

#check if any argument was used more than once
if (count_length == 3) and (args.br == True):	# --br must have been used more than once
	sys.exit(1)

elif (count_length == 4):
	if (args.br != True):	# --br must be used
		sys.exit(1)
	else:
		if input_file != True and output_file != True and format_file != True:
			sys.exit(1)	#one of these arguments must be used in combination w br

elif (count_length == 5):
	if (args.br == True):	# br cannot be used with this number of args
		sys.exit(1)
	#check if none is used more than once
	if (input_file == True):
		if (output_file != True) and (format_file != True):
			sys.exit(1)
	elif (output_file == True):
		if (input_file != True) and (format_file != True):
			sys.exit(1)
	elif (format_file == True):
		if (input_file != True) and (output_file != True):
			sys.exit(1)

elif (count_length == 6):
	#check if br is used and two different arguments!
	if (args.br != True):
		sys.exit(1)
	else:
		if (input_file == True):
			if (output_file != True) and (format_file != True):
				sys.exit(1)
		elif (output_file == True):
			if (input_file != True) and (format_file != True):
				sys.exit(1)
		elif (format_file == True):
			if (input_file != True) and (output_file != True):
				sys.exit(1)
		else:
			sys.exit(1)

elif (count_length == 7):
	# check if all the arguments are used except --br
	if (args.br == True):
		sys.exit(1)
	else:
		if (input_file != True) or (format_file != True) or (output_file != True):
			sys.exit(1)

elif(count_length == 8):
	# every possible argument must be used with this number of args
	if (input_file != True) or (format_file != True) or (output_file != True) or (args.br != True):
		sys.exit(1)
