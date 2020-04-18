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
    button_IDAstar = pygame.Rect(60, 400, 60, 30)
    button_IDDFS = pygame.Rect(150, 400, 60, 30)
    button_play = pygame.Rect(330, 100, 60, 30)
    button_reset = pygame.Rect(370, 350, 85, 30)
    button_restart = pygame.Rect(370, 400, 85, 30)
    button_speedup = pygame.Rect(370, 150, 30, 30)
    button_speeddown = pygame.Rect(330, 150, 30, 30)
    button_speedend = pygame.Rect(410, 150, 50, 30)
    big_font = pygame.font.Font('freesansbold.ttf', 32)
    small_font = pygame.font.Font(None, 25)

    current_state = puzzle.get_start_state()
    search_options = [search.a_star_search,
                      search.breadth_first_search,
                      search.depth_first_search]
    """ Game Mode:
    -1 = idle,
    -2 = ready to play animation,
    -3 = playing animation,
    >= 0: perform selected search
    """
    game_mode = -1

    # Create a timer
    clock = pygame.time.Clock()
    frame_rate = 1  # number of view changes per second

    # for animation purpose
    solution = []
    solution_index = 0

    running = True

    while running:
        # Perform selected search
        if game_mode >= 0:
            solution = search_summary.search_summary(
                search_options[game_mode], puzzle)
            game_mode = -2
            current_state = puzzle.get_start_state()

        # Handle the exit case
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if button_Astar.collidepoint(mouse_pos) and (game_mode == -1 or game_mode == -2):
                    game_mode = 0
                    solution_index = 0  # for animation purpose
                elif button_BFS.collidepoint(mouse_pos) and (game_mode == -1 or game_mode == -2):
                    game_mode = 1
                    solution_index = 0  # for animation purpose
                elif button_DFS.collidepoint(mouse_pos) and (game_mode == -1 or game_mode == -2):
                    game_mode = 2
                    solution_index = 0  # for animation purpose
                elif button_reset.collidepoint(mouse_pos) and (game_mode == -1 or game_mode == -2):
                    game_mode = -1
                    solution_index = 0  # for animation purpose
                    current_state = puzzle.get_start_state()
                elif button_restart.collidepoint(mouse_pos) and (game_mode == -1 or game_mode == -2):
                    game_mode = -1
                    solution_index = 0  # for animation purpose
                    puzzle.reset()
                    current_state = puzzle.get_start_state()
                elif button_play.collidepoint(mouse_pos) and game_mode == -2:
                    game_mode = -3
                    solution_index = 0  # for animation purpose
                elif button_speedup.collidepoint(mouse_pos) and game_mode == -3:
                    if frame_rate < 60:
                        frame_rate = int(frame_rate * 2)
                elif button_speeddown.collidepoint(mouse_pos) and game_mode == -3:
                    if frame_rate > 1:
                        frame_rate = int(frame_rate / 2)
                elif button_speedend.collidepoint(mouse_pos) and game_mode == -3:
                    solution_index = len(solution) - 1

        window.fill(WHITE)

        # Solution animation
        if game_mode == -3 and len(solution) > 0 and solution_index < len(solution):
            current_state = solution[solution_index]
            solution_index += 1

            count_animation = small_font.render(
                f'Step {solution_index} of {len(solution)}', True, BLACK)
            window.blit(count_animation, [330, 80])
        elif game_mode == -3:
            game_mode = -2
            frame_rate = 1
            solution_index = 0

        # Update puzzle state
        margin_y = 1
        for y in range(puzzle.dimension):
            margin_x = 1
            for x in range(puzzle.dimension):
                rect = pygame.Rect(x * block_size, y * block_size,
                                   block_size, block_size)
                pygame.draw.rect(window, BLACK, rect, 1)
                text = big_font.render(str(current_state[y][x]), True, BLACK)
                coordinate = (block_size * margin_x // 2,
                              block_size * margin_y // 2)
                window.blit(text, coordinate)
                margin_x += 2
            margin_y += 2

        # Draw different algo rects
        pygame.draw.rect(window, BROWN, button_Astar)
        pygame.draw.rect(window, BROWN, button_BFS)
        pygame.draw.rect(window, BROWN, button_DFS)
        pygame.draw.rect(window, BROWN, button_IDAstar)
        pygame.draw.rect(window, BROWN, button_IDDFS)
        pygame.draw.rect(window, BROWN, button_reset)
        pygame.draw.rect(window, BROWN, button_restart)
        astar = small_font.render("A*", True, WHITE)
        bfs = small_font.render("BFS", True, WHITE)
        dfs = small_font.render("DFS", True, WHITE)
        ida_star = small_font.render("IDA*", True, WHITE)
        iddfs = small_font.render("IDDFS", True, WHITE)
        reset = small_font.render('RESET', True, WHITE)
        restart = small_font.render('RESTART', True, WHITE)
        window.blit(astar, [80, 360])
        window.blit(bfs, [160, 360])
        window.blit(dfs, [250, 360])
        window.blit(ida_star, [70, 410])
        window.blit(iddfs, [155, 410])
        window.blit(reset, [380, 360])
        window.blit(restart, [375, 410])

        # Show Play button as needed
        if len(solution) > 0 and game_mode == -2:
            pygame.draw.rect(window, BROWN, button_play)
            play = small_font.render('PLAY', True, WHITE)
            window.blit(play, [335, 110])

        # Show -, +, END buttons on PLAY mode
        if game_mode == -3:
            pygame.draw.rect(window, BROWN, button_speedup)
            speedup = small_font.render('+', True, WHITE)
            window.blit(speedup, [380, 155])

            pygame.draw.rect(window, BROWN, button_speeddown)
            speeddown = small_font.render('-', True, WHITE)
            window.blit(speeddown, [340, 155])

            pygame.draw.rect(window, BROWN, button_speedend)
            speedend = small_font.render('END', True, WHITE)
            window.blit(speedend, [415, 160])

            speed_display = small_font.render(
                f'Frame Rate: {frame_rate}', True, BLACK)
            window.blit(speed_display, [330, 185])

        pygame.display.flip()

        clock.tick(frame_rate)

    pygame.quit()
