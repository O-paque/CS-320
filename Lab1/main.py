import math

def is_repetable(pattern, list):
    is_repeat = True
    for i in range(0, len(list), len(pattern)):
        sample = list[i:i+len(pattern)]
        if sample != pattern:
            is_repeat = False

    return is_repeat

def repeats(list):
    if list is None:
        return None
    elif len(list) == 1:
        return None
    repeat = None
    
    for i in range(1, math.floor(len(list) / 2) + 1): 
        # Pattern can't repeat past (floor(n) / 2) + 1 range 
        pattern = list[:i]
        if is_repetable(pattern, list):
            repeat = pattern
    
    return repeat