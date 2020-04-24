import time
import tracemalloc  # for memory tracking


def search_summary(selected_search, puzzle, round_times):
    print('')
    print(f'***** {selected_search.__name__} *****')
    print('Search Algorithm in Progress ...\n')
    export_text = f'\n***** {selected_search.__name__} *****\n'
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

    print('Done.\n')

    if actions is not None:
        if len(actions) < 30:
            print(f'Path -------------------------------> {actions}')
            export_text += f'Path -------------------------------> {actions}\n'
        else:
            print(
                f'Path -------------------------------> {actions[0:29]} ...too long, omit rest actions')
            export_text += f'Path -------------------------------> {actions[0:29]} ...too long, omit rest actions\n'
        print(
            f'Path length --------------------------------> {get_cost_of_actions(actions)} actions')
        export_text += f'Path length --------------------------------> {get_cost_of_actions(actions)} actions\n'
    print(
        f'Time taken in seconds ----------------------> {time_taken} seconds')
    export_text += f'Time taken in seconds ----------------------> {time_taken} seconds\n'
    print(
        f'Expanded nodes -----------------------------> {puzzle.expanded_nodes} nodes')
    export_text += f'Expanded nodes -----------------------------> {puzzle.expanded_nodes} nodes\n'
    print(
        f'Initial memory is --------------------------> {initial_mem} MiB')
    export_text += f'Initial memory is --------------------------> {initial_mem} MiB\n'
    print(
        f'Current memory is --------------------------> {current_mem} MiB')
    export_text += f'Current memory is --------------------------> {current_mem} MiB\n'
    print(
        f'Peak memory is -----------------------------> {peak_mem} MiB (=Memory Usage)')
    export_text += f'Peak memory is -----------------------------> {peak_mem} MiB (=Memory Usage)\n'

    print('Preparing Solution for Animation ...\n')
    solution=puzzle.get_solution_as_list_of_states(actions)
    print('Done.\n')

    # Export the collected data to .txt file for better user reading
    fileName = f'algo_summary_report{round_times}.txt'
    export_file = open('result/'+fileName, 'a')
    export_file.write(export_text)
    export_file.close()

    return solution


def get_cost_of_actions(actions):
    if actions is None:
        return None
    return len(actions)
