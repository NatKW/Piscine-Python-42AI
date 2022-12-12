import csv

""" implement a context manager as a class that opens, reads, and parses a CSV file"""

class CsvReader():
	def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
		assert isinstance(filename, str) and isinstance(sep, str) and isinstance(header, bool) \
		and isinstance(skip_bottom, int) and isinstance(skip_top, int), "Check class parameters"
		
		self.filename = filename
		self.sep = sep
		self.file_read = None
		self.header = header
		self.skip_top = skip_top
		self.skip_bottom = skip_bottom
		self.datas = []

	def __enter__(self):
		self.file_read = open(self.filename, 'r')
		csv_reader = csv.reader(self.file_read, delimiter=self.sep)
		for row in csv_reader:
				self.datas.append(row)
		return (self)
	
	def __exit__(self, exception_type, exception_value, exception_traceback):
		self.datas = []
		self.file_read.close()
	
	def getdata(self):
		""" Retrieves the data/records from skip_top to skip bottom.
		Return:
		nested list (list(list, list, ...)) representing the data.
		"""
		
		start = self.skip_top
		end = len(self.datas) - start
		if self.header:
			return self.datas[start + 1:end]
		return self.datas[start:end]

	def getheader(self):
		""" Retrieves the header from csv file.
		Returns:
		list: representing the data (when self.header is True).
		None: (when self.header is False).
		"""
		if self.header:
			return self.datas[0]
		return None

if __name__ == "__main__":
	with CsvReader('good.csv',',', True, 0, 18) as file:
		if file == None:
			print("File is missing")
		print('Header==True')
		print('Header :', file.getheader(), end = "\n")
		print('Datas :', file.getdata(), end = "\n\n")
	with CsvReader('good.csv',',', False, 0, 10) as file:
		if file == None:
			print("File is missing")
		print('Header==False')
		print('Header :', file.getheader(), end = "\n")
		print('Datas :', file.getdata(), end = "\n\n")
	with CsvReader('bad.csv',',', True, 0, 15) as file:
		if file == None:
			print("File is missing")
		print('Bad csv')
		print('Header :', file.getheader(), end = "\n")
		print('Datas :', file.getdata(), end = "\n\n")

