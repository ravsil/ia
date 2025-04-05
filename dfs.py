from time import time

def dfs(puzzle):
    puzzle = list(puzzle)
    visited = set()
    stack = [(puzzle, [])]
    index = 0

    while len(stack) != 0:
        current, path = stack.pop()
        index += 1
        if current == [1, 2, 3, 4, 5, 6, 7, 8, 0]:
            return path
        state = tuple(current)
        if state in visited:
            continue
        visited.add(state)
        i = current.index(0)

        if i % 3 != 0:
            left = current.copy()
            left[i], left[i - 1] = left[i - 1], left[i]
            stack.append((left, path + ["Left"]))
        if i % 3 != 2:
            right = current.copy()
            right[i], right[i + 1] = right[i + 1], right[i]
            stack.append((right, path + ["Right"]))
        if i > 2:
            up = current.copy()
            up[i], up[i - 3] = up[i - 3], up[i]
            stack.append((up, path + ["Up"]))
        if i < 6:
            down = current.copy()
            down[i], down[i + 3] = down[i + 3], down[i]
            stack.append((down, path + ["Down"]))
    return None


puzzle = (0, 8, 7, 6, 5, 4, 3, 2, 1)
start = time()
dfsPath = dfs(puzzle)
end = time()
print("DFS")
print("time:", end - start)
print(dfsPath)
print("moves:", len(dfsPath))