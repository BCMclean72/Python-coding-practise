#class created to test some class features in Python
#The class describes a triple. A math structure for a point in 3 dimensions.

class Triple:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    
    def __str__(self):
        return "({0},{1},{2})".format(self.x,self.y,self.z)

    def __add__(self, other):
        x=self.x + other.x
        y=self.y + other.y
        z=self.z + other.z
        return Triple(x,y,x)

    def dot_prod(self,other):
        """This fuction calculates the dot product of two triples

        Args:
            other (Triple): The second Triple in the dot product 

        Returns:
            Triple: The result of the dot product.
        """
        return self.x*other.x + self.y*other.y + self.z*other.z
    



t = Triple(2,3,6)
s = Triple(1,1,2)
r = t+s
t.test_variable = 13
dot = t.dot_prod(s)
print(t)
print(s)
print(r)
print(dot)

