import pandas as pd

# Load the dataset (assuming it's a CSV file)
# Replace 'your_dataset.csv' with the path to your ball-by-ball dataset
df = pd.read_csv('dataset/IPL_ball_by_ball_updated.csv')


# Extract unique teams from the 'batting team' column
unique_teams = sorted(df['batting_team'].unique())

# Save the unique teams into a text file
with open('teams.txt', 'w') as f:
    for team in unique_teams:
        f.write(f"{team}\n")

print("Unique teams saved in 'unique_teams.txt'")
