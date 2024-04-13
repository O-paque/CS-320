

def build_adj_list(torus, i, j):
    height = len(torus)
    length = len(torus[0])
    left, right = (j - 1, j + 1)
    top, bottom = (i - 1, i + 1)
    adj = []

    # Check if indexes are at boundaries, wrap to opposite side if true
    # to implement torus structure
    if left < 0:
        left = length - 1
    
    if right >= length:
        right = 0
        
    if bottom >= height:
        bottom = 0
        
    if top < 0:
        top = height - 1
    
    adj.append((i, left))
    adj.append((i, right))
    adj.append((top, j))
    adj.append((bottom, j))
    return adj


def find_path(torus, i, j, dictionary):
    if (i, j) in dictionary:
        return dictionary[(i, j)]
    
    adj_list = build_adj_list(torus, i, j)
    
    longest = [(i, j)]
    for k in adj_list:
        adj_x, adj_y = k
        
        if torus[adj_x][adj_y] > torus[i][j]:
            path = find_path(torus, adj_x, adj_y, dictionary)
            if len(path) + 1 > len(longest):
                longest = [(i, j)] + path
        
    dictionary[(i, j)] = longest
    return longest


def longest_path(torus):
    if torus is None or not torus or not torus[0]:
        return []
    
    rows = len(torus)
    cols = len(torus[0])

    i, j = (0, 0)
    longest = []
    
    while i < rows:
        while j < cols:
            path = find_path(torus, i, j, {})
            if len(path) > len(longest):
                longest = path
            j += 1
        i += 1
        j = 0
    
    return longest if len(longest) > 1 else []
