def create_board(size):
    return [[" " for _ in range(size)] for _ in range(size)]

def print_board(board):
    size = len(board)
    # The horizontal separator
    horizontal_sep = " ---" * size
    # Print the top border
    print(horizontal_sep)
    for row in range(size):
        # Print the row with vertical separators
        print("| " + " | ".join(board[row]) + " |")
        # Print the horizontal separator after each row
        print(horizontal_sep)

def check_win(board, player, row, col):
    size = len(board)
    # Check row
    if all(board[row][c] == player for c in range(size)):
        return True
    # Check column
    if all(board[r][col] == player for r in range(size)):
        return True
    # Check diagonal
    if row == col and all(board[i][i] == player for i in range(size)):
        return True
    if row + col == size - 1 and all(board[i][size - 1 - i] == player for i in range(size)):
        return True
    return False

def check_draw(board):
    return all(all(cell != " " for cell in row) for row in board)

def main():
    num_players = int(input("Enter number of players (2-4): "))
    while num_players not in range(2, 5):
        num_players = int(input("Invalid number. Enter number of players (2-4): "))

    symbols = ['X', 'O', '#', '@']
    player_names = [input(f"Enter player {i + 1} name: ") for i in range(num_players)]
    grid_size = int(input("Enter grid size (5-25): "))
    while grid_size < 5 or grid_size > 25:
        grid_size = int(input("Invalid size. Enter grid size (5-25): "))

    board = create_board(grid_size)
    player_turn = 0
    while True:
        print_board(board)
        current_player = player_turn % num_players
        print(f"{player_names[current_player]}'s turn ({symbols[current_player]}):")

        valid_move = False
        while not valid_move:
            try:
                row, col = map(int, input("Enter row and column numbers (e.g., 1 2): ").split())
                if board[row][col] == " ":
                    board[row][col] = symbols[current_player]
                    valid_move = True
                else:
                    print("Cell is already taken. Please try again.")
            except (IndexError, ValueError):
                print("Invalid input. Please try again.")

        if check_win(board, symbols[current_player], row, col):
            print_board(board)
            print(f"Congratulations, {player_names[current_player]} wins!")
            break
        if check_draw(board):
            print_board(board)
            print("The game is a draw.")
            break

        player_turn += 1

if __name__ == "__main__":
    main()