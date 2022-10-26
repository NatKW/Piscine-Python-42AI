import sys
import string

def text_analyser():
	for arg in (sys.argv[1:]):
		assert len(sys.argv) > 1, 'Provide a single string argument'
		assert isnumeric(arg) == False, 'Argument is not a string'
		txt = "The text contains {char} character(s):\n"
		#\- {up} upper letter(s)\n\- {low} lower letter(s)\n\- {} punctuation mark(s)\n\- {} space(s)'
	print(txt.format(char = count.arg.isalpha))