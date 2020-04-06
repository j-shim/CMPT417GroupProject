import puzzle
import search
import time


def search_timer(selected_search, puzzle):
    start_time = time.time()
    actions = selected_search(puzzle)
    end_time = time.time()
    time_taken = end_time - start_time
    time_taken = round(time_taken, 1)
    print('Path:', actions)
    print('Path length:', search.get_cost_of_actions(actions))
    print('Time taken in seconds:', time_taken)


if __name__ == '__main__':
    puzzle = puzzle.puzzle()
    # selected_search = search.depth_first_search
    selected_search = search.breadth_first_search
    search_timer(selected_search, puzzle)
