from collections.abc import Iterable

def ft_reduce(function_to_apply, iterable):
	"""Apply function of two arguments cumulatively.
	Args:
	function_to_apply: a function taking an iterable.
	iterable: an iterable object (list, tuple, iterator).
	Return:
	A value, of same type of elements in the iterable parameter.
	None if the iterable can not be used by the function.
	"""
	try:
		result = iterable[0]
		for i in iterable[1:]:
			result = function_to_apply(result, i)
		return result
	except TypeError:
		print(iterable, 'is not iterable')

if __name__ == '__main__':

	lst = ['H','e','l','l','o',' ','W','o','r','l','d']
	print(ft_reduce(lambda u, v: u + v, lst))
		print(ft_reduce(lambda u, v: u + v, lst))
	# Output:
	#"Hello World"
	lst = ['H','e','l','l','o',' ','W','o','r','l',1]
	print(ft_reduce(lambda u, v: u + v, lst))
	# Output:
	#None