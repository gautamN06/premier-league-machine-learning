import pandas as pd 
from features import get_team_stats, update_team_stats

matches = pd.read_csv("data/matches.csv")

matches["Date"] = pd.to_datetime(matches["Date"], dayfirst=True)
matches = matches.sort_values("Date").reset_index(drop=True)

print(matches.head())

print("\n--- COLUMNS ---")
print(matches.columns.tolist())

print("\n------- DATASET SHAPE -------")
print(matches.shape)


print("\n------- MISSING VALUES -------")
print(matches.isnull().sum().sort_values(ascending=False).head(20))

print("\n------- RESULTS -------")
print(matches["FTR"].value_counts())

print("\n------- TEAMS -------")
print(sorted(matches["HomeTeam"].unique()))

print("\n------- DATE RANGE -------")
print(matches["Date"].min(), "to", matches["Date"].max())

