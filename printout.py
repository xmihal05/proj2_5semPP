#!/usr/bin/python

#SYN:

#This file prints out formatted output

import arguments, sys, re
from collections import deque

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
	
	#check if formating file was stated
	if arguments.format_file == True:
		#read rules as que
		rules = deque(rules)
		#apply rules on text until rules que isnt empty
		while len(rules) > 0:
			s_rule = []	#init single rule list
			#get single rule from que
			s_rule = rules.popleft()
			#cast list as que
			s_rule = deque(s_rule)

			#get regular expression from single rule
			regular = s_rule.popleft()
			#convert as regex
			my_regex = r'('+re.escape(regular)+r')'

			#while commands arent empty apply them on text
			while len(s_rule) > 0:
				#pop command
				command = s_rule.popleft()

				#get type of command
				if re.match(r'bold', command):
					sin = re.sub(my_regex,r'<b>\1</b>',sin)

				elif re.match(r'italic', command):
					sin = re.sub(my_regex,r'<i>\1</i>',sin)

				elif re.match(r'underline', command):
					sin = re.sub(my_regex,r'<u>\1</u>',sin)

				elif re.match(r'teletype', command):
					sin = re.sub(my_regex,r'<tt>\1</tt>',sin)

				elif re.match(r'size\:([1-7])', command):
					sin = re.sub(my_regex,r'<font size=cislo>\1</font>',sin)
			
				elif re.match(r'color\:([0-9A-Fa-f]{6})', command):
					sin = re.sub(my_regex,r'<font color=\#farba>\1</font>',sin)

	count_line = 0
	print_count = 0
	#check if --br argument was used
	if arguments.args.br == True:
		for item in sin.split("\n"):
			count_line = count_line + 1 

		for item in sin.split("\n"):
			if print_count < (count_line - 1):
				fout.write(item.rstrip('\n') + '<br />\n')
				print_count = print_count + 1
	else:
		fout.write(sin)
		sys.exit(0)
