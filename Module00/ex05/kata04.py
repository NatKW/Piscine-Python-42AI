"""
String formatting:
The kata variable is always a tuple that contains, in the following order: • 2 non-negative integer containing up to 2 digits
• 1 decimal
• 1 integer
• 1 decimal

 Write a program that display this variable content according to the format shown below:
$> python3 kata04.py
module_00, ex_04 : 132.42, 1.00e+04, 1.23e+04
$> python3 kata04.py | cut -c 10,18
,:

"""

kata = (0, 4, 132.42222, 10000, 12345.67)

print(f'module_{kata[0]:0>2}, ex_{kata[1]:0>2} : {kata[2]:3.2f}, {kata[3]:.2e}, {kata[4]:.2e}')