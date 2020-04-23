import util


def depth_first_search(puzzle):
    fringe = util.Stack()
    start_state = puzzle.get_start_state()
    fringe.push(start_state)
    expanded = util.Counter()
    parent = {}
    while True:
        if fringe.isEmpty():
            return None

        node = fringe.pop()

        if puzzle.is_goal_state(node):
            return backtrace(start_state, node, parent)

        expanded[str(node)] += 1

        for successor in puzzle.get_successors(node):
            state, action, cost = successor
            if expanded[str(state)] == 0:
                fringe.push(state)
                parent[str(state)] = (str(node), action)


def backtrace(start_state, goal_state, parent):
    actions = []
    key = str(goal_state)
    while True:
        if key == str(start_state):
            actions.reverse()
            return actions
        actions.append(parent[key][1])
        key = parent[key][0]


def breadth_first_search(puzzle):
    fringe = util.Queue()
    start_state = puzzle.get_start_state()
    fringe.push(start_state)
    in_fringe = util.Counter()
    in_fringe[str(start_state)] += 1
    parent = {}
    while True:
        if fringe.isEmpty():
            return None

        node = fringe.pop()

        if puzzle.is_goal_state(node):
            return backtrace(start_state, node, parent)

        for successor in puzzle.get_successors(node):
            state, action, cost = successor
            if in_fringe[str(state)] == 0:
                fringe.push(state)
                parent[str(state)] = (str(node), action)
                in_fringe[str(state)] += 1


def heuristic(state, puzzle):
    """ heuristic = (sum of manhattanDistance(current_position, goal_position)) / 2 """
    h = 0
    for i in range(puzzle.dimension):
        for j in range(puzzle.dimension):
            # (0, 0) -> 1 as value, (0, 2) -> 3 as value, etc
            value = i * puzzle.dimension + j + 1
            if value == puzzle.dimension ** 2:  # value is ' '
                value = ' '
            current_position = puzzle.get_coordinates(state, value)
            goal_position = (i, j)
            h += util.manhattanDistance(current_position, goal_position)
    h /= 2
    return h


def a_star_search(puzzle):
    # Reference used(pseudocode): https://en.wikipedia.org/wiki/A*_search_algorithm
    fringe = util.PriorityQueue()
    start_state = puzzle.get_start_state()
    fringe.push(start_state, heuristic(start_state, puzzle))
    expanded = util.Counter()
    g = {}
    g[str(start_state)] = 0
    f = {}
    f[str(start_state)] = heuristic(start_state, puzzle)
    parent = {}
    while True:
        if fringe.isEmpty():
            return None

        node = fringe.pop()

        if puzzle.is_goal_state(node):
            return backtrace(start_state, node, parent)

        expanded[str(node)] += 1

        for successor in puzzle.get_successors(node):
            state, action, cost = successor
            tentative_g = g[str(node)] + cost
            if g.get(str(state)) == None or tentative_g < g.get(str(state)):
                if expanded[str(state)] == 0:
                    parent[str(state)] = (str(node), action)
                    g[str(state)] = tentative_g
                    f[str(state)] = g[str(state)] + heuristic(state, puzzle)
                    fringe.update(state, f[str(state)])


def search(path, g, bound, puzzle, expanded, parent):
    node = path.pop()
    f = g + heuristic(node, puzzle)
    if f > bound:
        return f
    if puzzle.is_goal_state(node):
        return True
    min = float("inf")

    for succ in puzzle.get_successors(node):
        state, action, cost = succ
        path.push(succ)
        if expanded[str(state)] == 0:
            parent[str(state)] = (str(node), action)
            expanded[str(node)] += 1
        t, p = search(path, g + cost, bound, puzzle, expanded, parent)
        if t == True:
            return True, p, node
        if t < min:
            min = t
        path.pop()

    return min, parent


def ida_star(puzzle):
    start_state = puzzle.get_start_state()
    bound = heuristic(start_state, puzzle)
    path = util.Stack()
    path.push(start_state)
    ##### ???
    parent = {}
    expanded = util.Counter()
    #####
    while True:
        if path.isEmpty():
            return None        
        t, p, node = search(path, 0, bound, puzzle, expanded, parent)
        if t == True:
            return backtrace(start_state, node, p)
        else:
            return None
        bound = t