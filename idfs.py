from time import time

def idfs(puzzle):
    puzzle = list(puzzle)
    visited = set()
    stack = [(puzzle, [], 0)]
    index = 0
    limit = 0

    while True:
        current, path, depth = stack.pop()
        index += 1
        if current == [1, 2, 3, 4, 5, 6, 7, 8, 0]:
            return path
        state = tuple(current)
        if state in visited:
            continue
        visited.add(state)
        i = current.index(0)

        if depth < limit:
            if i % 3 != 0:
                left = current.copy()
                left[i], left[i - 1] = left[i - 1], left[i]
                stack.append((left, path + ["Left"], depth + 1))
            if i % 3 != 2:
                right = current.copy()
                right[i], right[i + 1] = right[i + 1], right[i]
                stack.append((right, path + ["Right"], depth + 1))
            if i > 2:
                up = current.copy()
                up[i], up[i - 3] = up[i - 3], up[i]
                stack.append((up, path + ["Up"], depth + 1))
            if i < 6:
                down = current.copy()
                down[i], down[i + 3] = down[i + 3], down[i]
                stack.append((down, path + ["Down"], depth + 1))
        else:
            limit += 1
            stack.append((puzzle, [], limit))
            visited.clear()


puzzle = (0, 8, 7, 6, 5, 4, 3, 2, 1)
start = time()
path = idfs(puzzle)
end = time()
print("IDFS")
print("time:", end - start)
print(path)
print("moves:", len(path))