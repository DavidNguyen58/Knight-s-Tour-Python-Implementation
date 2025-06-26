import time
def print_board(state):
    for row in state:
        print(row)


def board(n):
    return [[0] * n for _ in range(n)]


def validate(pos, n):
    x, y = pos
    return 0 <= x < n and 0 <= y < n


def warnsdorf_heuristic(pos, dirs, visited, n):
    """
    Heuristic Search: Move the knight to a position with the least possible number of moves
    """
    def calculate_moves(pos, dirs, visited, n):
        x, y = pos
        count = 0

        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if not validate((nx, ny), n) or (nx, ny) in visited:
                continue
            count += 1
        
        return count
    
    x, y = pos
    moves = []

    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        if not validate((nx, ny), n) or (nx, ny) in visited:
            continue
        count = calculate_moves((nx, ny), dirs, visited, n)
        moves.append((count, (nx, ny)))
    
    moves.sort(key=lambda x: x[0])
    return [move for _, move in moves]


def search(state, src, dirs, dst, visited, res=[]):
    """
    DFS Search Method
    """
    N = len(state)
    x, y = src
    visited.add(src)
    state[x][y] = dst

    if len(visited) == len(state) * len(state[0]):
        return True
    
    for nx, ny in warnsdorf_heuristic(src, dirs, visited, N):
        if not validate((nx, ny), len(state)) or (nx, ny) in visited:
            continue
        if search(state, (nx, ny), dirs, dst + 1, visited, res):
            res.append((nx, ny))
            return True
    
    visited.remove(src)
    state[x][y] = 0
    return False


if __name__ == "__main__":
    n = 5

    state = board(n)
    dirs = [
        (2, 1), (1, 2), (-1, 2), (-2, 1),
        (-2, -1), (-1, -2), (1, -2), (2, -1)
    ]

    src = (0, 0)
    visited = set()
    res = []

    start = time.time()
    ans = search(state, src, dirs, 0, visited, res)
    end = time.time()

    print(f"The time it takes to run {end - start}.")
    if ans:
        print(f"The sequence of moves is {res}")
        print_board(state)