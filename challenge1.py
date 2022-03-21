class Point:
    def __init__(self,x,y,z): #varibles assigning
        self.x = x
        self.y = y
        self.z = z
    
    def square_value(val): #square the values
        return val ** 2
    
    def sqSum(self): 
        return Point.square_value(self.x)+Point.square_value(self.y)+Point.square_value(self.z)

obj = Point(1,3,5)
print(obj.sqSum())