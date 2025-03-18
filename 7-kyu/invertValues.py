"""
[1, 2, 3, 4, 5] --> [-1, -2, -3, -4, -5]
[1, -2, 3, -4, 5] --> [-1, 2, -3, 4, -5]
[] --> []
"""

def invert(lst):
    new_list = []
    for num in lst:
        result = num * -1
        new_list.append(result)
    return new_list

print(invert([1,-2,3]))



