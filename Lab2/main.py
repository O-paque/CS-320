import math


def binary_search(list, key, low, high):
    middle = math.floor((low + high) / 2)
    
    if low > high:
        return middle
        
    if key > list[len(list) - 1]:
        return high - 1
    
    if key == list[middle]:
        return middle
    elif key < list[middle]:
        return binary_search(list, key, low, middle - 1)
    elif key > list[middle]:
        return binary_search(list, key, middle + 1, high)


def extract(list, lo, hi):
    if list is None:
        return None
    elif list == []:
        return []
    elif lo is not None and hi is not None and lo > hi:
        return None

    if lo is None:
        lower = 0
    else:
        lower = binary_search(list, lo, 0, len(list))
       
        if list[lower] < lo:
            lower += 1
        while (lower > 0) and (list[lower] == list[lower - 1]):
            lower -= 1
        
    if hi is None:
        upper = len(list)
    else:
        upper = binary_search(list, hi, 0, len(list))
        while upper < len(list) - 1 and list[upper] == list[upper + 1]:
            upper += 1

    if lower < 0:
        return list[0:upper + 1]
    else:
        return list[lower:upper + 1]
