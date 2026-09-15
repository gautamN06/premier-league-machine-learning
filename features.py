team_stats = {}

def get_team_stats(team):
    if team not in team_stats:
        team_stats[team]={
            "wins":0,
            "draws": 0,
            "losses":0,
            "goals_for":0,
            "goals_against":0
        }

    return team_stats[team]


def update_team_stats(team, goals_for, goals_against):
    stats = get_team_stats(team)

    stats["goals_for"] += goals_for 
    stats["goals_against"] += goals_against

    if goals_for > goals_against: 
        stats["wins"] += 1
    elif goals_for == goals_against:
        stats["draws"] += 1
    else:
        stats["losses"] += 1 


update_team_stats("Liverpool", 2,1)
update_team_stats("Liverpool", 7,0)

print(team_stats)