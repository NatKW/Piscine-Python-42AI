def ft_filter(function_to_apply, iterable):
	"""Filter the result of function apply to all elements of the iterable.
	Args:
	function_to_apply: a function taking an iterable.
	iterable: an iterable object (list, tuple, iterator).
	Return:
	An iterable.
	None if the iterable can not be used by the function.
	"""
	
	try:
		iterator = iter(iterable)
		result = []
		for i in iterator:
			if function_to_apply(i) == True:
				result.append(i)
		return result
	except TypeError:
		print(iterable, 'is not iterable')

if __name__ == '__main__':

	x = [1, 2, 3, 4, 5]
	print(list(ft_filter(lambda dum: not (dum % 2), x)))
	# Output:
	#[2, 4]