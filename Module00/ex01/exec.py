import sys

for arg in (sys.argv):
	arg_bis = " ".join(sys.argv[1:]).swapcase()
print(arg_bis[::-1])