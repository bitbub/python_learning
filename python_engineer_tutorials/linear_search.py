import numpy as np

def linear_search(lst: list, target: int):
    """
    Find the target value from given list, and return its position(index).
    """

    ## return None if list is empty.
    if not lst:
        return None
    
    ## loop through list, find target and return target index.
    for i in range( 0, len(lst) ):
        if lst[i] == target:
            return i
    return None
        
my_list = [1,2,3,4,5,6,7,8,9,10,11,12]

print( linear_search(my_list, 3) )

    

