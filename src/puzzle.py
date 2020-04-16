import random
import copy

empty_space = ' '

""" Use this config for 8-puzzle (comment out other config) """
config = {
    'empty_space': empty_space,
    'goal_state': [[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, empty_space]],
    'dimension': 3,
    'num_of_shuffle_moves': 100,
    'initial_list': [1, 2, 3, 4, 5, 6, 7, 8, empty_space],
    'up': 'Up',
    'down': 'Down',
    'left': 'Left',
    'right': 'Right'
}

""" Use this config for 15-puzzle (comment out other config) """
# config = {
#     'empty_space': empty_space,
#     'goal_state': [[1, 2, 3, 4],
#                    [5, 6, 7, 8],
#                    [9, 10, 11, 12],
#                    [13, 14, 15, empty_space]],
#     'dimension': 4,
#     'num_of_shuffle_moves': 100,
#     'initial_list': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, empty_space],
#     'up': 'Up',
#     'down': 'Down',
#     'left': 'Left',
#     'right': 'Right'
# }

""" This example is to test code to see if we all get the same results (Line 44) """
# puzzle_example = [[2, 5, 4],
#                   [7, empty_space, 3],
#                   [8, 1, 6]]
# puzzle_example = [[8, 7, 4],
#                   [2, 6, 5],
#                   [' ', 1, 3]]


class Puzzle:
    def __init__(self):
        self.dimension = config['dimension']
        self.goal_state = config['goal_state']
        # self.start_state = self.__initialize_start_state()
        """ Option 1: Random Start State (Comment out one of the options) """
        self.start_state = self.__shuffle_goal_state(
            config['num_of_shuffle_moves'])

        """ Option 2: Fixed Start State: This is to test code under same example (Comment out one of the options) """
        # self.start_state = copy.deepcopy(puzzle_example)

        self.expanded_nodes = 0

    def is_goal_state(self, state):
        return state == self.goal_state

    def get_start_state(self):
        return copy.deepcopy(self.start_state)

    def __shuffle_goal_state(self, num_of_shuffle_moves):
        """ The shuffled state will always have a complete solution (i.e. Path cannot be None) """
        shuffled_state = copy.deepcopy(self.goal_state)
        for i in range(num_of_shuffle_moves):
            legal_actions = self.__get_legal_actions(shuffled_state)
            action = random.choice(legal_actions)
            shuffled_state = self.__get_successor_state(shuffled_state, action)
        return shuffled_state

    def __initialize_start_state(self):
        """
        The return state may have an incomplete solution (i.e. Path could be None)
        e.g.:
        [[1, 3],
         [2, ' ']]
        """
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
        legal_actions = self.__get_legal_actions(state)
        successors = []
        for action in legal_actions:
            successor_state = self.__get_successor_state(state, action)
            successors.append((successor_state, action, 1))
        self.expanded_nodes += 1
        return successors

    def __get_successor_state(self, state, action):
        next_state = copy.deepcopy(state)
        empty_location = self.__get_empty_location(state)
        if action == config['up']:
            tmp = next_state[empty_location[0] - 1][empty_location[1]]
            next_state[empty_location[0] -
                       1][empty_location[1]] = config['empty_space']
            next_state[empty_location[0]][empty_location[1]] = tmp
        elif action == config['down']:
            tmp = next_state[empty_location[0] + 1][empty_location[1]]
            next_state[empty_location[0] +
                       1][empty_location[1]] = config['empty_space']
            next_state[empty_location[0]][empty_location[1]] = tmp
        elif action == config['left']:
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

    def __get_legal_actions(self, state):
        empty_location = self.__get_empty_location(state)
        actions = []
        if empty_location[0] - 1 >= 0:
            actions.append(config['up'])
        if empty_location[0] + 1 < self.dimension:
            actions.append(config['down'])
        if empty_location[1] - 1 >= 0:
            actions.append(config['left'])
        if empty_location[1] + 1 < self.dimension:
            actions.append(config['right'])
        return actions

    def print_current_state(self, state):
        for i in range(self.dimension):
            print(state[i])
        print('')

    def print_solution(self, solution):
        for state in solution:
            self.print_current_state(state)

    def get_solution_as_list_of_states(self, path):
        """ Computes and returns the solution as a list of states from start_state to goal_state """
        state = self.start_state
        solution = []
        solution.append(copy.deepcopy(state))
        for action in path:
            state = self.__get_successor_state(state, action)
            solution.append(copy.deepcopy(state))
        return solution
