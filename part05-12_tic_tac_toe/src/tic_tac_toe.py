# Write your solution here
def play_turn(game_board: list, x: int, y: int, piece: str) -> bool:
    # Check if the coordinates are valid
    if x < 0 or x > 2 or y < 0 or y > 2:
        return False

    # Check if the square is empty
    if game_board[y][x] == "":
        # Place the symbol on the game board
        game_board[y][x] = piece
        return True
    else:
        return False

if __name__ == "__main__":

    # Example usage
    game_board = [["", "", ""], ["", "", ""], ["", "", ""]]
    print(play_turn(game_board, 2, 0, "X"))
    print(game_board)

