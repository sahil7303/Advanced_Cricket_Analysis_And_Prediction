import pandas as pd

# Load the dataset (assuming it's a CSV file)
# Replace 'your_dataset.csv' with the path to your ball-by-ball dataset
df = pd.read_csv('../dataset/IPL_ball_by_ball_updated.csv')


# Extract unique teams from the 'batting team' column
unique_bowlers = sorted(df['bowler'].unique())

# Save the unique teams into a text file
with open('bowlers.txt', 'w') as f:
    for bowler in unique_bowlers:
        f.write(f"{bowler}\n")

print("Unique bowlers saved in 'bowlers.txt'")
