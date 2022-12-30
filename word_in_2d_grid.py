# find words in grid
from typing import List, Tuple

class Case:
    def __init__(self, grid: List[List[str]], word: str, expect: List[Tuple[int, int]]):
        self.grid = grid
        self.word = word
        self.expect = expect

def print_debug(msg: str):
    if debug:
        print(msg)
def find_in_grid(grid: List[List[str]], word: str) -> List[Tuple[int, int]]:
    result = []

    # Find the first character
    x = 0
    y = 0
    pos = 0
    max_height = len(grid)
    max_width = len(grid[0])
    print_debug(f"Max height[{max_height}] width[{max_width}]")

    # Find first character
    first_chars = []
    while y < max_height:
        x = 0
        while x < max_width:
            print_debug(f"check x[{x}] y[{y}]")
            if grid[y][x] == word[0]:
                first_chars.append((x, y))
            x += 1
        y += 1
    print_debug(f"first_char: {first_chars}")

    for f in first_chars:
        result = [f]
        r = check_and_move(grid, word, pos + 1, f[0], f[1])
        result += r
        if len(result) == len(word):
            break

    if len(result) != len(word):
        return []

    return result

def check_and_move(grid: List[List[str]], word: str, pos: int, x: int, y: int):
    max_height = len(grid)
    max_width = len(grid[0])
    if x >= max_width or y >= max_height or pos >= len(word):
        return []
    result = []
    paths = [(x + 1, y), (x, y + 1)]
    for p in paths:
        tx, ty = p
        print_debug(f"Check {pos} in {word} == {grid[ty][tx]} at [{tx}, {ty}]")
        if word[pos] == grid[ty][tx]:
            result.append((tx, ty))
            if pos < len(word) - 1:
                r = check_and_move(grid, word, pos + 1, tx, ty)
                result += r
            print_debug(f"cam return: {result}")
            return result
    return []
        

debug = False
if __name__ == "__main__":
    g = [
        ["A", "T", "R", "V", "B", "E"],
        ["R", "T", "A", "O", "L", "E"],
        ["A", "M", "C", "K", "T", "E"],
        ["N", "O", "R", "E", "B", "G"],
    ]
    c1 = Case(g, "ART", [(0, 0), (0, 1), (1, 1)])
    c2 = Case(g, "ATTACK", [(0, 0), (1, 0), (1, 1), (2, 1), (2, 2), (3, 2)])
    c3 = Case(g, "VOLT", [(3, 0), (3, 1), (4, 1), (4, 2)])
    cases = [c1, c2, c3]
    for c in cases:
        result = find_in_grid(c.grid, c.word)
        print(f"case[{c.word}] {'PASS' if result == c.expect else 'FAIL'} Expect:<{c.expect}> Got:<{result}>")
        assert result == c.expect