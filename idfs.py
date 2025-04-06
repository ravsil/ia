from collections import deque
import time
import psutil
import os

def get_ram_usage():
    process = psutil.Process(os.getpid())
    return process.memory_info().rss / 1024 / 1024  # MB

def rebuild_path(start, finish):
    i = start.index("9")
    if i > 2:
        cpy = list(start)
        cpy[i], cpy[i - 3] = cpy[i - 3], cpy[i]
        if "".join(cpy) == finish:
            return "Up"
    if i < 6:
        cpy = list(start)
        cpy[i], cpy[i + 3] = cpy[i + 3], cpy[i]
        if "".join(cpy) == finish:
            return "Down"
    if i % 3 != 0:
        cpy = list(start)
        cpy[i], cpy[i - 1] = cpy[i - 1], cpy[i]
        if "".join(cpy) == finish:
            return "Left"
    if i % 3 != 2:
        cpy = list(start)
        cpy[i], cpy[i + 1] = cpy[i + 1], cpy[i]
        if "".join(cpy) == finish:
            return "Right"

def idfs(puzzle):
    puzzle = int("".join([str(x) for x in puzzle]).replace("0", "9"))
    GOAL = "123456789"
    limit = 0
    data = {
        "path_to_goal": [],
        "cost_of_path": 0,
        "nodes_expanded": 0,
        "fringe_size": 0,
        "max_fringe_size": 0,
        "search_depth": 0,
        "max_search_depth": 0,
        "running_time": time.time(),
        "max_ram_usage": 0
    }

    while True:
        stack = deque()
        stack.append((0, puzzle))
        visited = {puzzle: 0}
        tree = {puzzle: -1}
        
        while stack:
            data["max_fringe_size"] = max(data["max_fringe_size"], len(stack))
            data["max_ram_usage"] = max(data["max_ram_usage"], get_ram_usage())

            depth, current = stack.pop()
            if depth > limit:
                continue
            current_str = str(current)
            data["nodes_expanded"] += 1
            data["search_depth"] = depth
            data["max_search_depth"] = max(data["max_search_depth"], depth)
            if current_str == GOAL:
                while tree[current] != -1:
                    data["path_to_goal"].append(rebuild_path(str(tree[current]), str(current)))
                    current = int(tree[current])
                data["path_to_goal"].reverse()
                data["cost_of_path"] = len(data["path_to_goal"])
                data["fringe_size"] = len(stack)
                data["running_time"] = time.time() - data["running_time"]
                return data

            i = current_str.index('9')
            neighbors = []
            if i % 3 != 2:
                l = list(current_str)
                l[i], l[i + 1] = l[i + 1], l[i]
                neighbors.append(int(''.join(l)))
            if i % 3 != 0:
                l = list(current_str)
                l[i], l[i - 1] = l[i - 1], l[i]
                neighbors.append(int(''.join(l)))
            if i < 6:
                l = list(current_str)
                l[i], l[i + 3] = l[i + 3], l[i]
                neighbors.append(int(''.join(l)))
            if i > 2:
                l = list(current_str)
                l[i], l[i - 3] = l[i - 3], l[i]
                neighbors.append(int(''.join(l)))

            for neighbor in reversed(neighbors):
                if neighbor not in visited or visited[neighbor] > depth + 1:
                    visited[neighbor] = depth + 1
                    if depth < limit:
                        stack.append((depth + 1, neighbor))
                        tree[neighbor] = current

        limit += 1

puzzle = (0, 8, 7, 6, 5, 4, 3, 2, 1)
result = idfs(puzzle)
print(result)