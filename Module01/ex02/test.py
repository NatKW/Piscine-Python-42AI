import vector
from vector import Vector

e1 = Vector("Error Test")
v1 = Vector(5)
v2 = Vector((10, 16))
v3 = Vector(range(2, 7))
v4 = Vector([1.3, 4.8, 9.1])
v5 = Vector([1, 4, 9])
v = [v1, v2, v3, v4, v5]
for i in v:
    print(i.values)