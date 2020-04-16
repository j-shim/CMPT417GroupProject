import time
import tracemalloc  # for memory tracking


def search_summary(selected_search, puzzle):
    print(f'***** {selected_search.__name__} *****')
    start_time = time.time()  # start timer

    tracemalloc.start()  # start memory tracking
    initial_mem, _ = tracemalloc.get_traced_memory()
    actions = selected_search(puzzle)  # perform search algorithm
    current_mem, peak_mem = tracemalloc.get_traced_memory()
    tracemalloc.stop()  # stop memory tracking

    end_time = time.time()  # end timer
    time_taken = end_time - start_time

    time_taken = round(time_taken, 2)
    # Convert to MiB
    initial_mem = round(initial_mem / (1024 ** 2), 6)
    current_mem = round(current_mem / (1024 ** 2), 6)
    peak_mem = round(peak_mem / (1024 ** 2), 6)

    # print(f'Path -----------------------------------------> {actions}')
    print(
        f'Path length ----------------------------------> {get_cost_of_actions(actions)} actions')
    print(
        f'Time taken in seconds ------------------------> {time_taken} seconds')
    print(
        f'Expanded nodes -------------------------------> {puzzle.expanded_nodes} nodes')
    print(
        f'Initial memory is ----------------------------> {initial_mem} MiB')
    print(
        f'Current memory is ----------------------------> {current_mem} MiB')
    print(
        f'Peak memory is -------------------------------> {peak_mem} MiB (=Memory Usage)')
    print('')

    return actions


def get_cost_of_actions(actions):
    if actions is None:
        return None
    return len(actions)
