import math

def distance(point1, point2):
    return math.sqrt(((point1[0] - point2[0])**2) + (point1[1] - point2[1])**2)

def closest_pair(points:list): # returns int (distance)
    # sort list
    points = sorted(points)
    
    def divide():
        # create left and right lists
        len_half = round(len(points) / 2)
        L = points[:len_half]
        R = points[len_half:]
        
    
