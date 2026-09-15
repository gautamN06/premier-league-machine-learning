import pandas as pd 



def load_matches():
    matches = pd.read_csv("data/matches.csv")

    #has the date range go from 2024 to 2025 rather than 2025 to 2024
    matches["Date"] = pd.to_datetime(matches["Date"], dayfirst=True)
    return matches 

if __name__ == "__main__":
    matches = load_matches()

    print(matches.head())

    print("\n------- COLUMNS -------")
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