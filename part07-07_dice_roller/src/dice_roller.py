# Write your solution here
import random

def roll(die: str):
    dice = {
        "A": [3, 3, 3, 3, 3, 6],
        "B": [2, 2, 2, 5, 5, 5],
        "C": [1, 4, 4, 4, 4, 4],
    }
    return random.choice(dice[die])

def play(die1: str, die2: str, times: int):
    wins_die1, wins_die2, ties = 0, 0, 0
    for _ in range(times):
        roll_die1 = roll(die1)
        roll_die2 = roll(die2)
        if roll_die1 > roll_die2:
            wins_die1 += 1
        elif roll_die2 > roll_die1:
            wins_die2 += 1
        else:
            ties += 1
    return wins_die1, wins_die2, ties

if __name__ == "__main__":
    
    print("Rolling die A:", [roll("A") for _ in range(20)])
    print("Rolling die B:", [roll("B") for _ in range(20)])
    print("Rolling die C:", [roll("C") for _ in range(20)])

    
    result = play("A", "C", 1000)
    print("A vs. C:", result)
    result = play("B", "B", 1000)
    print("B vs. B:", result)

