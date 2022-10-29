"""
String formatting:
The kata variable is always a string whose length is not higher than 42.
kata = "The right format"
Write a program that display this variable content according to the format shown below:
$> python3 kata03.py | cat -e
--------------------------The right format%
$> python3 kata03.py | wc -c
42
$>

"""
kata = "The right format"
print(f'{kata:->42}', end='')