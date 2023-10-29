class BallPlayer:
    def __init__(self, name: str, number: int, goals: int, assists: int, minutes: int):
        self.name = name
        self.number = number
        self.goals = goals
        self.assists = assists
        self.minutes = minutes

    def __str__(self):
        return (f'BallPlayer(name={self.name}, number={self.number}, '
                f'goals={self.goals}, assists={self.assists}, minutes={self.minutes})')


def most_goals(ball_players: list):
    if not ball_players:
        return None
    
    max_goals = -1
    top_scorer = None

    for player in ball_players:
        if player.goals > max_goals:
            max_goals = player.goals
            top_scorer = player.name

    return top_scorer


def most_points(ball_players: list):
    if not ball_players:
        return None
    
    max_points = -1
    top_player = None

    for player in ball_players:
        total_points = player.goals + player.assists
        if total_points > max_points:
            max_points = total_points
            top_player = (player.name, player.number)

    return top_player


def least_minutes(ball_players: list):
    if not ball_players:
        return None
    
    min_minutes = float('inf')
    least_minutes_player = None

    for player in ball_players:
        if player.minutes < min_minutes:
            min_minutes = player.minutes
            least_minutes_player = player

    return least_minutes_player


if __name__ == "__main__":
    player1 = BallPlayer("Archie Bonkers", 13, 5, 12, 46)
    player2 = BallPlayer("Speedy Tickets", 7, 2, 26, 55)
    player3 = BallPlayer("Cruella De Hill", 9, 1, 32, 26)
    player4 = BallPlayer("Devilled Tasmanian", 12, 1, 11, 41)
    player5 = BallPlayer("Donald Quack", 4, 3, 9, 12)
    
    team = [player1, player2, player3, player4, player5]
    print(most_goals(team))
    print(most_points(team))
    print(least_minutes(team))
