'''

Challenge 1: Square Numbers and Return Their Sum

Problem Statement #
Implement a class Point that has three properties and a method. All these attributes (properties and methods) should be
public. This problem can be broken down into two tasks:

Task 1 #
Implement a constructor to initialize the values of three properties: x, y, and z.

Task 2 #
Implement a method, sqSum(), in the Point class which squares x, y, and z and returns their sum.

Sample Properties

'''


class Point:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def sqSum(self):
        result = (self.x * self.x) + (self.y * self.y) + (self.z * self.z)
        return result

obj1 = Point(2, 3, 5)
print(obj1.sqSum())