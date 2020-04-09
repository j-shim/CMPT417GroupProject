import puzzle
import search
import time


def search_timer(selected_search, puzzle):
    print(selected_search.__name__)
    start_time = time.time()
    actions = selected_search(puzzle)
    end_time = time.time()
    time_taken = end_time - start_time
    time_taken = round(time_taken, 1)
    print('Path:', actions)
    print('Path length:', search.get_cost_of_actions(actions))
    print('Time taken in seconds:', time_taken)
    print('Expanded nodes:', puzzle.expanded_nodes)
    print('Verify Path leads Start State to Goal State:',
          puzzle.verify_computed_path(actions))
    print('')


if __name__ == '__main__':
    puzzle_instance = puzzle.puzzle()
    # selected_search = search.depth_first_search
    # selected_search = search.breadth_first_search
    # selected_search = search.a_star_search
    searches = [search.depth_first_search,
                search.breadth_first_search,
                search.a_star_search]
    for selected_search in searches:
        search_timer(selected_search, puzzle_instance)
    puzzle_instance.print_start_state()
