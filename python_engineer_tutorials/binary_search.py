def binary_search(lst: list, target: int):
    """
    Find the target value from given list, and return its position(index).
    """
    
    ## return None if list is empty.
    if not lst:
        return None

    first_index = 0            ## first index of the list.
    last_index = len(lst) - 1  ## last index of the list.

    while first_index <= last_index:

        mid_index = (first_index + last_index) // 2 ## find mid index using floor division.

        if target == lst[mid_index]:
            return mid_index
        
        elif target > lst[mid_index]:
            first_index = mid_index + 1
        
        else:
            last_index =  mid_index - 1

    return None

my_list = [1,2,3,4,5,6,7,8,9,10,11,12]

print(binary_search(my_list, 5))