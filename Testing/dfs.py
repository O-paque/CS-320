def longest_path(torus):
    if torus is None or not torus or not torus[0]:
        return []

    m, n = len(torus), len(torus[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def is_valid(x, y, prev_value):
        return 0 <= x < m and 0 <= y < n and torus[x][y] > prev_value

    def dfs(x, y, memo):
        print("new dfs")
        if (x, y) in memo:
            return memo[(x, y)]

        max_path = [(x, y)]
        current_value = torus[x][y]

        for dx, dy in directions:
            print("dx: ", dx, ", dy: ", dy)
            new_x, new_y = (x + dx) % m, (y + dy) % n

            if is_valid(new_x, new_y, current_value):
                path = dfs(new_x, new_y, memo)
                if len(path) + 1 > len(max_path):
                    max_path = [(x, y)] + path

        memo[(x, y)] = max_path
        return max_path

    result = []
    for i in range(m):
        for j in range(n):
            path = dfs(i, j, {})
            if len(path) > len(result):
                result = path

    return result if len(result) > 1 else []

# Example usage:
torus = [
    [1, 2, 3],
    [6, 5, 4],
    [7, 8, 9]
]

result = longest_path(torus)
print(result)

arr1 = [[0,9,8],
        [3,5,1],
        [4,2,6]]

result = longest_path(arr1)
print(result)