from time import time

def bfs(puzzle):
    puzzle = list(puzzle)
    visited = set()
    queue = [(puzzle, [])]
    index = 0
    end = [1, 2, 3, 4, 5, 6, 7, 8, 0]

    while index < len(queue):
        current, path = queue[index]
        index += 1
        if current == end:
            return path
        state = tuple(current)
        if state in visited:
            continue
        visited.add(state)
        i = current.index(0)

        if i % 3 != 0:
            left = current.copy()
            left[i], left[i - 1] = left[i - 1], left[i]
            queue.append((left, path + ["Left"]))
        if i % 3 != 2:
            right = current.copy()
            right[i], right[i + 1] = right[i + 1], right[i]
            queue.append((right, path + ["Right"]))
        if i > 2:
            up = current.copy()
            up[i], up[i - 3] = up[i - 3], up[i]
            queue.append((up, path + ["Up"]))
        if i < 6:
            down = current.copy()
            down[i], down[i + 3] = down[i + 3], down[i]
            queue.append((down, path + ["Down"]))
    return None

puzzle = (0,8,7,6,5,4,3,2,1)
start = time()
path = bfs(puzzle)
end = time()
print("BFS")
print("time:", end - start)
print(path)
print("moves:", len(path))
