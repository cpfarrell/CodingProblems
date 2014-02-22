import sys

class node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

infinity = float("infinity")
neg_infinity = float("-infinity")

def is_search(spot, min=neg_infinity, max=infinity):
    #Empty tree is easy to search
    if not spot:
        return True

    #Is value within allowed range
    if spot.value<min or spot.value>max:
        return False

    #Check if each sub tree is binary search 
    return is_search(spot.left, min, spot.value) and is_search(spot.right, spot.value, max)

a = node(8, None, None)
b = node(12, None, None)
c = node(9, a, b)
d = node(5.1, None, None)
e = node(5, None, d)
root = node(6, e, c)
print is_search(root)
