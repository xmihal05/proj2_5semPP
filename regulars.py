#!/usr/bin/python

#SYN:

import sys, re, printout
from collections import deque

def substitute_regs(infile, regs, rules):

	#cast list as queue
	regs = deque(regs)

	new_regs = []	#list of new regular expressions
	new_expr = ""
	expr_list = []	#list of chars from single expression
	close_tag = False	#set for closing ]
	no_tag = False	#no use of paranthesis => ()
	starting_par = 0 #number of ( used in reg. expression

	#for every element of que do
	while len(regs) != 0:
		expr = regs.popleft()
		first_inserted = False
				
		#parse string into list of chars
		expr_list = list(expr)
		if len(expr_list) > 1:
			#cast list as que
			expr_list = deque(expr_list)
			
			popfirst = False	#pop new first charecter
			no_sec = False	#none second char

			first = expr_list.popleft()
			while len(expr_list) > 0:
				if popfirst == True:
					first = expr_list.popleft()
					popfirst = False

				if len(expr_list) > 0:
					second = expr_list.popleft()
				else:
					no_sec = True

				if first == '.':
					if first_inserted == False:
						sys.exit(4) #error in reg. expression
					if no_sec == True:
						sys.exit(4) #needs another string
					if second == '.' or second == '|':
						sys.exit(4)	#wrong reg.expr
					else:
						new_expr += second
						popfirst = True

				elif first == '|':
					if first_inserted == False:
						sys.exit(4) #error in reg. expr
					elif no_sec == True:
						sys.exit(4) #needs second pair
					elif second == '.' or second == '|':
						sys.exit(4)	#wrong reg.expr
					else:
						new_expr += first
						if len(expr_list) == 0:
							expr_list.append(second)	#push last one!
							popfirst = True
						else:
							first = second

				elif first == '!':
					if no_sec == True:
						sys.exit(4)	#error in reg. exprss
					if second == '(':
						no_tag = True
					else:	#negation for only one char
						close_tag = True	#close in next loop
						new_expr += '[^'
						if first_inserted == False:
							first_inserted = True
						if len(expr_list) == 0:
							expr_list.append(second)	#push last one!
							popfirst = True
						else:
							first = second
				
				elif first == '(':
					starting_par = starting_par + 1
					if no_sec == True:
						sys.exit(4) #none ')' used
					else:
						if no_tag != True:
							new_expr += '('
						if second == ')':
							popfirst = True
							if no_tag != True:
								new_expr += ')'
							else:
								no_tag = False
						else:
							if len(expr_list) == 0:
								expr_list.append(second)	#push last one!
								popfirst = True
							else:
								first = second
					

				elif first == ')':
					if starting_par < 1:
						sys.exit(4)	# ( wasnt used
					else:
						starting_par = starting_par - 1		
					if no_tag != True:
						new_expr += ')'
					else:
						no_tag = False
					if no_sec != True:
						if len(expr_list) == 0:
							expr_list.append(second)	#push last one!
							popfirst = True
						else:
							first = second

				elif first == '%':
					if no_sec == True:
						sys.exit(4) #reg exprss error
					
					#check if next is special char or %t or %n or %s
					if second == '.' or second == '|' or second == '!' \
		 or second == '*' or second == '+' or second == '(' or second == ')' \
		or second == '%' or second == 't' or second == 'n' or second == 's':
						if second == '.':
							new_expr += '\.'
						elif second == '|':
							new_expr += '\|'
						elif second == '*':
							new_expr += '\*'
						elif second == '+':
							new_expr += '\+'
						elif second == '(':
							new_expr += '\('
						elif second == ')':
							new_expr += '\)'
						elif second == 't':
							new_expr += '\t'
						elif second == 'n':
							new_expr += '\n'
						elif second == 's':
							new_expr += '\s'
						elif second == '!' or second == '%':
							new_expr += second
						if first_inserted == False:
							first_inserted = True
						if close_tag == True:
							new_expr += ']'
							close_tag = False
						popfirst = True

					# %a for any character
					elif second == 'a':
						new_expr += '.'	#matches any char
						if first_inserted == False:
							first_inserted = True
						popfirst = True
						
					# %d for number 0-9
					elif second == 'd':
						new_expr += '[0-9]'	
						if first_inserted == False:
							first_inserted = True
						popfirst = True

					# %l for lower case letters
					elif second == 'l':
						new_expr += '[a-z]'
						if first_inserted == False:
							first_inserted = True
						popfirst = True
					
					# %L for capital letter
					elif second == 'L':
						new_expr += '[A-Z]'
						if first_inserted == False:
							first_inserted = True
						popfirst = True

					# %w for lower case or capital letter
					elif second == 'w':
						new_expr += '[a-zA-Z]'
						if first_inserted == False:
							first_inserted = True
						popfirst = True

					# %W for any kind of letter and numbers
					elif second == 'W':
						new_expr += '[a-zA-Z0-9]'
						if first_inserted == False:
							first_inserted = True
						popfirst = True
				
					#enter closing ] for negation if needed
					if close_tag == True:
						new_expr += ']'
						close_tag = False
				else:
					new_expr += first
					if first_inserted == False:
						first_inserted = True
					if no_sec != True:
						if len(expr_list) == 0:
							expr_list.append(second)	#push last one!
							popfirst = True
						else:
							first = second
					#add ] for negation if needed
					if close_tag == True:
						new_expr += ']'
						close_tag = False

		if new_expr != "":
			expr = new_expr
			new_expr = ""
		#save as new regular expression
		new_regs.append(expr)

	#sort new regulars
	sorted_regs = []
	sorted_regs = new_regs

	#add rest of lists to new regular expressions
	filled = []	#list for adding rules to regular expressions

	#work with lists like with que
	rules = deque(rules)
	new_regs = deque(new_regs)

	while len(rules) > 0:
		single = []	#init single line list	
		#pop old regular with rules	
		elem = rules.popleft()

		#now pop all rules and leave old reg.expression behind
		while len(elem) > 1:
			tmp = elem.pop()
			single.append(tmp)

		#pop new regular expression for pairing
		exprss = new_regs.popleft()
		single.append(exprss)	#apend new regular exprss

		filled.append(single) #append into new list

		tmp = elem.pop() #pop old regular expression

	#sort regular expression by their length
	sorted_regs.sort(key=len, reverse=True)

	#cast lists as ques
	sorted_regs = deque(sorted_regs)
	filled = deque(filled)	
	sorted_rules = []	#empty list for sorted rules

	while len(sorted_regs) > 0:
		single = [] #init single rule list
		
		#pop sorted regular expression
		s_reg = sorted_regs.popleft()
		single.append(s_reg)
		matched = False #didnt find match with other list

		while matched == False:
			#pop single rule from not sorted que
			not_sorted = filled.popleft()

			#pop regular expression from not sorted
			ns_reg = not_sorted.pop()
			
			if ns_reg == s_reg:
				matched = True #found match
				while len(not_sorted) > 0:
					tmp = not_sorted.pop()
					single.append(tmp)
				sorted_rules.append(single)
			else: #didnt find match
				not_sorted.append(ns_reg)	#append back into list
				filled.append(not_sorted)	#append list back in filled list

	#match, add html tags and write output into outfile
	printout.print_output(infile,sorted_rules)
	
