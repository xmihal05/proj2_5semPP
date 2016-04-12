#!/usr/bin/python

#SYN:

#This file parses formating file into separate rules

import arguments, sys, re

def rule_parse():
	# open formating file
	try:
		ffile = open(arguments.args.f_file)
	# couldnt open formating file => exit 2
	except IOError:
		sys.exit(2)

	split_rules = [] #empty array for splitted rules
	#read each line of a file and parse them into array
	for line in ffile:
		split_rules.append(re.split("\t+", line))

	print split_rules
