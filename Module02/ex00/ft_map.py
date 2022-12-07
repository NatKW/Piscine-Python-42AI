def ft_map(function_to_apply, iterable):
	"""Map the function to all elements of the iterable.
	Args:
	function_to_apply: a function taking an iterable.
	iterable: an iterable object (list, tuple, iterator).
	Return: An iterable.
	None if the iterable can not be used by the function.
	"""
	
	try:
		iterator = iter(iterable)
		result = []
		for i in iterator:
			result.append(function_to_apply(i))
		return result
	except TypeError:
		print(iterable, 'is not iterable')

if __name__ == '__main__':
	x = [1, 2, 3, 4, 5]
	print(list(ft_map(lambda t: t + 1, x)))
	x = [1, "a", 3, 4, 5]
	print(list(ft_map(lambda t: t + 1, x)))
