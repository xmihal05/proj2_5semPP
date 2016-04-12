#!/usr/bin/python

#SYN:

#This file parses formating file into separate rules

import arguments, sys

def rule_parse():
	# open formating file
	try:
		ffile = open(arguments.args.f_file)
	# couldnt open formating file => exit 2
	except IOError:
		sys.exit(2)

	print 'read formating file line by line'

