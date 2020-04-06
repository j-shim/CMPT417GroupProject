import util


def depth_first_search(puzzle):
    fringe = util.Stack()
    start_state = puzzle.get_start_state()
    print(start_state)
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
            state, action = successor
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


def get_cost_of_actions(actions):
    return len(actions)


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
            state, action = successor
            if in_fringe[str(state)] == 0:
                fringe.push(state)
                parent[str(state)] = (str(node), action)
                in_fringe[str(state)] += 1
