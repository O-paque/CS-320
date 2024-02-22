import math

def merge(front,back,merged):
    i = 0
    j = 0
    
    print("Merged before sort: ", merged)
    
    while i in range(len(merged)) and j in range(len(merged)):
        if front[i] <= back[j]:
            merged[i+j] = front[i]
            i += 1
        else:
            merged[i+j] = back[j]
            j += 1
        
    while i in range(len(merged)):
        merged[i+j] = front[i]
        i += 1
        
    while j in range(len(merged)):
        merged[i+j] = back[j]
        j += 1
    
    print("Merged after sort: ", merged)
    return merged


def mergesort(mlist):
    
    if len(mlist) > 1:
        middle = math.floor(len(mlist) / 2)
        frontList = mergesort(mlist[:middle])
        backList = mergesort(mlist[middle:])
    else:
        return mlist
    
    merge(frontList, backList, mlist)
    return mlist
    

    

testList1 = [0,8,4,9,2,6]
merge1 = [2,4]
merge2 = [1,3]
merge3 = [0, 0, 0, 0]

print(merge(merge1, merge2, merge3))

testResponse1 = mergesort(testList1)

print("Response 1: ", testResponse1)

x = 5
m = 0

while m in range(x):
    print(m)
    m += 1

