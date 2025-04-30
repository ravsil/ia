import time
import psutil
import os
import heapq

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

def get_next(a, b, current, tree, queue, depth):
    l = list(current)
    l[a], l[b] = l[b], l[a]
    target = int(''.join(l))
    if target not in tree:
        heapq.heappush(queue, (manhattan(str(target)), depth + 1, target))
        tree[target] = current

def manhattan(current, goal="123456789"):
    dist = 0
    for i, val in enumerate(current):
        if val == '9': continue
        target = goal.index(val)
        dist += abs(target // 3 - i // 3) + abs(target % 3 - i % 3)
    return dist

def busca_gulosa(puzzle):
    puzzle = int("".join([str(x) for x in puzzle]).replace("0", "9"))
    GOAL = "123456789"
    queue = []
    heapq.heappush(queue, (manhattan(str(puzzle)), 0, puzzle))
    visited = set()
    tree = {puzzle: -1}
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
    while queue:
        data["max_fringe_size"] = max(data["max_fringe_size"], len(queue))
        data["max_ram_usage"] = max(data["max_ram_usage"], get_ram_usage())
        _, depth, current = heapq.heappop(queue)
        if current in visited:
            continue
        visited.add(current)
        current = str(current)
        data["nodes_expanded"] += 1
        data["search_depth"] = max(data["search_depth"], depth)
        data["max_search_depth"] = max(data["max_search_depth"], depth)
        if current == GOAL:
            current = int(current)
            while tree[current] != -1:
                data["path_to_goal"].append(rebuild_path(str(tree[current]), str(current)))
                current = int(tree[current])
            data["path_to_goal"].reverse()
            data["cost_of_path"] = len(data["path_to_goal"])
            data["fringe_size"] = len(queue)
            data["running_time"] = time.time() - data["running_time"]
            return data
        i = current.index('9')
        if i % 3 != 2: # right
            get_next(i, i + 1, current, tree, queue, depth)
        if i % 3 != 0: # left
            get_next(i, i - 1, current, tree, queue, depth)
        if i < 6: # down
            get_next(i, i + 3, current, tree, queue, depth)
        if i > 2: # up
            get_next(i, i - 3, current, tree, queue, depth)
    data["fringe_size"] = len(queue)
    data["running_time"] = time.time() - data["running_time"]
    data["path_to_goal"] = "Sem solução"
    return data

puzzle = (0, 8, 7, 6, 5, 4, 3, 2, 1)
result = busca_gulosa(puzzle)
print(result)