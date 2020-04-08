import random
import copy

empty_space = ' '
config = {
    'empty_space': empty_space,
    'goal_state': [[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, empty_space]],
    'dimension': 3,
    'initial_list': [1, 2, 3, 4, 5, 6, 7, 8, empty_space]
}

# config = {
#     'goal_state': [[1, 2],
#                    [3, ' ']],
#     'dimension': 2,
#     'initial_list': [1, 2, 3, ' ']
# }


class puzzle:
    def __init__(self):
        self.dimension = config['dimension']
        self.goal_state = config['goal_state']
        self.start_state = self.__initialize_start_state()
        self.expanded_nodes = 0

    def is_goal_state(self, state):
        return state == self.goal_state

    def get_start_state(self):
        return self.start_state

    def __initialize_start_state(self):
        initial_list = config['initial_list']
        random_puzzle = []
        for i in range(self.dimension):
            row = []
            for j in range(self.dimension):
                chosen = random.choice(initial_list)
                initial_list.remove(chosen)
                row.append(chosen)
            random_puzzle.append(row)
        return random_puzzle

    def __get_empty_location(self, state):
        for i in range(self.dimension):
            for j in range(self.dimension):
                if state[i][j] == config['empty_space']:
                    return i, j
        return None  # this should never happen

    def get_successors(self, state):
        legal_actions = self.get_legal_actions(state)
        successors = []
        for action in legal_actions:
            successor_state = self.__get_successor_state(state, action)
            successors.append((successor_state, action, 1))
        self.expanded_nodes += 1
        return successors

    def __get_successor_state(self, state, action):
        next_state = copy.deepcopy(state)
        empty_location = self.__get_empty_location(state)
        if action == 'Up':
            tmp = next_state[empty_location[0] - 1][empty_location[1]]
            next_state[empty_location[0] -
                       1][empty_location[1]] = config['empty_space']
            next_state[empty_location[0]][empty_location[1]] = tmp
        elif action == 'Down':
            tmp = next_state[empty_location[0] + 1][empty_location[1]]
            next_state[empty_location[0] +
                       1][empty_location[1]] = config['empty_space']
            next_state[empty_location[0]][empty_location[1]] = tmp
        elif action == 'Left':
            tmp = next_state[empty_location[0]][empty_location[1] - 1]
            next_state[empty_location[0]][empty_location[1] -
                                          1] = config['empty_space']
            next_state[empty_location[0]][empty_location[1]] = tmp
        else:  # 'Right'
            tmp = next_state[empty_location[0]][empty_location[1] + 1]
            next_state[empty_location[0]][empty_location[1] +
                                          1] = config['empty_space']
            next_state[empty_location[0]][empty_location[1]] = tmp
        return next_state

    def get_legal_actions(self, state):
        empty_location = self.__get_empty_location(state)
        actions = []
        if empty_location[0] - 1 >= 0:
            actions.append('Up')
        if empty_location[0] + 1 < self.dimension:
            actions.append('Down')
        if empty_location[1] - 1 >= 0:
            actions.append('Left')
        if empty_location[1] + 1 < self.dimension:
            actions.append('Right')
        return actions
