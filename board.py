from pprint import pprint
BOARD = [[None]*7 for _ in range(8)] # 7x8 matrix
months = ["JAN", "FAB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]
for i, month in enumerate(months):
    BOARD[i//6][i%6] = month

for i, day in enumerate(range(1, 32)):
    BOARD[2+i//7][i%7] = str(day)

days = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
for i, day in enumerate(days):
    if i < 4:
        BOARD[6][i + 3] = day
    else:
        BOARD[7][i] = day


if __name__ == "__main__":
    pprint(BOARD)