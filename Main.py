def initialize_board(size):
    return [[" " for _ in range(size)] for _ in range(size)]


def print_board(board):
    size = len(board)
    for row in board:
        print("__" + "__|__".join(row) + "__")
        print("  " + "  |  " * size)
    print("\n")


def check_win(board, player_symbol):
    size = len(board)
    # Check horizontal and vertical lines
    for i in range(size):
        if all(board[i][j] == player_symbol for j in range(size)) or all(
                board[j][i] == player_symbol for j in range(size)):
            return True
    # Check diagonals
    if all(board[i][i] == player_symbol for i in range(size)) or all(
            board[i][size - 1 - i] == player_symbol for i in range(size)):
        return True
    return False


def is_board_full(board):
    return all(cell != " " for row in board for cell in row)


def main():
    size = int(input("Enter the size of the board (5 to 25): "))
    if not (5 <= size <= 25):
        print("Invalid size. Using default 5x5.")
        size = 5

    num_players = int(input("Enter number of players (2 to 4): "))
    if not (2 <= num_players <= 4):
        print("Invalid number of players. Using 2 players.")
        num_players = 2

    symbols = ["X", "O", "#", "@"]
    players = [input(f"Enter player {i + 1} name: ") for i in range(num_players)]
    player_symbols = symbols[:num_players]

    board = initialize_board(size)
    current_player = 0

    while True:
        print_board(board)
        print(f"{players[current_player]}'s turn ({player_symbols[current_player]}): ")
        try:
            x, y = map(int, input("Enter row and column numbers (e.g., 1 2 for row 1, column 2): ").split())
            if board[x - 1][y - 1] != " ":
                print("Cell is already taken. Choose another cell.")
                continue
        except (ValueError, IndexError):
            print("Invalid input. Please enter row and column numbers within the grid size.")
            continue

        board[x - 1][y - 1] = player_symbols[current_player]
        if check_win(board, player_symbols[current_player]):
            print_board(board)
            print(f"{players[current_player]} wins!")
            break
        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = (current_player + 1) % num_players


if __name__ == "__main__":
    main()
