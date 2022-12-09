import csv

""" implement a context manager as a class that opens, reads, and parses a CSV file"""

class CsvReader():
	def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
		if not isinstance(filename, str) and isinstance(sep, str) and isinstance(header, bool) \
		and isinstance(skip_bottom, int) and isinstance(skip_top, int):
			exit()
		self.filename = filename
		self.sep = sep
		self.header = header
		self.skip_top = skip_top + header
		self.skip_bottom = skip_bottom

	def __enter__(self):
		with open(self, 'r') as file:
			reader = csv.reader(file)
			writer = csv.writer(file)
			for row in reader:
				if len(row) < 5 or len(row) > 100:
					continue
			writer.writerow(row)
	
	def __exit__(self):
		file.close()
	
	def getdata(self):
		""" Retrieves the data/records from skip_top to skip bottom.
		Return:
		nested list (list(list, list, ...)) representing the data.
		"""
		rows = []
		for row in csvreader:
			rows.append(row)

	def getheader(self):
		""" Retrieves the header from csv file.
		Returns:
		list: representing the data (when self.header is True).
		None: (when self.header is False).
		"""
		if self.header == True:
			header = []
			header = next(csvreader)

if __name__ == "__main__":
	with CsvReader('good.csv') as file:
		if file == None:
			print("File is corrupted")
		data = file.getdata()
		header = file.getheader()

