def generator(text, sep=" ", option=None):
	""" 
	Splits the text according to sep value and yield the substrings.
	option precise if an action is performed to the substrings before it is yielded.

	shuffle : shuffles the list f words
	unique : returns a list where each word appears only once
	ordered: alphabetically sorts the words
	"""
	try:
		words = text.slit(sep)
		for word in words:
			yield (words)
	except:
		if type(text) is not str \
		or option not in ['None', 'shuffle', 'unique', 'ordered']:
			yield "Error"

	




if __name__ == '__main__':
    text = "Le Lorem Ipsum est simplememt du faux texte."
	for word in generator(text)
		if word
			print(word)
	print("\n")

	for words in generator(text):
        print("- '%s'" %words)
    print("---------------------------------------------------------------")
	# for word in generator(text, sep=" ", option="shuffle"):
	# 	print(word)
	# for word in generator(text, sep=" ", option="ordered"):
	# 	print(word)
	# text = "Lorem Ipsum Lorem Ipsum"
	# for word in generator(text, sep=" ", option="unique"):
	# 	print(word)
	# text = 1.0
	# for word in generator(text, sep="."):
	# 	print(word)