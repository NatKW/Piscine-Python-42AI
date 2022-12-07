import sys
import re

if len(sys.argv) != 3:
    print('ERROR')
    sys.exit()
try:
    # N = int(sys.argv[2])
    S = re.split(r'[^\w]+', str(sys.argv[1]))
    S = [word for word in S if len(word)> int(sys.argv[2])]
    print(S)    
except ValueError:
    print('ERROR')
