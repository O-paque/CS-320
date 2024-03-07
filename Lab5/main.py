import random


def placement(numobjects, map):
    if map is None or numobjects <= 0:
        return None

    rows, columns = len(map), len(map[0])
    
    places = []
    
    for i in range(rows):
        for j in range(columns):
            if (map[i][j]):
                places.append((i, j))
    
    return places


def print_arrays(array):
    rows = len(array)
    for i in range(rows):
        print(array[i])


def create_rand_array(num_rows, num_cols):
    array = [[False for i in range(num_cols)] for j in range(num_rows)]
    print(array)
    for i in range(num_rows):
        for j in range(num_cols):
            if(random.randrange(2)):
                array[i][j] = True
    return array



map1 = [[False, False, True],
        [False, True, False],
        [True, False, False]]

map2 = create_rand_array(10, 10)

list1 = placement(3, map1)
print_arrays(map1)
print(list1)

print_arrays(map2)

