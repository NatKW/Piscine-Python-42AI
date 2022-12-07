class Evaluator:
	""" Code a class Evaluator, that has two static functions named zip_evaluate and enumerate_evaluate.
The goal of these 2 functions is to compute the sum of the lengths of every words of
a given list weighted by a list of coefficinents coefs (yes, the 2 functions should do the
same thing).
The lists coefs and words have to be the same length. If this is not the case, the
function should return -1.
You have to obtain the desired result using zip in the zip_evaluate function, and
with enumerate in the enumerate_evaluate function. """

	@staticmethod
	def zip_evaluate(coefs, words):
		assert type(coefs) == list and type(words) == list, 'Parameters must be lists'
		#assert coefs.isnumeric() == True, 'Provide only integers'

		if len(words) == len(coefs):
			return sum([coef*len(word) for coef, word in zip(coefs, words)])
		return -1

	@staticmethod
	def enumerate_evaluate(coefs, words):
		assert type(coefs) == list and type(words) == list, 'Parameters must be lists'
		#assert coefs.isnumeric() == True, 'Provide only integers'

		if len(words) == len(coefs):
			count = 0
			return sum([coefs[count]*len(word) for count, word in enumerate(words, count)])
		return -1		



		
			

