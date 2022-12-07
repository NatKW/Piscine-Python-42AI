from random import randrange

def sattolo_cycle(items) -> None:
	"""Sattolo's algorithm from Wikipedia 'Fisher-Yates shuffle'"""
	i = len(items)
	while i > 1:
		i = i - 1
		j = randrange(i)  # 0 <= j <= i-1
		items[j], items[i] = items[i], items[j]
		return items

def generator(text, sep=" ", option=None):
	""" 
	Splits the text according to sep value and yield the substrings.
	option precise if an action is performed to the substrings before it is yielded.

	shuffle : shuffles the list f words
	unique : returns a list where each word appears only once
	ordered: alphabetically sorts the words
	"""
	try:
		words = text.split(sep)

		if (option == 'shuffle'):
			words = sattolo_cycle(words)
		elif (option == 'ordered'):
			words.sort()
		elif (option=='unique'):
			words = list(set(words))

		for word in words:
			yield (word)		

	except:
		if type(text) is not str \
		or option not in ['None', 'shuffle', 'unique', 'ordered']:
			yield "Error"


			
if __name__ == '__main__':
	text = "Le Lorem Ipsum est simplememt du faux texte."
	for word in generator(text, sep=" "):
		print(word)		
	print("---------------------------------------------------------------")
	for word in generator(text, sep=" ", option="shuffle"):
		print(word)
	print("---------------------------------------------------------------")
	for word in generator(text, sep=" ", option="ordered"):
		print(word)
	print("---------------------------------------------------------------")
	text = "Lorem Lorem Ipsum Ipsum Lorem Lorem Ipsum Ipsum"
	for word in generator(text, sep=" ", option='unique'):
	 	print(word)
	print("---------------------------------------------------------------")
	text = 1.0
	for word in generator(text, sep="."):
		print(word)
