import datetime

"""
String formating:
kata02
The kata variable is always a tuple that contains 5 non-negative integers. 
The first integer contains up to 4 digits, the rest up to 2 digits.
Write a program that display this variable content according to the format shown below:
$> python3 kata02.py | cat -e
25/09/2019 03:30$
$> python3 kata02.py | wc -c
17

"""

kata = (2019, 9, 25, 3, 30)
k = datetime.datetime(kata[0],kata[1],kata[2],kata[3],kata[4])
print(k.strftime("%d/%m/%Y %H:%M"))