import math
import time
start_time = time.time()


def binary_search(list, key, low, high):
    middle = math.floor((low + high) / 2)
    
    if low > high:
        return middle
    
    print("Middle: ", middle, ", low: ", low, ", high: ", high)
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

    if lo is None:
        lower = 0
    else:
        lower = binary_search(list, lo, 0, len(list))
        if list[lower] < lo:
            lower += 1
        while lower > 0 and list[lower] == list[lower - 1]:
            lower -= 1
        
    if hi is None:
        upper = len(list)
    else:
        upper = binary_search(list, hi, 0, len(list))
        if list[upper] > hi:
            upper -= 1
        while upper < len(list) - 1 and list[upper] == list[upper + 1]:
            upper += 1
        
    if lower > upper:
        return None
    else:
        return list[lower:upper + 1]
# Delete anything after this

test_list1 = [10, 10, 10, 11, 13, 18, 24, 41, 57, 61, 62, 63, 
              80, 90, 94, 96, 99, 99, 99, 99, 99]
test_list2 = []
test_list3 = None

print("Test 1: ", extract(test_list1, 18, 94))
print("Test 2: ", extract(test_list2, 18, 94))
print("Test 3: ", extract(test_list3, 18, 94))
print("Test 3.5: ", extract(None, 18, 94))
print("Test 4: ", extract(test_list1, 94, 18))
print("Test 5: ", extract(test_list1, None, 94))
print("Test 6: ", extract(test_list1, 24, None))
print("Test 7: ", extract(test_list1, None, None))
print("Test 8: ", extract(test_list1, 15, 97))
print("Test 9: ", extract(test_list1, 100, 200))

end_time = time.time()
ex_t = end_time - start_time
ex_t *= 1000
print('Execution time: ', ex_t, " milliseconds")
