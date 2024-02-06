import math

def extract(list,lo,hi):
    if list is None:
        return None
    elif lo > hi:
        return None
    elif list == []:    # Need to check this case
        return []
    
    lower, upper = findBoundary(list, lo), findBoundary(list, hi)
    
    return list[lower:upper+1]
    
    
def findBoundary(list, boundary):
    middle = math.floor(len(list) / 2)
    
    return 0
