from load_data import load_matches

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


def create_features(matches):
    rows = []

    team_stats.clear()

    for _, match in matches.iterrows():

        home_team = match["HomeTeam"]
        away_team = match["AwayTeam"]

        home_stats = get_team_stats(home_team)
        away_stats = get_team_stats(away_team)


        row = {
            #looking at stats for teams at home 
            "home_wins": home_stats["wins"],
            "home_draws": home_stats["draws"],
            "home_losses": home_stats["losses"],
            "home_goals_for": home_stats["goals_for"],
            "home_goals_against": home_stats["goals_against"],

            #looking at stats for away
            "away_wins": away_stats["wins"],
            "away_draws": away_stats["draws"],
            "away_losses": away_stats["losses"],
            "away_goals_for": away_stats["goals_for"],
            "away_goals_against": away_stats["goals_against"],    

            "result": match["FTR"]       

        }

        rows.append(row)

        update_team_stats(
            home_team, 
            match["FTHG"],
            match["FTAG"]
        )

        update_team_stats(
            away_team,
            match["FTAG"],
            match["FTHG"]
        )

    return rows 


if __name__ == "__main__":
    matches = load_matches()
    features = create_features(matches)

    print(f"Number of feature rows:  {len(features)}")
    print(f"Number of matches: {len(matches)}")

    print("\n First 5 feature rows:")
    for row in features[:5]:
        print(row)
