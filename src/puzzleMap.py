import pygame
import sys
import random
import search
import search_summary
from pygame.locals import *


def init(puzzle):
    # some colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    BROWN = (150, 75, 0)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)

    # screen basic parameters
    width = 500
    height = 500
    block_size = 100

    pygame.init()
    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption('3x3 Sliding Puzzle')
    button_Astar = pygame.Rect(60, 350, 60, 30)
    button_BFS = pygame.Rect(150, 350, 60, 30)
    button_DFS = pygame.Rect(240, 350, 60, 30)
    button_IDAstar = pygame.Rect(330, 350, 60, 30)
    button_IDDFS = pygame.Rect(60, 400, 60, 30)
    big_font = pygame.font.Font('freesansbold.ttf', 32)
    small_font = pygame.font.Font(None, 25)

    # Just for test, need import more cases
    # TODO: how to combine our code? also need to uniform the format
    # June: for now I'll create puzzle instance from main.py and pass it to this function as an argument
    # Passing it as an argument rather than instantiating it here lets us use the same start state for different search algorithms
    current_state = puzzle.get_start_state()

    # Create a timer
    clock = pygame.time.Clock()
    frame_rate = 60
    time_count = 0

    click = False
    # Path stored as list of actions (e.g. [Up, Down, Left, Right, Down])
    actions = None
    solution = []  # for animation purpose
    solution_index = 0  # for animation purpose

    while True:
        # Handle the exit case
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if button_Astar.collidepoint(mouse_pos):
                    click = True
                    solution_index = 0  # for animation purpose
                    actions = search_summary.search_summary(
                        search.a_star_search, puzzle)
                    # TODO: maybe we should stop timer, or moreover, should we be able to stop timer..? not sure about this
                    # Also path is stored in actions, might be useful for animation (also take a look at puzzle.verify_computed_path(path))

                    # for animation purpose
                    solution = puzzle.get_solution_as_list_of_states(actions)
                elif button_BFS.collidepoint(mouse_pos):
                    click = True
                    actions = search_summary.search_summary(
                        search.breadth_first_search, puzzle)
                elif button_DFS.collidepoint(mouse_pos):
                    click = True
                    actions = search_summary.search_summary(
                        search.depth_first_search, puzzle)

        window.fill(WHITE)

        margin_y = 1
        for y in range(puzzle.dimension):
            margin_x = 1
            for x in range(puzzle.dimension):
                rect = pygame.Rect(x*block_size, y*block_size,
                                   block_size, block_size)
                pygame.draw.rect(window, BLACK, rect, 1)
                text = big_font.render(str(current_state[y][x]), True, BLACK)
                coordinate = (block_size*margin_x // 2,
                              block_size*margin_y // 2)
                window.blit(text, coordinate)
                margin_x += 2
            margin_y += 2

        # Doing the time count
        # NOTE: It seems like while search algorithm is being executed, this if block is not executed (I don't think pygame is asynchronous)
        # As a result the clock ticks only after search algorithm is finished
        if click == True:
            total_seconds = time_count // frame_rate
            minutes = total_seconds // 60
            seconds = total_seconds % 60
            output_time = "{0:02}:{1:02}".format(minutes, seconds)
            time_text = small_font.render(output_time, True, BLACK)
            pygame.draw.ellipse(window, RED, [330, 85, 80, 50], 5)
            window.blit(time_text, [350, 100])

            time_count += 1
            clock.tick(frame_rate)

        # Solution animation
        # just a basic guideline of how the animation would be, using necessary variables
        # Not sure how to further improve this..
        if len(solution) > 0 and solution_index < len(solution):
            current_state = solution[solution_index]
            solution_index += 1

        # Draw different algo rects
        pygame.draw.rect(window, BROWN, button_Astar)
        pygame.draw.rect(window, BROWN, button_BFS)
        pygame.draw.rect(window, BROWN, button_DFS)
        pygame.draw.rect(window, BROWN, button_IDAstar)
        pygame.draw.rect(window, BROWN, button_IDDFS)
        astar = small_font.render("A*", True, WHITE)
        bfs = small_font.render("BFS", True, WHITE)
        dfs = small_font.render("DFS", True, WHITE)
        ida_star = small_font.render("IDA*", True, WHITE)
        iddfs = small_font.render("IDDFS", True, WHITE)
        window.blit(astar, [80, 360])
        window.blit(bfs, [160, 360])
        window.blit(dfs, [250, 360])
        window.blit(ida_star, [340, 360])
        window.blit(iddfs, [65, 410])

        pygame.display.flip()
