

def longest_path(torus):
    if torus is None:
        return []
    
    rows = len(torus)
    cols = len(torus[0])
    
    if rows == 0 or cols == 0:
        return []
    i, j = (0,0)
    
    while i < rows:
        while j < cols:
            print(torus[i][j], end = " ")
            j += 1
            
        i += 1
        j = 0
        print()
    
    return 0


def find_path(torus, rows, cols, i, j):
    visited = [[0 for i in range(cols)] for j in range(rows)]
    path = [(i,j)]
    visited[i][j] = 1
    
    
    
    return 0

# test arrays
arr1 = [[0,9,8],
        [3,5,1],
        [4,2,6]]

arr2 = [[0,0,0,0],
        [0,0,0,0],
        [0,0,0,0]]

# test that array indexing works as expected
print(arr1)
arr1[1][2] = 9
print(arr1)

# test being able to find the rows and columns of an unknown array/matrix
print(arr2)
rows = len(arr2)
cols = len(arr2[0])
print("Rows in arr2: ", rows, "\nCols in arr2: ", cols)

# test making an 2D array of zeroes will work as expected
visited = [[0 for i in range(cols)] for j in range(rows)]
print(visited)
visited[1][3] += 1
print(visited)

# test appending works on anything
test1 = []
test1.append((0,0))
test1.append(8)
test1.append('abc')
print(test1)

if (0,0) in test1:
    print("We found it!")

longest_path(arr1)