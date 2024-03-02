

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


def find_path(torus, path, i, j):
    
    adj_list = build_adj_list(torus, i, j)
    print("adj_list in find_path: ", adj_list)
    
    longest = []
    # temp = path  # Do I need a temp value in this function??? 
    temp = []
    temp.append(path)    
    for i in adj_list:

        print("I in find_path: ", i)
        adj_x, adj_y = i
        path_x, path_y = path[len(path) - 1]
        adjacent = torus[adj_x][adj_y]
        compare = torus[path_x][path_y]
        
        if (adjacent > compare) and (adj_x, adj_y) not in path:
            temp.append((adj_x, adj_y))
            find_path(torus, temp, adj_x, adj_y)
            
        if len(temp) > len(longest):
            longest = temp
    # path = longest
    return longest


def longest_path(torus):
    if torus is None:
        return []
    
    rows = len(torus)
    cols = len(torus[0])
    
    if rows == 0 or cols == 0:
        return []
    i, j = (0, 0)
    longest = []
    
    while i < rows:
        while j < cols:
            path = [(i, j)]
            # print(torus[i][j], end = " ")
            temp = find_path(torus, path, i, j)
            if len(temp) > len(longest):
                longest = temp
            j += 1
        i += 1
        j = 0
        # print()
    
    return longest


# def find_path_2(torus, path, i, j):
    
#     adj_list = build_adj_list(torus, i, j)
#     print("adj_list in find_path: ", adj_list)
    
#     smallest = adj_list[0]
    
#     for i in adj_list:
#          adj_x, adj_y = i
#          path_x, path_y = smallest
#          temp = torus[adj_x][adj_y]
#          compare = torus[path_x][path_y]
#          print("Temp: ", temp,", compare: ", compare)
#          if (temp < compare) and i not in path:
#              smallest = (adj_x, adj_y)
             
#     print("Smallest: ", smallest)
        
#     if smallest not in path:
#         path.append(smallest)
#         adj_x, adj_y = smallest
#         find_path_2(torus, path, adj_x, adj_y)

        
#     return path
        

print("test arrays")
arr1 = [[0,9,8],
        [3,5,1],
        [4,2,6]]

arr2 = [[0,0,0,0],
        [0,0,0,0],
        [0,0,0,0]]

print("test that array indexing works as expected")
print(arr1)
arr1[1][2] = 9
print(arr1)
arr1[1][2] = 1
print(arr1)
arr1[2][0] = 100
print(arr1)
arr1[2][0] = 4
print(arr1)

print("test being able to find the rows and columns of an unknown array/matrix")
print(arr2)
rows = len(arr2)
cols = len(arr2[0])
print("Rows in arr2: ", rows, "\nCols in arr2: ", cols)

print("test making an 2D array of zeroes will work as expected")
visited = [[0 for i in range(cols)] for j in range(rows)]
print(visited)
visited[1][3] += 1
print(visited)

print("test appending works on anything")
test1 = []
test1.append((0,0))
test1.append(8)
test1.append('abc')
print(test1)
if (0,0) in test1:
    print("We found it!")

print("test longest_path returns without errors")
longest_path(arr1)

print("test build_adj_list works properly")
i, j = (1,1) # change this to any [0-2][0-2] index and check manually
adj1 = build_adj_list(arr1, i, j)
print()
longest_path(arr1)
print(adj1)
print("Start: ", arr1[i][j])

i, j = adj1[0]
print("Left: ", arr1[i][j])

i, j = adj1[1]
print("Right: ", arr1[i][j])

i, j = adj1[2]
print("Top: ", arr1[i][j])

i, j = adj1[3]
print("Bottom: ", arr1[i][j])

for i in adj1:
    print("i: ", i)
    x, y = i
    print("x: ", x, ", y: ", y)
    
print("test find_path works properly")
path1 = [(1,1)]
path1 = find_path(arr1, path1, 1, 1)
print(path1)

# print("test find_path_2 works properly")
# path1 = [(0,0)]
# path1 = find_path_2(arr1, path1, 0, 0)
# print(path1)
