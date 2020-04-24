import util
import copy


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


# ida* algorithm
# Reference used(pseudocode): https://en.wikipedia.org/wiki/Iterative_deepening_A*    

def search(path, g, bound, puzzle):
    node = copy.deepcopy(path.list[len(path.list) - 1])  # copy last element
    f = g + heuristic(node, puzzle)
    if f > bound:
        return False, f
    if puzzle.is_goal_state(node):
        return True, 0  # 0 is dummy value (don't need f value)
    min_value = float('inf')

    for succ in puzzle.get_successors(node):
        state, action, cost = succ  # don't need 'action' value
        if state not in path.list:
            path.push(state)
            found, new_bound = search(path, g + cost, bound, puzzle)
            if found:
                return found, 0  # 0 is dummy value
            if new_bound < min_value:
                min_value = new_bound
            path.pop()

    return False, min_value


def ida_star(puzzle):
    infinity = float('inf')
    start_state = puzzle.get_start_state()
    bound = heuristic(start_state, puzzle)
    # util.Stack is a class. Use util.Stack().list to return a list of states
    path = util.Stack()  # this will be the solution (list of states from start to goal)
    path.push(start_state)
    while True:
        found, new_bound = search(path, 0, bound, puzzle)
        if found:
            # path.list is a list of states: for consistency with other search functions, we return a list of actions (e.g. ["Up", "Left", "Right"])
            return puzzle.convert_solution_from_states_to_actions(path.list)
        if new_bound >= infinity:
            return None
        bound = new_bound


# iddfs function
# non-recursion version
# Reference used(pseudocode): https://en.wikipedia.org/wiki/Iterative_deepening_depth-first_search

def iddfs_search_no_recursive(puzzle):
    max_int = 999999
    for max_depth in range(max_int):
        found, remaining = depth_limited_dfs_no_recursive(puzzle, max_depth)
        if found is not None:
            return found
        elif not remaining:
            return None


def depth_limited_dfs_no_recursive(puzzle, max_depth):
    fringe = util.Stack()
    start_state = puzzle.get_start_state()
    root_depth = 0
    any_remaining = False
    fringe.push((start_state, root_depth))
    expanded = util.Counter()
    parent = {}
    while True:
        if fringe.isEmpty():
            return None, any_remaining

        node, node_depth = fringe.pop()

        if puzzle.is_goal_state(node):
            return backtrace(start_state, node, parent), any_remaining

        expanded[str(node)] += 1

        successors = puzzle.get_successors(node)
        if node_depth < max_depth:
            for successor in successors:
                state, action, cost = successor
                if expanded[str(state)] == 0:
                    fringe.push((state, node_depth + 1))
                    parent[str(state)] = (str(node), action)
        elif len(successors) > 0:
            any_remaining = True


# recursion version

def iddfs_search(puzzle):
    max_int = 999999
    start_state = puzzle.get_start_state()
    for depth in range(max_int):
        expanded = util.Counter()
        parent = {}
        found, remaining = depth_limited_dfs(
            puzzle, start_state, depth, expanded, parent)
        if found is not None:
            return backtrace(start_state, found, parent)
        elif not remaining:
            return None


def depth_limited_dfs(puzzle, current_state, depth, expanded, parent):
    if depth == 0:
        if puzzle.is_goal_state(current_state):
            return (current_state, True)
        else:
            return (None, True)  # (Not found, but may have children)
    elif depth > 0:
        any_remaining = False

        expanded[str(current_state)] += 1
        successor_states = puzzle.get_successors(current_state)
        for successor in successor_states:
            state, action, cost = successor
            if expanded[str(state)] == 0:
                parent[str(state)] = (str(current_state), action)

                found, remaining = depth_limited_dfs(
                    puzzle, state, depth - 1, expanded, parent)
                if found is not None:
                    return (found, True)
                if remaining:
                    # (At least one node found at depth, let IDDFS deepen)
                    any_remaining = True
        return (None, any_remaining)