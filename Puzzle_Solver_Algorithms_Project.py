def solve_puzzle(Board, Source, Destination):
    """
    The function solve_puzzle takes a 2-d array as an argument to its parameter Board. It takes a tuple of integers
    representing coordinates on the Board to its parameters Source and Destination. Using BFS, the function solve_puzzle
    attempts to find a shortest path from the Source coordinate to the Destination coordinate. If such a path is found,
    the path as a list of coordinates, and a string of directions ('R' = right, 'L' = left, 'U' = up, 'D' = down) is
    returned as tuple. If no path is found, None is returned.
    """
    graph_memo = {Source: {"path": [Source], "directions": ""}}

    visited = dict()
    queue = [Source]

    while len(queue) > 0:
        current = queue[0]
        visited[current] = graph_memo[current]
        current_path = visited[current]["path"]
        current_directions = visited[current]["directions"]

        x = current[1]
        y = current[0]

        if Board[y][x] == "#":
            visited.pop(current)
            queue.pop(0)
            continue
        a = x
        b = y

        a += 1
        if 0 <= a < len(Board[0]):
            if (b, a) not in visited:
                temp_list = list()
                for element in current_path:
                    temp_list.append(element)
                temp_list.append((b, a))
                temp_string = current_directions + "R"
                if (b, a) not in graph_memo:
                    graph_memo[(b, a)] = {"path": temp_list, "directions": temp_string}
                else:
                    if len(temp_list) < len(graph_memo[(b, a)]["path"]):
                        graph_memo[(b, a)] = {"path": temp_list, "directions": temp_string}
                if (b, a) not in queue:
                    queue.append((b, a))

        a -= 2
        if 0 <= a < len(Board[0]):
            if (b, a) not in visited:
                temp_list = list()
                for element in current_path:
                    temp_list.append(element)
                temp_list.append((b, a))
                temp_string = current_directions + "L"
                if (b, a) not in graph_memo:
                    graph_memo[(b, a)] = {"path": temp_list, "directions": temp_string}
                else:
                    if len(temp_list) < len(graph_memo[(b, a)]["path"]):
                        graph_memo[(b, a)] = {"path": temp_list, "directions": temp_string}
                if (b, a) not in queue:
                    queue.append((b, a))

        a = x

        b -= 1
        if 0 <= b < len(Board):
            if (b, a) not in visited:
                temp_list = list()
                for element in current_path:
                    temp_list.append(element)
                temp_list.append((b, a))
                temp_string = current_directions + "U"
                if (b, a) not in graph_memo:
                    graph_memo[(b, a)] = {"path": temp_list, "directions": temp_string}
                else:
                    if len(temp_list) < len(graph_memo[(b, a)]["path"]):
                        graph_memo[(b, a)] = {"path": temp_list, "directions": temp_string}
                if (b, a) not in queue:
                    queue.append((b, a))

        b += 2
        if 0 <= b < len(Board):
            if (b, a) not in visited:
                temp_list = list()
                for element in current_path:
                    temp_list.append(element)
                temp_list.append((b, a))
                temp_string = current_directions + "D"
                if (b, a) not in graph_memo:
                    graph_memo[(b, a)] = {"path": temp_list, "directions": temp_string}
                else:
                    if len(temp_list) < len(graph_memo[(b, a)]["path"]):
                        graph_memo[(b, a)] = {"path": temp_list, "directions": temp_string}
                if (b, a) not in queue:
                    queue.append((b, a))

        queue.pop(0)

    return None if Destination not in visited else (visited[Destination]["path"], visited[Destination]["directions"])

puzzle = [
['-', '-', '-', '-', '-'],
['-', '-', '#', '-', '-'],
['-', '-', '-', '-', '-'],
['#', '-', '#', '#', '-'],
['-', '#', '-', '-', '-']
]


print(solve_puzzle(puzzle, (0, 2), (2, 2)))
print(solve_puzzle(puzzle, (0, 0), (4, 4)))
print(solve_puzzle(puzzle, (0, 0), (4, 0)))
print(solve_puzzle(puzzle, (0, 0), (0, 0)))
print(solve_puzzle(puzzle, (0, 0), (1, 2)))
