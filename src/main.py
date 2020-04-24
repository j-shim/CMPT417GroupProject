import puzzle
import puzzleMap
import os

if __name__ == '__main__':
    # clear all reports in result files
    # we assume 10 is the max round times that user will play
    for i in range(20):
        fileName = f'algo_summary_report{i}.txt'
        if os.path.exists("result/"+fileName):
            os.remove("result/"+fileName)

    # set up the new puzzle
    puzzle_instance = puzzle.Puzzle()
    # running the puzzle ...
    puzzleMap.init(puzzle_instance)
