from pieces import PIECES
from board import BOARD
import functools
import time


def get_rotations(piece):
    rotations = []
    for _ in range(4):
        rotations.append(piece)
        piece = tuple(sorted((-p[1], p[0]) for p in piece))
    return tuple(rotations)


def flip(piece):
    return tuple(sorted([(p[0], -p[1]) for p in piece]))

def move_origin(piece):
    min_x = min(x for x, y in piece)
    min_y = min(y for x, y in piece)
    return tuple(sorted((x - min_x, y - min_y) for x, y in piece))

@functools.cache
def get_all_rotations_and_flip(piece):
    rotations = get_rotations(piece)
    flipped_rotation = get_rotations(flip(piece))
    r = set()
    for rotation in rotations:
        r.add(move_origin(rotation))
    for rotation in flipped_rotation:
        r.add(move_origin(rotation))
    return r

def get_all_pos_for_piece(piece, other_pieces, board):
    positions = set()
    for y in range(len(board)):
        for x in range(len(board[0])):
            for rotation in get_all_rotations_and_flip(piece):
                if all(is_valid_piece(rotation, other_pieces, board, x, y) for px, py in rotation):
                    positions.add((x, y, rotation))
    return positions

def is_valid_piece(piece, other_pieces, board, x, y):
    for px, py in piece:
        if x + px < 0 or x + px >= len(board[0]) or y + py < 0 or y + py >= len(board):
            return False
        if board[y + py][x + px] != -1:
            return False
    for px, py in piece:
        board[y + py][x + px] = 1
    valid = True
    for px, py in piece:
        if not valid:
            break
        for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            nx, ny = x + px + dx, y + py + dy
            if nx < 0 or nx >= len(board[0]) or ny < 0 or ny >= len(board):
                continue
            if board[ny][nx] == -1:
                visited = set()
                subdfs(board, (nx, ny), visited)
                if not(len(visited) in valid_number_holes(other_pieces, len(board[0]), len(board))):
                    valid = False
                    break
    for px, py in piece:
        board[y + py][x + px] = -1
    return valid

@functools.cache
def valid_number_holes(other_pieces, width, height):
    s = set()
    piece_length = list(map(len, other_pieces))
    nb_four = piece_length.count(4)
    nb_five = piece_length.count(5)
    for i in range(1, width * height + 1):
        n_4 = nb_four
        n_i = i
        while n_i > 0:
            if n_i % 5 == 0 and nb_five >= n_i // 5:
                s.add(i)
                break
            elif n_4 > 0:
                n_i -= 4
                n_4 -= 1
            else:
                break
        if n_i == 0:
            s.add(i)
    return s

def subdfs(board, start_pos, visited):
    visited.add(start_pos)
    for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
        nx, ny = start_pos[0] + dx, start_pos[1] + dy
        if nx < 0 or nx >= len(board[0]) or ny < 0 or ny >= len(board):
            continue
        if (nx, ny) in visited:
            continue
        if board[ny][nx] == -1:
            subdfs(board, (nx, ny), visited)

def dfs(board, pieces, piece_idx, solutions=[]):
    if piece_idx == len(pieces):
        solutions.append([list(row) for row in board])
        print(pretty_print_board(board))
        return
    piece = pieces[piece_idx]
    other_pieces = tuple(pieces[piece_idx + 1:]) if piece_idx + 1 < len(pieces) else ()
    all_possibilities = get_all_pos_for_piece(piece,other_pieces, board)
    for i, (x, y, rotation) in enumerate(all_possibilities):
        if piece_idx == 0:
            print(f"working on possibility {i+1}/{len(all_possibilities)}")
        for px, py in rotation:
            board[y + py][x + px] = piece_idx
        dfs(board, pieces, piece_idx + 1, solutions)
        for px, py in rotation:
            board[y + py][x + px] = -1
    return solutions


def transform_board(board, month, day, week_day):
    for y in range(len(board)):
        for x in range(len(board[0])):
            if board[y][x] == month or board[y][x] == day or board[y][x] == week_day:
                continue
            if board[y][x] is None:
                continue
            board[y][x] = -1
    return board

def pretty_print_board(board):
    s = ""
    s += "+" + "-" * 21 + "+\n"
    for row in board:
        s += "|"
        for cell in row:
            if cell == None:
                s+= "###"
            elif cell == -1:
                s += "   "
            elif type(cell) == str:
                assert len(cell) <= 3
                s += cell + " " * (3 - len(cell))
            else:
                s += f" {cell} "
        s += "|\n"
    s += "+" + "-" * 21 + "+\n"
    return s


if __name__ == "__main__":

    start_time = time.time()
    month = "DEC"
    day = "24"
    week_day = "TUE"

    day_board = transform_board(BOARD, month, day, week_day)
    print(pretty_print_board(day_board))
    solutions = []
    dfs(day_board, PIECES, 0,solutions)

    with open(f"solutions/{month}_{day}_{week_day}.txt", "w") as f:
        for board in solutions:
            f.write(pretty_print_board(board))
        f.write(str(len(solutions)))
    print(f"finished in {time.time() - start_time} seconds")