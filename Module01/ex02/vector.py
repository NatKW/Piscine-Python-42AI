class Vector:
    def __init__(self, object):
        if type(object) is int:
            self.values = [float(d) for d in range(int(object))]
            self.size = object
            self.shape = (1, self.size)
        elif type(object)is list:
            self.values = object
            self.size = len(object)
            self.shape = (self.size, 1)
        elif type(object) is tuple and len(object) == 2:
            self.values =[float(o) for o in range(object[0], object[1])] 
            self.size = len(self.values)
            self.shape = (1, self.size)
        else:
            print("Wrong Init of class Vector: \nobject must be list[float] / list[list[float]] / int / tuple[int] ...")       