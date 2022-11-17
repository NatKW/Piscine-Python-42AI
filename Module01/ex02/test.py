from vector import Vector

if __name__ == "__main__": 

    e1 = Vector("Error Test")

    print("Error test: ", e1)

    v1 = Vector(5)
    v2 = Vector((10, 16))
    
    v4 = Vector([1.3, 4.8, 9.1])
    v5 = Vector([1, 4, 9])

    v6 = Vector([[0.0], [1.0], [2.0], [3.0]])

    v = [v1, v2, v4, v5, v6]

    for i in v:
        print(i.values)
        print(i.size)
        print(i.shape)

# Row vector of shape (1, n)
# = list of floats
#Vector([[0.0, 1.0, 2.0, 3.0]]).shape)
# Expected output : (1,4)  
# Column vector of shape (n, 1)
# = list of lists of single floats
#Vector([[0.0], [1.0], [2.0], [3.0]]).shape)
# Expected output:(4,1)
