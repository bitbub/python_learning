def recursive_binary_search(lst: list, target: int):
    """
    Find the target value recursively from given list, and return ture if found else return false.
    """

    if not lst:
        return False
    else:
        mid_point = len(lst) // 2

        if target == lst[mid_point]:
            return True
        else:
            if target > lst[mid_point]:
                return recursive_binary_search(lst[mid_point+1:], target)
            else:
                return recursive_binary_search(lst[:mid_point], target)            


my_list = [1,2,3,4,5,6,7,8,9,10,11,12]
print(recursive_binary_search(my_list, 12))