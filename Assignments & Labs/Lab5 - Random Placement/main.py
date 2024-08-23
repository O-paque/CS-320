import random


def placement(num_objects, map):
    if not map or num_objects <= 0:
        return None

    rows, columns = len(map), len(map[0])
    valid_places, selected_places = [], []
    
    for i in range(rows):
        for j in range(columns):
            if (map[i][j]):
                valid_places.append((i, j))
    
    if len(valid_places) < num_objects:
        return None
    
    while (len(selected_places) < num_objects):
        rand_pos = random.randrange(len(valid_places))
        selected_places.append(valid_places.pop(rand_pos))
    
    return selected_places
