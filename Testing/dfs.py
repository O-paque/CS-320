def longest_path(torus):
    if torus is None or not torus or not torus[0]:
        return []

    rows, columns = len(torus), len(torus[0])

    result = []
    for i in range(rows):
        for j in range(columns):
            path = dfs(torus, i, j, {})
            if len(path) > len(result):
                result = path

    return result if len(result) > 1 else []

def is_valid(x, y, rows, columns, torus, prev_value):
    return 0 <= x < rows and 0 <= y < columns and torus[x][y] > prev_value

def dfs(torus, x, y, memo):
    rows, columns = len(torus), len(torus[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    print("new dfs")
    if (x, y) in memo:
        return memo[(x, y)]

    max_path = [(x, y)]
    current_value = torus[x][y]

    for dx, dy in directions:
        print("dx: ", dx, ", dy: ", dy)
        new_x, new_y = (x + dx) % rows, (y + dy) % columns

        if is_valid(new_x, new_y, rows, columns, torus, current_value):
            path = dfs(torus, new_x, new_y, memo)
            if len(path) + 1 > len(max_path):
                max_path = [(x, y)] + path

    memo[(x, y)] = max_path
    return max_path


arr1 = [[0,9,8],
        [3,5,1],
        [4,2,6]]

result = longest_path(arr1)
print(result)