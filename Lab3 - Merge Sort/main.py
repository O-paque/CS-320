import math


def merge(front, back):
    i = 0
    j = 0
    merged = []
    
    while i in range(len(front)) and j in range(len(back)):
        if front[i] <= back[j]:
            merged.append(front[i]) 
            i += 1
        else:
            merged.append(back[j]) 
            j += 1
        
    while i in range(len(front)):
        merged.append(front[i])
        i += 1
        
    while j in range(len(back)):
        merged.append(back[j]) 
        j += 1

    return merged


def mergesort(mlist):
    if mlist is None:
        return None
    elif mlist == []:
        return []
    
    if len(mlist) > 1:
        middle = math.floor(len(mlist) / 2)
        frontList = mergesort(mlist[:middle])
        backList = mergesort(mlist[middle:])
    else:
        return mlist
    
    return merge(frontList, backList)
