import puzzle
import search

if __name__ == '__main__':
    puzzle = puzzle.puzzle()
    path = search.depth_first_search(puzzle)
    print(path)
