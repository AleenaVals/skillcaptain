# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 10:25:49 2023

@author: aleen
"""

'''
Create a Python class called Point that represents a point in 2D space. 
Implement the __init__ method to initialize the x and y coordinates of the point. 
Implement the __eq__ method to compare two Point objects for equality based on their coordinates.'''


class Point:
    '''Represents a point in 2D space.'''
    
    def __init__(self,x,y):
        self.x=x
        self.y=y
        
    def __eq__(self,other):
        '''Compares two point objects for equality based on their coordinates.'''
        
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False
 
point_1= Point(1,2)
point_2= Point(3,4)
point_3= Point(1,2)

print(point_1 == point_2)
print(point_1 == point_3)
    
