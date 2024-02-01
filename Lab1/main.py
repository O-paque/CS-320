import math

def isRepetable(pattern, list):
    isRepeat = True
    for i in range(0, len(list), len(pattern)):
        sample = list[i:i+len(pattern)]
        if sample != pattern:
            isRepeat = False

    return isRepeat

def repeats(list):
    if list == None:
        return None
    elif len(list) == 1:
        return None
    repeat = None
    
    # print("List length: ", len(list), "\nLength / 2: ", len(list)/2)
    for i in range(1, math.floor(len(list)/2)+1):
        pattern = list[0:i]
        # print('pattern:' , list[0:i])
        if isRepetable(pattern, list):
            repeat = pattern
    
    return repeat
        
            
simpleList6 = ['a','b','c','a','b','c']
simpleList7 = ['a','b','a','b','a','b', 'a']
simpleList8 = ['a','b', 1, 2,'a','b', 1, 2]
simpleList11 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
simpleList12 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]

oneList = ['a']

result = repeats(simpleList6)
print("List 1: " , simpleList6, "\nPattern: ", result)
result = repeats(simpleList7)
print("List 2: " , simpleList7, "\nPattern: ", result)
result = repeats(simpleList8)
print("List 3: " , simpleList8, "\nPattern: ", result)
result = repeats(oneList)
print("List 4: " , oneList, "\nPattern: ", result)
result = repeats(None)
print("List 5: " , None, "\nPattern: ", result)
result = repeats(simpleList11)
print("List 6: " , simpleList11, "\nPattern: ", result)
result = repeats(simpleList12)
print("List 7: " , simpleList11, "\nPattern: ", result)


