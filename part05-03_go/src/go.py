# Write your solution here
def who_won(game_board: list):
    player1_count = 0
    player2_count = 0

    for row in game_board:
        for piece in row:
            if piece == 1:
                player1_count += 1
            elif piece == 2:
                player2_count += 1

    if player1_count > player2_count:
        return 1
    elif player2_count > player1_count:
        return 2
    else:
        return 0

if __name__ == '__main__':
    game_board1 = [
        [1, 2, 1],
        [1, 2, 2],
        [2, 1, 1]
    ]

    game_board2 = [
        [1, 2, 1],
        [1, 2, 2],
        [2, 1, 2]
    ]

    game_board3 = [
        [1, 2, 0],
        [1, 2, 2],
        [2, 1, 1]
    ]

    print(who_won(game_board1))  
    print(who_won(game_board2))  
    print(who_won(game_board3))  