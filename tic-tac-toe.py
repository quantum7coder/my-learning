#SHOW BOARD
def print_board(board):
    """Prints the board in a formatted way"""
    for row in board:
        print(" | ".join(row))
        print("-" * (4 * len(board[0]) - 3))

#CHECK FOR WINNER
def check_winner(board, symbol, k):
    """Check if the given symbol has won with k in a row"""
    m, n = len(board), len(board[0])
    for i in range(m):
        for j in range(n - k + 1):
            if all(board[i][j + d] == symbol for d in range(k)):
                return True
    for i in range(m - k + 1):
        for j in range(n):
            if all(board[i + d][j] == symbol for d in range(k)):
                return True
    for i in range(m - k + 1):
        for j in range(n - k + 1):
            if all(board[i + d][j + d] == symbol for d in range(k)):
                return True
    for i in range(m - k + 1):
        for j in range(k - 1, n):
            if all(board[i + d][j - d] == symbol for d in range(k)):
                return True
    return False

#RUN THE GAME
def tic_tac_toe():
    m = int(input("Enter number of rows (m): "))
    n = int(input("Enter number of columns (n): "))
    k = int(input("Enter number of consecutive marks to win: "))
    board = [[" " for _ in range(n)] for _ in range(m)]
    players = [("User1", "X"), ("User2", "O")]
    total_moves = m * n
    print("\nGame Start!\n")
    print_board(board)
    for move in range(total_moves):
        player_name, symbol = players[move % 2]
        print(f"\n{player_name}'s turn ({symbol})")
        while True:
            try:
                r = int(input(f"Enter row (0-{m-1}): "))
                c = int(input(f"Enter col (0-{n-1}): "))

                if 0 <= r < m and 0 <= c < n and board[r][c] == " ":
                    board[r][c] = symbol
                    break
                else:
                    print("Invalid move. Try again.")
            except ValueError:
                print("Invalid input. Enter integers only.")

        print_board(board)
        if check_winner(board, symbol, k):
            print(f"\n{player_name} ({symbol}) WINS! 🎉")
            return
    print("\nIt's a DRAW!")
tic_tac_toe()
