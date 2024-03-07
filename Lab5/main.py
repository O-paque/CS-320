import random


def placement(num_objects, map):
    if map is None or not map or num_objects <= 0:
        return None

    rows, columns = len(map), len(map[0])
    valid_places, selected_places = [], []
    
    for i in range(rows):
        for j in range(columns):
            if (map[i][j]):
                valid_places.append((i, j))
    
    while (len(selected_places) < num_objects) and len(valid_places) > 0:
        rand_pos = random.randrange(len(valid_places))
        selected_places.append(valid_places.pop(rand_pos))
    
    return selected_places


def print_arrays(array):
    rows = len(array)
    for i in range(rows):
        print(array[i])


def create_rand_array(num_rows, num_cols):
    array = [[False for i in range(num_cols)] for j in range(num_rows)]
    for i in range(num_rows):
        for j in range(num_cols):
            
            if(random.randrange(2)):
                array[i][j] = True
    return array



map1 = [[False, False, True],
        [False, True, False],
        [True, False, False]]

map2 = create_rand_array(10, 10)

print_arrays(map2)

list1 = placement(20, map2)
print(list1)
list1 = sorted(list1)
print(list1)
