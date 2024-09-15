import pandas as pd

# Load the dataset (make sure the file path is correct)
df = pd.read_csv('../dataset/IPL_ball_by_ball_updated.csv')

# Extract unique values from 'striker', 'non striker', and 'bowler' columns
strikers = df['striker'].unique()
non_strikers = df['non_striker'].unique()
bowlers = df['bowler'].unique()

# Combine all unique players and remove duplicates
unique_players = sorted(set(strikers).union(set(non_strikers)).union(set(bowlers)))

# Save the unique players into a text file
with open('all_players.txt', 'w') as f:
    for player in unique_players:
        f.write(f"{player}\n")

print("Unique players saved in 'all_players.txt'")
