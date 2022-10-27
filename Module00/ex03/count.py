import string
import sys

def text_analyser(text=None):
	"""
	This function counts the number of upper characters, lower characters,
	punctuation and spaces in a given text.
	"""

	if text is None:
		text = input('What is the text to analyse?\n')
	punctuation = sum((c in string.punctuation) for c in text)
	lower = sum(c.islower() for c in text)
	upper = sum(c.isupper() for c in text)
	spaces = sum(c.isspace() for c in text)

	print(f'The text contains {len(text)} characters:\n'
          f'- {upper} upper letters\n'
          f'- {lower} lower letters\n'
          f'- {punctuation} punctuation marks\n'
          f'- {spaces} spaces')

"""
Part 1 : Test your function with the python console

def main()
	print(text_analyser.__doc__)
	text_analyser(42)
	text_analyser()"Python 2.0, released 2000, introduced
features like List comprehensions and a garbage collection
system capable of collecting reference cycles.")
	text_analyser()

if __name__ == '__main__':
	main()
"""

"""
Part 2 : update your file so it can also be launched as a standalone program.

"""
if __name__ == '__main__':
	if len(sys.argv) == 1:
		print("Provide a string to analyse")
	elif len(sys.argv) == 2:
		text_analyser(sys.argv[1])
	else:
		print("Provide a SINGLE string to analyse")


