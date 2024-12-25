from typing import List, Tuple

class Board:
    mask: int
    pieces: List[Tuple[Tuple[int, int], Tuple[Tuple[int, int]]]]

    def __init__(self, month, day, week_day):
    

    def get_matrix_board(self):
        matrix_board = [[None]*7 for _ in range(8)] # 7x8 matrix
        months = ["JAN", "FAB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]
        for i, month in enumerate(months):
            matrix_board[i//6][i%6] = month

        for i, day in enumerate(range(1, 32)):
            matrix_board[2+i//7][i%7] = str(day)

        days = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
        for i, day in enumerate(days):
            if i < 4:
                matrix_board[6][i + 3] = day
            else:
                matrix_board[7][i] = day
        return matrix_board
    def to_string(self):
        s = ""
        s += "+" + "-" * 21 + "+\n"
        for row in :
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
