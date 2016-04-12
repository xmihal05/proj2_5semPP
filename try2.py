#!/usr/bin/python

#SYN:

# This is Main File of the project, which connects and calls function from other scripts

import sys, arguments, rules, printout

if arguments.input_file == True:	#input file was stated
	try:	#try opening an input file
		fin = open(arguments.args.in_file)

	except IOError:
		sys.exit(2)

	#read (copy) file into string and close it
	sin = fin.read()
	fin.close()

else:	# input wasnt stated => read string from stdin
	sin = sys.stdin.read()

if arguments.format_file == True:
	# call function for parsinf formatting file
	rules.rule_parse()
else:
	#none formatting file => print input on output
	printout.print_output(sin)
