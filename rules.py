#!/usr/bin/python

#SYN:

#This file parses formating file into separate rules

import arguments, sys, re, regulars
from collections import deque

def rule_parse(infile):
	# open formating file
	try:
		ffile = open(arguments.args.f_file)
	# couldnt open formating file => exit 2
	except IOError:
		sys.exit(2)

	split_rules = [] #empty array for splitted rules
	#read each line of a file and parse them into array
	for line in ffile:
		white_chars = re.match("[\t\s\r\f\v]*\n",line)
		if not white_chars: #cuts emty lines from format file
			split_rules.append(re.split("\t+|,\s*\t*", line))
	

	# list for easier use
	new_rules = []
	single_rule = []
	lm_list = []
	regs = []
	
	#pop saved rules, midify and check them, then save them into new list
	#continue with checking until list is empty
	while len(split_rules) != 0:
		line_list = split_rules.pop()	#separate lines list
		
		#cast list as queue
		line_que = deque(line_list)

		#left most is regular expression
		leftmost = line_que.popleft()
		
		#check ordinal value of chars
		lm_list = list(leftmost)	#split string into chars
		while len(lm_list) > 1:	#list of chars isnt empty
			single_char = lm_list.pop()
			if ord(single_char) < 32:	
				exit(4)	#wrong char used in regular expression

		#every char passed => append	
		single_rule.append(leftmost)
		regs.append(leftmost)	#list of regular expressions for sorting
	
		#check if commands are used rightly
		#continue with appending rest of list until it is empty
		while len(line_que) != 0:
			singles = line_que.popleft()
			if singles != '':
				commands = re.match("bold|italic|underline|teletype|size\:[1-7]|color\:[0-9A-Fa-f]{6}",singles)
				if commands:
					single_rule.append(singles)
				else:
					exit(4) #command not found

		if len(single_rule) < 2:	#list contains only 1 element 
			exit(4)		#formatting file has error syntax
		new_rules.append(single_rule)
		single_rule = []	#erase single rules list
			
	
	# free(single_rule)	FREE LISTS THAT ARENT USED ANYMORE!!!
	ffile.close()

	#substitute regular exressions so that pythons regex understands them
	regulars.substitute_regs(infile, regs, new_rules)
