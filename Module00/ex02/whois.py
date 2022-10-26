import sys

for arg in (sys.argv[1:]):
	a = 0
	try:
		a = int(arg)
	except ValueError:
		print('argument is not an integer')
		exit()
	assert len(sys.argv) == 2, 'more than one argument are provided'
	if a == 0:
		print('I\'m Zero.')
	elif (a % 2) == 0:
		print('I\'m Even.')
	else:
		print('I\'m Odd.')