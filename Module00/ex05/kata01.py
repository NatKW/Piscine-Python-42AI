"""
String formating:
kata01
The kata variable is always a dictionary and can only be filled with strings.

Write a program that display this variable content according to the format shown below:
$> python3 kata01.py
Python was created by Guido van Rossum
Ruby was created by Yukihiro Matsumoto
PHP was created by Rasmus Lerdorf
$>

"""

kata = {
    'Python': 'Guido van Rossum',
'Ruby': 'Yukihiro Matsumoto',
'PHP': 'Rasmus Lerdorf',
}
for k, v in kata.items():
    print(k,"was created by", v)