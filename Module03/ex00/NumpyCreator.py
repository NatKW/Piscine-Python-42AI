import numpy as np

class NumpyCreator:
	""" Each
	method receives as an argument a different type of data structure and transforms it into
	a Numpy array"""

	def from_list(self, lst): 
		""" Takes a list or nested lists and returns its corresponding
		Numpy array"""
		if type(lst)==list:
			return np.array(lst, dtype=object)
		return None
	
	def from_tuple(self, tpl): 
		"""takes a tuple or nested tuples and returns its correspond-
		ing Numpy array."""
		if type(tpl)==tuple:
			return self.from_list(tpl)
		return None

	def from_iterable(self, itr): 
		"""Takes an iterable and returns an array which contains
		all its elements."""
		return np.fromiter(iter)

	@staticmethod
	def from_shape(shape, value=0): 
		""" Returns an array filled with the same value.
		The first argument is a tuple which specifies the shape of the array, and the second
		argument specifies the value of the elements. This value must be 0 by default."""
		return np.full(shape, value)

	@staticmethod
	def random(*shape): 
		"""Returns an array filled with random values. It takes as an
		argument a tuple which specifies the shape of the array."""
		return np.random.rand(*shape)

	@staticmethod
	def identity(n): 
		"""Returns an array representing the identity matrix of size n."""
		return np.identity(n)